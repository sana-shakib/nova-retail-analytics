http://10.145.120.214:8502

# Nova Retail Analytics

## End-to-End Data Analytics and Machine Learning Case Study

**Nova Retail Group** is a fictional retail and e-commerce company operating in the cosmetics, fragrance, and skincare industry.

This project presents an end-to-end business analytics solution designed to transform transactional data into actionable insights. The workflow covers data generation, relational database design, data loading, SQL analysis, exploratory data analysis, customer intelligence, machine learning, sales forecasting, and interactive business intelligence.

The project is designed to demonstrate how data can be transformed into practical insights that support decision-making across sales, customers, products, inventory, marketing, and revenue planning.

---

## Project Overview

Nova Retail Analytics combines multiple analytical disciplines into a single business-oriented project:

* Data Generation and Preparation
* Relational Database Design
* PostgreSQL Data Management
* SQL Business Analysis
* Python Data Analysis
* Exploratory Data Analysis
* Customer Segmentation
* RFM Analysis
* Machine Learning
* Sales Forecasting
* Forecast Evaluation
* Interactive Streamlit Dashboard
* Data Quality and Validation

The objective is not only to build analytical models, but to create a complete analytics workflow that connects technical implementation with business decision-making.

---

## Project Snapshot

| Metric                    |               Value |
| ------------------------- | ------------------: |
| Industry                  | Retail & E-commerce |
| Business Model            |                 B2C |
| Sales Channels            |   Online & Physical |
| Branches                  |                   5 |
| Analysis Period           |           2022–2025 |
| Transactions              |              50,000 |
| Units Sold                |             150,147 |
| Total Revenue             |          523.6B IRR |
| Average Transaction Value |          10.47M IRR |

---

## Business Objectives

The project addresses several key business questions:

* How does revenue change over time?
* Which branches generate the highest revenue?
* Which products contribute most to overall sales?
* Which customers generate the highest business value?
* What customer segments can be identified?
* Which customers may be at risk of becoming inactive?
* How effective are marketing campaigns?
* How can inventory performance be monitored?
* How can historical sales data be used for revenue forecasting?

---

## End-to-End Analytics Workflow

```text
Business Understanding
        |
        v
Data Generation
        |
        v
Database Design
        |
        v
PostgreSQL Data Loading
        |
        v
SQL Analysis
        |
        v
Python Data Analysis
        |
        v
Feature Engineering
        |
        v
Customer Segmentation
        |
        v
Machine Learning
        |
        v
Sales Forecasting
        |
        v
Forecast Evaluation
        |
        v
Streamlit Dashboard
        |
        v
Business Insights
```

---

## Database Architecture

PostgreSQL is used as the primary relational database for the project.

The database contains multiple entities designed to represent the main operational areas of a retail business.

### Core Entities

* Customers
* Products
* Sales
* Orders
* Order Details
* Payments
* Inventory
* Branches
* Marketing Campaigns
* Customer Feedback

The database structure supports transactional analysis, customer analytics, product performance analysis, inventory monitoring, and marketing evaluation.

---

## Sales Analytics

The sales analytics layer focuses on understanding revenue performance and transaction behavior.

### Analysis Areas

* Revenue trends
* Monthly and yearly sales
* Transaction volume
* Average transaction value
* Branch performance
* Product performance
* Units sold
* Revenue contribution

### Key Results

| KPI                       |     Result |
| ------------------------- | ---------: |
| Total Transactions        |     50,000 |
| Total Units Sold          |    150,147 |
| Total Revenue             | 523.6B IRR |
| Average Transaction Value | 10.47M IRR |

These metrics provide a high-level view of the overall commercial performance of the business.

---

## Customer Analytics

Customer analytics focuses on understanding purchasing behavior and customer value.

### Analytical Areas

* Purchase frequency
* Recency
* Monetary value
* Customer purchasing behavior
* RFM analysis
* Customer segmentation
* Customer churn risk

RFM analysis is used to identify meaningful customer groups and support targeted retention and marketing strategies.

Potential customer groups include:

* High-value customers
* Loyal customers
* Recently active customers
* At-risk customers
* Inactive customers

---

## Product and Inventory Analytics

Product and inventory analysis evaluates product performance and stock-related business factors.

### Analysis Areas

* Best-selling products
* Revenue contribution
* Sales volume
* Inventory levels
* Product profitability
* Stock management
* Potential inventory risks

These insights can help support product prioritization and inventory planning.

---

## Marketing Analytics

Marketing analytics evaluates campaign activity and its relationship with customer behavior and revenue.

### Analysis Areas

* Campaign performance
* Customer response
* Revenue impact
* Campaign effectiveness
* Target customer opportunities

The objective is to provide a data-driven foundation for improving marketing allocation and customer targeting.

---

## Machine Learning

Machine learning is applied to business problems where predictive analytics can provide additional value.

The project focuses primarily on sales forecasting while also incorporating customer-oriented analytical techniques.

### Sales Forecasting

Historical sales data is transformed into time-based and business-related features and used to predict future sales.

The forecasting pipeline includes:

* Historical sales aggregation
* Time-series feature engineering
* Model training
* Future prediction
* Model evaluation
* Forecast visualization

### Forecast Evaluation

| Metric |      Result |
| ------ | ----------: |
| MAE    | 404.98M IRR |
| RMSE   | 538.34M IRR |
| MAPE   |       3.73% |

The evaluation results indicate strong forecasting performance on the selected evaluation dataset, with a MAPE of 3.73%.

---

## Customer Segmentation

Customer segmentation is based on RFM analysis.

### RFM Dimensions

**Recency**
How recently a customer made a purchase.

**Frequency**
How frequently a customer purchases.

