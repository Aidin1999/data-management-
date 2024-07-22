# Data Management Project

## Overview

This document is part of my job in data management, where I handle large datasets. The tasks include normalizing data and creating a database in MySQL. 

## Project Components

### Database Design

In the diagram file, you can see the database schema designed for this project. The diagram was created using MySQL Workbench, and a picture of the design is included.

### SQL File

The SQL file generated from the database design is provided. This file contains the necessary commands to create the database schema in MySQL.

### Python Scripts

#### `copped.py`
This script is responsible for cropping the original data file into a manageable format.

#### `chunck.py`
This script divides the cropped data into two parts for easier importing into the database.

### Data Import

The `import.py` script handles the process of importing the split data files into the MySQL database.

### Exploratory Data Analysis (EDA)

The `eda.py` script includes various visualizations to explore and understand the data.

### Queries

#### RDBMS Queries
There are three SQL query files for testing purposes:
- `query-a.sql`
- `query-b.sql`
- `query-c.sql`

These queries are designed to ensure the accuracy of the database operations.

#### MongoDB Query
The `mongo-db-queries.txt` file contains a MongoDB query. The first command in this file denormalizes the data, and the subsequent commands are used for testing.

## File Structure

- **Diagram File**: Contains the database schema design.
- **SQL File**: Includes the commands to create the database schema.
- **Python Files**:
  - `copped.py`: Crops the original data file.
  - `chunck.py`: Splits the data into two parts.
  - `import.py`: Imports the data into the database.
  - `eda.py`: Contains the EDA visualizations.
- **Queries**:
  - `query-a.sql`
  - `query-b.sql`
  - `query-c.sql`
  - `mongo-db-queries.txt`

## Conclusion

This project demonstrates the complete workflow of managing and processing large datasets, from normalization and database creation to data import, EDA, and querying. It showcases the integration of different technologies and tools to achieve efficient data management and analysis.

---

**Project by:** [Your Name]
