# HELOC Credit Performance Project

This project predicts whether a HELOC applicant has Good or Bad credit performance. See the [proposal](docs/ProjectProposal.md) 
and [data audit](docs/data_audit.md).

## Run

Use Python 3.12 in a virtual environment. Download the [HELOC dataset](https://www.kaggle.com/datasets/averkiyoliabev/home-equity-line-of-creditheloc) 
and place it at private/heloc_dataset_v1.csv before running the script.

From the project directory:

```bash
python -m pip install -r src/requirements.txt
python src/data_audit.py
python src/baseline.py
```

Repository: [MachineLearningProject](https://github.com/Jacklee504/MachineLearningProject).

[Baseline Results](docs/baseline_results.md)

## Assistance Declaration

I made use of ChatGPT/Codex when trying to find suitable datasets, as well as for creating a plan for each milestone so that I could work efficiently. I implemented the plans independently, using the plans as guidance. 

I used it to assist in the data audit as I was unsure of exactly what should be measured. I got it then to verify my data_audit implementation to ensure it was correct.