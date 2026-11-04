# Data Engineering Project – Superstore ETL Pipeline

## Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python, Pandas, and MySQL.

The goal is to extract raw Superstore sales data, clean and transform it, and load the processed dataset into a MySQL database.

The entire ETL workflow is developed and documented in a single Jupyter Notebook.

## Project Objectives

- Build an end-to-end ETL pipeline.
- Extract data from a CSV file.
- Clean and transform raw data using Pandas.
- Perform data quality and integrity checks.
- Load processed data into MySQL.
- Implement logging to monitor pipeline execution.
- Document the workflow and make it reproducible.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data extraction and transformation |
| MySQL | Relational database |
| SQLAlchemy | Database connection and operations |
| PyMySQL | MySQL driver |
| Jupyter Notebook | ETL workflow development |
| Python Logging | Execution monitoring |
| Git and GitHub | Version control |

## Project Structure

```text
data-engineering/
│
├── data/
│   ├── raw/
│   │   └── superstore.csv
│   │
│   └── processed/
│       └── superstore_clean.csv
│
├── notebooks/
│   └── etl_pipeline.ipynb
│
├── src/
│   └── logger.py
│
├── sql/
│   └── create_tables.sql
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ETL Pipeline

The pipeline is organized into three main stages.

### 1. Extract

- Read the raw Superstore CSV dataset.
- Handle file encoding when necessary.
- Load the data into a Pandas DataFrame.
- Record the extraction process through logging.

### 2. Transform

- Inspect the dataset structure and data types.
- Check missing values and duplicates.
- Clean and standardize column names.
- Convert date columns into datetime format.
- Standardize data types.
- Perform data quality checks.

### 3. Load

- Save the cleaned dataset as a CSV file.
- Connect to MySQL using SQLAlchemy.
- Load the transformed data into the `superstore_sales` table.
- Use a transactional full refresh to ensure data consistency.
- Record the loading process through logging.

## Data Quality and Validation

The pipeline includes validation checks to ensure data consistency and integrity.

The following checks are performed:

- Missing values inspection.
- Duplicate records inspection.
- Data type validation.
- Primary key uniqueness verification.
- Comparison between the number of records in the DataFrame and the MySQL table.

## Results

The ETL pipeline was successfully executed and validated.

| Metric | Result |
|---|---:|
| Total records extracted | 9,994 |
| Total records processed | 9,994 |
| Total records loaded into MySQL | 9,994 |
| Duplicate records | 0 |
| Unique primary keys | 9,994 |
| DataFrame / MySQL count match | True |

All implemented validation checks were successfully passed.

## Logging

The project includes a logging system implemented in `src/logger.py`.

Logs are written to:

```text
logs/pipeline.log
```

The logging system records:

- Pipeline execution start and completion.
- Data extraction.
- Data transformation.
- CSV export.
- MySQL loading.
- Errors and exceptions.

Log files are stored locally and excluded from version control.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/daleronco-star/data-engineering-superstore.git

cd data-engineering-superstore
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```text
DB_HOST=localhost
DB_PORT=8889
DB_NAME=data_engineering
DB_USER=root
DB_PASSWORD=your_password
```

Replace `your_password` with your own MySQL password.

### 4. Create the database and table

Create the `data_engineering` database in MySQL and execute:

```text
sql/create_tables.sql
```

### 5. Run the ETL pipeline

Open Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
notebooks/etl_pipeline.ipynb
```

Execute the notebook cells in order.

## Future Improvements

- Improve error handling.
- Implement automated pipeline execution.
- Add more advanced data quality checks.
- Expand the project with additional datasets.

## Author

**Daleronco**

GitHub: [daleronco-star](https://github.com/daleronco-star)
