from pathlib import Path

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


data_path = Path(__file__).resolve().parents[1] / "private" / "heloc_dataset_v1.csv"
data = pd.read_csv(data_path)

all_minus9 = data.drop(columns="RiskPerformance").eq(-9).all(axis=1)
data = data.loc[~all_minus9].drop_duplicates().copy()

y = data["RiskPerformance"].map({"Good": 0, "Bad": 1})
if y.isna().any():
    raise ValueError("RiskPerformance contains an unexpected label")

X = data.drop(columns="RiskPerformance")

X = X.mask(X.isin([-7, -8, -9]))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42,
)

baseline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median", add_indicator=True)),
        ("classifier", DummyClassifier(strategy="prior")),
    ]
)
baseline.fit(X_train, y_train)

predictions = baseline.predict(X_test)
bad_probabilities = baseline.predict_proba(X_test)[:, 1]

print(f"Rows used: {len(data)}")
print(f"Training rows: {len(X_train)}")
print(f"Test rows: {len(X_test)}")
print(classification_report(
    y_test,
    predictions,
    labels=[0, 1],
    target_names=["Good", "Bad"],
    zero_division=0,
))
print(f"ROC-AUC:   {roc_auc_score(y_test, bad_probabilities):.3f}")
print("Confusion matrix (rows: actual Good/Bad; columns: predicted Good/Bad):")
print(confusion_matrix(y_test, predictions, labels=[0, 1]))
