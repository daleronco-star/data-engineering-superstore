\# Superstore Sales – Data Engineering ETL Pipeline



\## Project Overview



This project implements an ETL (Extract, Transform, Load) pipeline using Python, Pandas and MySQL.



The pipeline processes the Superstore sales dataset, performs data cleaning and quality checks, saves the transformed data into a CSV file, and loads the results into a MySQL database.



The project demonstrates the main stages of a data engineering workflow, from raw data extraction to database loading and validation.



\## Project Objectives



\- Extract data from a CSV source.

\- Clean and transform the dataset using Pandas.

\- Perform data quality checks.

\- Save the processed dataset as a CSV file.

\- Load the transformed data into a MySQL database.

\- Validate the number of records and primary key uniqueness.

\- Implement logging to monitor pipeline execution.



\## Technologies Used



\- \*\*Python\*\* – Main programming language.

\- \*\*Pandas\*\* – Data manipulation and transformation.

\- \*\*MySQL\*\* – Relational database for data storage.

\- \*\*SQLAlchemy\*\* – Database connection and interaction.

\- \*\*PyMySQL\*\* – MySQL database driver.

\- \*\*Python-dotenv\*\* – Environment variable management.

\- \*\*Jupyter Notebook\*\* – Development and execution environment.

\- \*\*Git \& GitHub\*\* – Version control and project hosting.



\## Project Structure



```text

data-engineering-superstore/

│

├── data/

│   ├── raw/

│   │   └── superstore.csv

│   │

│   └── processed/

│       └── superstore\_clean.csv

│

├── notebooks/

│   └── etl\_pipeline.ipynb

│

├── src/

│   └── logger.py

│

├── sql/

│   └── create\_tables.sql

│

├── .gitignore

└── requirements.txt

```



\## ETL Pipeline



\### 1. Extract



\- Load the original Superstore CSV dataset.

\- Read the source data using Pandas.

\- Record the extraction process through logging.



\### 2. Transform



\- Inspect the dataset structure.

\- Identify missing values.

\- Check for duplicate records.

\- Standardize column names.

\- Convert date columns to datetime format.

\- Perform data quality checks on numerical fields and dates.



\### 3. Load



\- Save the cleaned dataset as `superstore\_clean.csv`.

\- Connect to the MySQL database.

\- Load the transformed records into the `superstore\_sales` table.

\- Use a full refresh strategy to replace the existing table data within a transaction.



\### 4. Validation



\- Compare the number of records in the Python DataFrame with the number stored in MySQL.

\- Verify primary key uniqueness.

\- Record pipeline execution through logging.



\## Results



The pipeline was successfully executed with the following results:



| Metric | Result |

|---|---:|

| Extracted records | 9,994 |

| Processed records | 9,994 |

| Loaded records | 9,994 |

| Data quality anomalies | 0 |

| Unique primary keys | 9,994 |

| Database validation | Passed |



\## Setup and Installation



\### 1. Clone the repository



```bash

git clone https://github.com/daleronco-star/data-engineering-superstore.git

cd data-engineering-superstore

```



\### 2. Install dependencies



```bash

pip install -r requirements.txt

```



\### 3. Configure environment variables



Create a `.env` file in the project root directory:



```env

DB\_HOST=localhost

DB\_PORT=8889

DB\_NAME=data\_engineering

DB\_USER=your\_username

DB\_PASSWORD=your\_password

```



Replace the example values with your own MySQL configuration.



\### 4. Create the database and table



Create the `data\_engineering` database in MySQL and execute the SQL script:



```text

sql/create\_tables.sql

```



\### 5. Run the ETL pipeline



Open Jupyter Notebook and execute:



```text

notebooks/etl\_pipeline.ipynb

```



Run the notebook cells in order, from the imports to the final validation.



\## Logging



The project includes a logging module in `src/logger.py`.



Pipeline execution information is recorded locally in:



```text

logs/pipeline.log

```



The log records pipeline initialization, extraction, transformation, loading and completion events.



\## Future Improvements



\- Modularize the ETL pipeline into independent Python modules.

\- Improve error handling and pipeline reliability.

\- Implement automated pipeline execution.

\- Add more advanced data quality checks.

\- Expand the project with additional analytical queries.



\## Author



Data Engineering Portfolio Project



\*\*GitHub:\*\* \[daleronco-star](https://github.com/daleronco-star)

