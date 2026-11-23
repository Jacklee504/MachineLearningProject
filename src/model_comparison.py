import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import ConfusionMatrixDisplay


def load_and_split():
    data_path = Path(__file__).resolve().parents[1] / "private" / "heloc_dataset_v1.csv"
    data = pd.read_csv(data_path)

    all_minus9 = data.drop(columns="RiskPerformance").eq(-9).all(axis=1)
    data = data.loc[~all_minus9].drop_duplicates().copy()

    y = data["RiskPerformance"].map({"Good": 0, "Bad": 1})
    if y.isna().any():
        raise ValueError("RiskPerformance contains an unexpected label")

    X = data.drop(columns="RiskPerformance")

    X = X.mask(X.isin([-7, -8, -9]))

    return train_test_split(
        X,
        y,
        test_size=0.20,
        stratify=y,
        random_state=42,
    )


X_train, X_test, y_train, y_test = load_and_split()


def make_models():

    return {
        "Dummy Baseline": Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median", add_indicator=True)),
                ("classifier", DummyClassifier(strategy="prior")),
            ]
        ),
        "LogisticRegression": Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median", add_indicator=True)),
                ("scaler", StandardScaler()),
                ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
            ]
        ),
        "RandomForest": Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median", add_indicator=True)),
                ("classifier", RandomForestClassifier(random_state=42)),
            ]
        )
    }

def evaluate(name, model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    bad_probabilities = model.predict_proba(X_test)[:, 1]

    cr = classification_report(y_test, predictions, target_names=["Good", "Bad"], output_dict=True, zero_division=0)
    
    metrics = {
        "Accuracy": cr["accuracy"],
        "Bad precision": cr["Bad"]["precision"],
        "Bad recall": cr["Bad"]["recall"],
        "Bad F1": cr["Bad"]["f1-score"],
        "Good recall": cr["Good"]["recall"],
        "ROC-AUC": roc_auc_score(y_test, bad_probabilities),
    }    
    
    return metrics, confusion_matrix(y_test, predictions, labels=[0, 1])

def save_confusion_matrix(matrix):
    display = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=["Good", "Bad"])
    display.plot()
    display.ax_.set_title("Random Forest Confusion Matrix")
    display.ax_.set_xlabel("Predicted label")
    display.ax_.set_ylabel("Actual label")
    display.figure_.savefig("docs/random_forest_confusion_matrix.png")


models = make_models()
folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("Training-set cross-validation (5 stratified folds):")
print("| Model | Bad F1 (mean ± SD) | Bad recall (mean ± SD) | ROC-AUC (mean ± SD) |")
print("|---|---:|---:|---:|")
for name in ("LogisticRegression", "RandomForest"):
    scores = cross_validate(
        models[name], X_train, y_train, cv=folds,
        scoring={"bad_f1": "f1", "bad_recall": "recall", "roc_auc": "roc_auc"},
    )
    print(
        f"| {name} | {scores['test_bad_f1'].mean():.3f} ± {scores['test_bad_f1'].std():.3f} | "
        f"{scores['test_bad_recall'].mean():.3f} ± {scores['test_bad_recall'].std():.3f} | "
        f"{scores['test_roc_auc'].mean():.3f} ± {scores['test_roc_auc'].std():.3f} |"
    )

print("\nHeld-out test results:")
print("| Model | Accuracy | Bad precision | Bad recall | Bad F1 | Good recall | ROC-AUC |")
print("|---|---:|---:|---:|---:|---:|---:|")

matrices = []
for name, model in models.items():
    metrics, matrix = evaluate(name, model, X_train, X_test, y_train, y_test)
    print(
        f"| {name} | {metrics['Accuracy']:.3f} | "
        f"{metrics['Bad precision']:.3f} | {metrics['Bad recall']:.3f} | "
        f"{metrics['Bad F1']:.3f} | {metrics['Good recall']:.3f} | "
        f"{metrics['ROC-AUC']:.3f} |"
    )
    matrices.append((name, matrix))

forest_matrix = next(matrix for name, matrix in matrices if name == "RandomForest")
save_confusion_matrix(forest_matrix) 


print("\n| Model | Good → Good | Good → Bad | Bad → Good | Bad → Bad |")
print("|---|---:|---:|---:|---:|")
for name, matrix in matrices:
    print(
        f"| {name} | {matrix[0, 0]} | {matrix[0, 1]} | "
        f"{matrix[1, 0]} | {matrix[1, 1]} |"
    )