**Monetary**
How much revenue a customer generates.

The resulting segments can be used to support:

* Customer retention
* Targeted marketing
* Loyalty strategies
* Customer prioritization
* Churn-risk management

---

## Interactive Dashboard

The project includes a modular Streamlit dashboard that provides a management-oriented view of business performance.

### Dashboard Modules

* Overview
* Sales
* Products
* Marketing
* Forecast

The dashboard combines KPIs, visualizations, analytical services, database connectivity, data validation, and machine learning outputs into a unified interface.

---

## Dashboard Architecture

The application follows a modular service-oriented structure.

```text
Streamlit Interface
        |
        +-- Pages
        |
        +-- Components
        |
        +-- Services
              |
              +-- Data Management
              +-- KPI Services
              +-- Sales Services
              +-- Customer Services
              +-- Marketing Services
              +-- Forecasting
              +-- Data Validation
              +-- Data Quality
              |
              v
        PostgreSQL / Data Layer
```

This architecture improves maintainability, testability, scalability, and separation of responsibilities.

---

## Technology Stack

### Programming

* Python
* SQL

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-learn
* XGBoost
* LightGBM

### Database

* PostgreSQL
* SQLAlchemy

### Dashboard

* Streamlit

### Development and Documentation

* Jupyter Notebook
* Excel
* Git
* GitHub

---

## Repository Structure

```text
nova-retail-analytics/
|
+-- 03_Data_Generation/
|   +-- generate_data.py
|   +-- generate_sales.py
|   +-- generate_products.py
|   +-- generate_customers.py
|   +-- generate_inventory.py
|   +-- generate_marketing_campaigns.py
|   +-- generate_order_details.py
|   +-- generate_orders.py
|   +-- generate_payments.py
|   +-- generate_branches.py
|   +-- generate_customer_feedback.py
|   +-- sales.csv
|   +-- customers.csv
|   +-- products.csv
|   +-- inventory.csv
|   +-- orders.csv
|   +-- order_details.csv
|   +-- payments.csv
|   +-- branches.csv
|   +-- marketing_campaigns.csv
|   +-- customer_feedback.csv
|
+-- 04_Data_Loading/
|   +-- insert_data.py
|
+-- 05_SQL_Analysis/
|   +-- sales_analysis.sql
|   +-- customer_analysis.sql
|   +-- product_analysis.sql
|
+-- 07_Python_Analysis/
|   +-- 01_sales_analysis.ipynb
|   +-- outputs/
|
+-- dashboard/
|   +-- app.py
|   +-- config.py
|   +-- assets/
|   +-- components/
|   +-- pages/
|   +-- services/
|   +-- utils.py
|
+-- connection.py
+-- requirements.txt
+-- tables_description.xlsx
+-- README.md
+-- .gitignore
```

---

## Performance and Optimization

The dashboard incorporates several performance-oriented improvements:

* Cached data loading
* Reduced repeated database operations
* Optimized forecasting workflow
* Prevention of unnecessary model retraining
* Data type normalization
* Data validation
* Modular service architecture

The forecasting workflow was specifically optimized to avoid unnecessary model retraining during normal dashboard execution.

---

## Data Quality and Validation

The project includes dedicated data quality and validation components to improve reliability throughout the analytics pipeline.

Validation includes:

* Data type normalization
* Missing-value handling
* Required-column validation
* Data consistency checks
* Input validation
* Analytical data preparation

This ensures that downstream analytics and machine learning processes operate on structured and validated data.

---

## Testing

The dashboard and analytical services include dedicated test modules covering key components of the application.

Testing areas include:

* Sales services
* KPI services
* Customer services
* Customer segmentation
* Forecasting
* Forecast evaluation
* Marketing services
* Data processing

The goal is to reduce regression risk and improve the reliability of analytical services.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sanashakibb-maker/nova-retail-analytics.git
cd nova-retail-analytics
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Configure the PostgreSQL database connection according to the project's configuration.

---

## Running the Dashboard

From the project root:

```bash
streamlit run dashboard/app.py
```

The application will start through the local Streamlit server.

---

## Data and Security

This repository is structured as a portfolio project and does not contain production credentials.

Sensitive configuration values should be stored through environment variables and excluded from version control.

Database backups, environment files, logs, caches, temporary files, and other sensitive artifacts are excluded through `.gitignore` where appropriate.

---

## Project Status

**Portfolio Ready**

Implemented components include:

* Data generation
* PostgreSQL database
* Data loading pipeline
* SQL analytics
* Python data analysis
* Exploratory analysis
* Customer segmentation
* RFM analysis
* Machine learning
* Sales forecasting
* Forecast evaluation
* Interactive Streamlit dashboard
* Data validation
* Data quality checks
* Automated caching
* Modular application architecture
* Service-level testing
* Git and GitHub version control

---

## Future Improvements

Potential future extensions include:

* Real-time database integration
* Automated daily database backups
* Automated email reporting
* Advanced churn prediction
* Automated model retraining
* Cloud deployment
* Role-based dashboard access
* Automated data quality monitoring
* Advanced inventory forecasting
* CI/CD integration

---

## Author

**Sana Shakib**

Data Analyst | Data Science & Machine Learning

### Core Areas

Data Analysis | SQL | Python | Machine Learning | Forecasting | PostgreSQL | Business Intelligence | Streamlit

---

## Project Highlights

Nova Retail Analytics is an end-to-end retail analytics solution that brings together:

**Data Engineering + SQL Analytics + Python Analysis + Machine Learning + Forecasting + Business Intelligence**

The project demonstrates how a complete data workflow can be designed to move from raw business data to analytical insights and decision-support tools.
