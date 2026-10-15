Dataset shape: 10,459 rows × 24 columns

Target:
- Good: 5,000
- Bad: 5,459

Predictors:
- 23 numeric credit-history features

Missing/data-quality findings:
- No standard NaN values
- Special codes -7, -8 and -9 are used
- 588 rows have all predictor values equal to -9
- Those 588 rows contain 323 Bad and 265 Good labels
- One additional duplicate pair exists outside the all -9 rows
- 587 duplicate rows are reported by pandas
