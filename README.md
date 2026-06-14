# 🍽 Budget Food Finder

A Python-based web scraping and recommendation system that helps users find food items based on **budget, category, and keyword search**. Built using BeautifulSoup and enhanced with a Streamlit dashboard for interactive visualization.

---

## 🚀 Project Overview

Budget Food Finder extracts menu data from a restaurant website, cleans and structures it, and provides smart recommendations based on user input such as food name and budget. It also includes data visualization and an interactive UI.

---

## ✨ Features

- 🌐 Web scraping using BeautifulSoup
- 📊 Data extraction from restaurant menus
- 🧹 Data cleaning and preprocessing
- 💰 Budget-based filtering system
- 🔍 Keyword-based food search
- 📂 Category grouping (Bowls, Salads, Drinks, etc.)
- 📊 Data visualization using Matplotlib
- 🖥 Streamlit interactive dashboard
- ⭐ Top recommendation highlight system

---

## 🛠️ Technologies Used

- Python
- BeautifulSoup
- Requests
- Pandas
- Matplotlib
- Streamlit
- Git & GitHub

---

## 📁 Project Structure
Budget-Food-Finder/
│
├── scraper.py # Web scraping script
├── cleaner.py # Data cleaning & preprocessing
├── recommender.py # Recommendation engine
├── visualizer.py # Charts and analysis
├── app.py # Streamlit web app
│
├── data/
│ ├── raw_data.csv
│ └── cleaned_data.csv
│
├── charts/
│ ├── category_distribution.png
│ └── top_expensive_items.png
│
├── requirements.txt
└── README.md


---

## 🖥️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Run scraper
python scraper.py
3️⃣ Clean data
python cleaner.py
4️⃣ Run recommender (CLI version)
python recommender.py
5️⃣ Run Streamlit App
python -m streamlit run app.py

📊 Example Usage

Input:
Food: chicken
Budget: 300
Output:
Classic Chicken Caesar
Chicken Pesto Parm
BBQ Chicken Salad

📈 Visualizations

Category distribution of menu items
Average price by category
Top expensive items analysis

🎯 Key Learning Outcomes

Web scraping with BeautifulSoup
Data cleaning and preprocessing
Building recommendation logic
Working with CSV datasets
Creating interactive dashboards using Streamlit
Structuring a full Python project

🚀 Future Enhancements

Multi-restaurant scraping system
Price trend analysis
AI-based recommendation ranking
Deployment on Streamlit Cloud
User login system

## 🎓 Internship Details

- Internship ID: CITS1184  
- Domain: Python Development / Web Scraping  
- Project Type: Budget Food Finder (Web Scraper (BeautifulSoup))

👨‍💻 Author

Revuri Navyasree



