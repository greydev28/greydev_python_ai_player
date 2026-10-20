# Part 09 — Data & Mathematics for AI

AI engineering depends on data reasoning, not just model APIs. Learn enough mathematics to understand model behaviour and enough data tooling to detect bad inputs.

## NumPy
An array is a typed, often multidimensional collection designed for numerical operations. Learn shape, dimensions, indexing, slicing, broadcasting, vectorised operations, aggregation, and random number generation. Shape mismatches are among the most common early errors.

## pandas
A `DataFrame` is tabular data with labelled rows and columns. Practise loading CSV files, inspecting `.head()`, `.info()`, `.describe()`, handling missing values, filtering rows, grouping, joining, and exporting results. Always inspect data before modelling.

## Visualisation
Use charts to answer questions. Label axes, include units, title the chart, and do not distort the scale. A chart should support a conclusion, not merely look attractive.

## Statistics
- Mean: arithmetic average; sensitive to outliers.
- Median: middle value; often robust to outliers.
- Variance/standard deviation: spread around the mean.
- Correlation: association, not proof of causation.
- Probability: quantify uncertainty and update beliefs with evidence.
- Sampling bias: your data may not represent the population you care about.

## Linear algebra intuition
A scalar is one number, a vector is an ordered list of numbers, a matrix is a 2D array, and a tensor generalises arrays to more dimensions. A model often maps input features (vectors/matrices) to predictions using learned parameters.

## Data workflow
1. State the question and unit of analysis.
2. Inspect schema, types, missingness, duplicates, and suspicious values.
3. Split data before fitting preprocessing transformations.
4. Establish a simple baseline.
5. Visualise and evaluate.
6. Record assumptions and limitations.

## Exercises
1. Use NumPy to create a 5x3 array and compute each column's mean.
2. Load a CSV with pandas and report row count, missing values per column, and duplicate rows.
3. Group a sales table by product and calculate total revenue.
4. Create a histogram and a scatter plot with clear labels.
5. Explain with an example why correlation does not establish causation.
6. Write a data-quality report before attempting any model.

## Greydev Advanced Challenge — Data Quality and Mathematical Reasoning

1. Analyse a real public dataset with at least 10,000 rows. Document its source/licence, column meanings, missingness, duplicates, outliers, and potential sampling bias before making charts.
2. Implement a reproducible cleaning pipeline that separates raw data from transformed data. Make every transformation explicit and explain how you avoid changing the source dataset.
3. Investigate a surprising correlation. Use plots and domain reasoning to explain why correlation does not establish causation; identify confounders and what additional evidence would be needed.
4. Compare vectorised NumPy/pandas operations with a Python loop on the same data. Validate that the outputs agree, measure performance, and explain the limitations of the benchmark.
5. Write a short report connecting distributions, variance, sampling uncertainty, vectors/matrices, and a real decision. Include at least one conclusion the data does **not** justify.

