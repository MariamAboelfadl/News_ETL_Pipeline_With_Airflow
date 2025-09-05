#  News ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![SQLite](https://img.shields.io/badge/SQLite-Database-orange) 

Python | SQLite | News API | ETL

---

## ✨ Introduction

Welcome to the **News ETL Pipeline Project** 🚀

This repository demonstrates how to build a **ETL pipeline** that extracts news articles from a public API, transforms the data, and loads it into a **SQLite database**.

It’s designed as a showcase of **Data Engineering best practices**: modular Python scripts, clear task separation (Extract → Transform → Load), and an orchestrated workflow.

---

## ⚙️ Tech Stack

| Tool/Service        | Role                                              |
| ------------------- | ------------------------------------------------- |
| 📰 News API         | Source of articles published in the last 24 hours |
| 🐍 Python           | Orchestrates ETL tasks                            |
| 🗄 SQLite           | Stores transformed news data                      |
| 🔄 Python Scripts   | Modular Extract, Transform, Load logic            |
| 📂 Folder Structure | Organizes code & reusable components              |

---

## 🗂 Repository Structure

```
dags/
etl/
    extract_news.py        # Extract news articles from the API
    transform_news.py      # Clean & transform the data
    load_news.py           # Load transformed data into SQLite
news_etl_script.py         # Orchestrates all ETL tasks
__pycache__/               # Python cache files
README.md
```

---

## 🚀 Pipeline Overview

**Task Flow:**

```
extract_task → transform_task → load_task
```

1️⃣ **Extract (`extract_news.py`)**

* Fetches `author`, `content`, `source`, `title`, `publish_date`
* Only articles published in the **last 24 hours**

2️⃣ **Transform (`transform_news.py`)**

* Converts text to **lowercase**
* Converts column datatypes (e.g., `publish_date` → datetime)
* Cleans data (removes nulls, trims spaces)

3️⃣ **Load (`load_news.py`)**

* Stores the cleaned data into a **SQLite database** (`news.db`)
* Creates table if it doesn’t exist

4️⃣ **Orchestration (`news_etl_script.py`)**

* Runs ETL tasks sequentially: **Extract → Transform → Load**

---

## 📈 Key Learnings

* Build ETL pipeline in Python
* Extract data from APIs and handle JSON responses
* Transform and clean data for analytics
* Load and manage data in SQLite
* Orchestrate ETL tasks sequentially

---

## 🚧 Future Enhancements

* 🔍 Add **data quality checks** (missing values, duplicates)
* ☁ Migrate to **BigQuery** for larger datasets
* 📊 Add **analytics-ready views** or dashboards
