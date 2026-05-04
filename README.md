# Lakehouse Road Accidents France

## Project Overview

This project is a Data Engineering portfolio project that builds a Lakehouse pipeline using Python, PySpark and a Bronze/Silver/Gold architecture.

The goal is to process French road accident open data and transform raw CSV files into clean, reliable and analytics-ready datasets.

## Business Objective

The project aims to answer questions such as:

- Which departments have the highest number of road accidents?
- What are the most accident-prone hours?
- How does accident severity vary by user type?
- What trends can be observed by month or year?

## Tech Stack

- Python
- PySpark
- Spark SQL
- Delta Lake / Parquet
- Git & GitHub
- Jupyter Notebook / Databricks-ready notebooks

## Architecture

The pipeline follows a Lakehouse architecture:

```text
Raw CSV files
    ↓
Bronze layer
    ↓
Silver layer
    ↓
Gold layer
    ↓
SQL analysis / BI reporting