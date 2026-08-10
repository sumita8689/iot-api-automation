\# IoT API Automation Framework



A Python-based API automation framework for testing REST APIs using Pytest and Behave (BDD).



The framework validates API responses against expected data, performs database validation using SQLite, and supports automated test execution through Docker and GitHub Actions CI.



\## Tech Stack



\- Python 3.13

\- Pytest

\- Requests

\- Behave (BDD)

\- SQLite

\- Docker

\- GitHub Actions



\## What is Tested



\- GET products

\- GET a single product

\- Negative API scenarios

\- POST/create product

\- PUT/update product

\- DELETE product

\- API response validation

\- API-to-database validation

\- Data-driven testing with Pytest

\- BDD scenarios with Behave



\## Project Structure



```text

iot-api-automation/

│

├── api/                    # API classes and endpoint methods

├── database/               # Database connection and utility functions

├── features/               # Behave feature files and step definitions

├── tests/                  # Pytest API and database tests

├── test\_data/              # Test data

├── utilities/              # Shared utilities

├── .github/

│   └── workflows/

│       └── tests.yml       # GitHub Actions CI workflow

├── Dockerfile              # Docker test environment

├── requirements.txt        # Python dependencies

├── README.md

└── .gitignore

```



\## Running the Tests



\### Install dependencies



```bash

pip install -r requirements.txt

```



\### Run Pytest



```bash

python -m pytest -v

```



\### Run Behave



```bash

python -m behave

```



\### Run the complete test suite with Docker



Build the Docker image:



```bash

docker build -t iot-api-automation .

```



Run the tests:



```bash

docker run --rm iot-api-automation

```



The Docker container runs both the Pytest and Behave test suites.



\## Continuous Integration



GitHub Actions automatically runs the test suite whenever code is pushed to the repository.



The CI pipeline:



1\. Checks out the repository

2\. Builds the Docker image

3\. Runs the complete test suite inside the Docker container

4\. Reports the test result



\## Test Reporting



Pytest generates an HTML test report using the configured reporting setup.



\## Database Validation



The framework uses SQLite to validate API responses against database data.



\## BDD Testing



Behave is used to implement BDD scenarios for API operations including:



\- GET product

\- POST product

\- Data-driven scenarios

\- Scenario Outlines

\- Data Tables

