- Dataset shape: 10,459 rows × 24 columns
- Variable types: 'RiskPerformance' is a string, all 23 predictors are integers.

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

After treating -7, -8 and -9 as missing, I reviewed the predictor statistics. Some of the values are way above 
its 75th percentiles. E.g. MSinceOldestTradeOpen has a maximum of 803 months compared with a 75th percentile
of 257, and NumBank2NatlTradesWHighUtilization has a maximum of 18 compared with a 75th percentile of 2. These 
values were kept as they aren't confirmed to be errors.