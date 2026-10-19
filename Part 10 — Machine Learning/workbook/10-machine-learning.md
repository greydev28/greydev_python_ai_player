# Part 10 — Machine Learning with scikit-learn

## Vocabulary
- **Feature (X):** information supplied to a model.
- **Target (y):** the value/category to predict.
- **Training:** fit parameters from training examples.
- **Inference:** use a fitted model to make predictions.
- **Classification:** predict a category.
- **Regression:** predict a numerical value.
- **Baseline:** simple reference model used to judge whether complexity helps.
- **Generalisation:** performance on unseen examples.

## The safe workflow
1. Define the prediction target and how predictions will be used.
2. Split training and test data. Do not tune decisions on the test set.
3. Build a simple baseline.
4. Preprocess within a pipeline so transformations are fitted only on training folds.
5. Select metrics that match the cost of errors.
6. Use cross-validation for model selection.
7. Evaluate once on the held-out test set.
8. Inspect errors, subgroup performance, and limitations.
9. Save the pipeline and document data/model versions.

## Metrics
Classification: accuracy, precision, recall, F1, confusion matrix, ROC-AUC (when appropriate). Accuracy can be misleading on imbalanced classes. Regression: MAE, MSE/RMSE, and R². Choose metrics based on the actual use case, not because one number looks impressive.

## Leakage
Leakage occurs when training receives information unavailable at prediction time or information from the test set. Examples: scaling the entire dataset before splitting, using a future outcome as a feature, or duplicates crossing the split.

## Exercises
1. Train a majority-class baseline and a logistic regression classifier on a public beginner dataset.
2. Compare accuracy, precision, recall, and F1. Explain the trade-offs.
3. Build a regression model and report MAE against a baseline.
4. Demonstrate data leakage in a toy example, then fix it using a pipeline.
5. Write a model card: intended use, data, metrics, known limitations, and risks.

## Greydev Advanced Challenge — Defensible Machine Learning

1. Choose a non-sensitive dataset and define the prediction target, intended use, and cost of false positives versus false negatives before training.
2. Build a naive baseline and at least two stronger models. Use a reproducible split and cross-validation; keep the test set untouched until the final comparison.
3. Build preprocessing inside a scikit-learn pipeline. Demonstrate a leakage-prone approach in a separate experiment, then explain why its reported score is misleading.
4. Evaluate imbalanced classification using precision, recall, F1, a confusion matrix, and an appropriate threshold analysis. Explain which errors matter most for your use case.
5. Inspect errors and subgroup performance where ethically and statistically appropriate. Discuss uncertainty, representativeness, fairness risks, and limitations.
6. Save the full preprocessing/model pipeline, reload it in a clean process, and prove that predictions are reproducible. Write a model card and a model-change log.

