# Project 1 — Supermarket Sales Analysis

## Overview
A portfolio-ready exploratory data analysis of a retail/supermarket-style sales dataset.

### Dataset
- Rows: 9,994
- Original columns: 21
- Period: 2014-01-03 to 2017-12-30
- Missing cells: 0
- Duplicate rows: 0

## Key Results
- Total sales: $2,297,200.86
- Total profit: $286,397.02
- Unique orders: 5,009
- Unique customers: 793
- Average order value: $458.61
- Profit margin: 12.47%

## Main Findings
1. Technology has the highest category sales.
2. West has the highest regional sales.
3. Sales increase strongly across the 2014–2017 period.
4. Tables generate substantial sales but negative aggregate profit.
5. Discount and profit show a negative association in this dataset.

## Deliverables
- `notebook/01_supermarket_sales_analysis.ipynb`
- `reports/supermarket_sales_report.pdf`
- `visualizations/`
- `src/`
- `data/supermarket_sales_clean.csv`

## Setup
```bash
pip install pandas numpy matplotlib seaborn jupyter reportlab
jupyter notebook
```

## Important interpretation note
Correlation and descriptive analysis identify associations. They do not establish causation.
