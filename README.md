# python-frameworks
python frameworks assignment
# Frameworks_Assignment: CORD-19 Analysis

## 📌 Overview
This project analyzes the **CORD-19 metadata.csv dataset** and presents findings through visualizations and an interactive Streamlit app.

## 🚀 Features
- Data cleaning (dates, missing values, abstract word counts)
- Visualizations:
  - Publications per year
  - Top publishing journals
  - Word cloud of titles
- Interactive Streamlit dashboard

## 📂 Structure
- `notebooks/analysis.ipynb`: Data exploration & visualizations
- `app/streamlit_app.py`: Streamlit web app
- `data/metadata.csv`: Dataset
- `requirements.txt`: Dependencies

## 📊 Findings
- COVID-19 research peaked in 2020.
- Journals like *BMJ* and *The Lancet* published many papers.
- Frequent words in titles include *COVID*, *SARS-CoV-2*, and *pandemic*.

## 💡 Reflection
Challenges:
- Handling missing dates/journals
- Dataset size (needed sampling for faster testing)
Learnings:
- Streamlit makes sharing analysis interactive and simple
- Cleaning data is just as important as analyzing it

## ▶️ Run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
