import pandas as pd

df = pd.read_csv(
    Path(__file__).resolve().parents[1] / "private" / "heloc_dataset_v1.csv"
)

print("Shape:", df.shape)
print("\nColumn types:")
print(df.dtypes)

print("\nTarget distribution:")
print(df["RiskPerformance"].value_counts())

print("\nMissing values:")
print(df.isna().sum().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

special_counts = pd.DataFrame({
    "-7": (df == -7).sum(),
    "-8": (df == -8).sum(),
    "-9": (df == -9).sum(),
})

print("\nSpecial value counts:")
print(special_counts[special_counts.sum(axis=1) > 0])

predictors = df.drop(columns="RiskPerformance")
all_minus9 = (predictors == -9).all(axis=1)

print("\nRows with all predictors = -9:", all_minus9.sum())
print(df.loc[all_minus9, "RiskPerformance"].value_counts())

numeric_clean = predictors.mask(predictors.isin([-7, -8, -9]))

print("\nDescriptive statistics:")
print(numeric_clean.describe())