# HELOC Credit Performance Project

[Repository Link](https://github.com/Jacklee504/MachineLearningProject)

```text
Can credit history predict whether a HELOC record is labelled Good or Bad? 
```

Both learned models outperformed the dummy baseline on ROC-AUC. Random forest had slightly higher mean Bad recall and F1 in cross-validation, while logistic regression had higher mean ROC-AUC.

## Project structure

- src/contains the audit, baseline, and model comparison scripts. The main script issrc/model_comparison.py
- docs/contains the proposal, audit, results, and confusion matrix.
- private/holds the dataset locally and is excluded from Git.

## Setup and run

Tested on macOS with Python 3.12. Package versions are pinned in [requirements.txt](src/requirements.txt).

From the project directory, runmkdir -p private Download the [FICO HELOC dataset from Kaggle](https://www.kaggle.com/datasets/averkiyoliabev/home-equity-line-of-creditheloc) and save it asprivate/heloc_dataset_v1.csv

Run these commands from the project directory. The audit summarises the dataset, the baseline sets a reference score, and the model comparison prints the final metrics and saves the random forest confusion matrix.

```bash
python3.12 -m venv .venv
source .venv/bin/activate

python -m pip install -r src/requirements.txt

python src/data_audit.py
python src/baseline.py
python src/model_comparison.py
```

## Documentation

- [Baseline Results](docs/baseline_results.md).
- [Model Comparison Results](docs/model_comparison.md).
- [Data Statement](docs/data_statement.md)
- [Model Card](docs/model_card.md)
- [Reflective Changelog](docs/reflective_changelog.md)

[Random forest confusion matrix](docs/random_forest_confusion_matrix.png)

## Assistance Declaration

I made use of ChatGPT/Codex when trying to find suitable datasets, as well as for creating a plan for each milestone so that I could work efficiently. I implemented the plans independently, using the plans as guidance. 

I used it to assist in the data audit as I was unsure of exactly what should be measured. I got it then to verify my data_audit implementation to ensure it was correct.

I also used it to clean up formatting of output such as for the model comparison tables, as I wanted the information to be clear.