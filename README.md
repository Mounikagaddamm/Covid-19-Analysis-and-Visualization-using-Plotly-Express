

## 🦠 COVID-19 Data Analysis & Visualization with Plotly Express

Interactive and insightful visual exploration of global COVID-19 trends using **Plotly Express**, **Pandas**, and **Choropleth Maps**. This project uncovers key pandemic patterns across countries and continents using compelling visual storytelling.

## 🔍 Overview

This project visualizes COVID-19 case trends, mortality rates, testing data, and recovery statistics. It includes animated bar charts, bubble charts, and world maps to demonstrate the evolution of the pandemic across time and geography.


## 🚀 Features

✅ Clean and preprocess COVID-19 datasets
✅ Country and continent-level comparisons
✅ Animated charts showing progression over time
✅ Interactive choropleth maps
✅ Data-driven insights into global testing and fatality rates


## 🧰 Tech Stack

* **Languages**: Python
* **Libraries**: Plotly Express, Pandas, Matplotlib
* **Platform**: Google Colab
* **Visualization**: Bar Charts, Bubble Charts, Choropleth Maps

## 📊 Datasets

* **covid.csv** – Summary data by country (cases, deaths, tests, etc.)
* **covid\_grouped.csv** – Time-series data grouped by country and date

## 📌 Visualizations Included

| Type               | Description                                           |
| ------------------ | ----------------------------------------------------- |
| 📈 Bar Charts      | Top countries by cases, deaths, recoveries, and tests |
| 🫧 Bubble Charts   | Continent-wise case/test spread and impact            |
| 🌍 Choropleth Maps | Animated world maps (confirmed, deaths, recoveries)   |
| 📅 Time Series     | Country-wise daily growth (e.g., U.S.)                |
| ☁️ Word Cloud      | (Optional - for future enhancement)                   |


## 🧼 Data Preprocessing

* Dropped unused columns: `NewCases`, `NewDeaths`, `NewRecovered`
* Handled missing and redundant values
* Aggregated and grouped data by date and region

## 🛠️ How to Use

1. Clone the repository

   git clone https://github.com/yourusername/covid19-plotly-visualization.git
  
2. Install dependencies

pip install pandas plotly matplotlib
   
4. Run the notebook in **Google Colab** or locally.
5. Ensure dataset paths match your environment.


## 📈 Sample Output

* 📊 Top 15 countries with most cases
* 📉 Comparative analysis of Total Cases vs Total Deaths
* 🌐 Animated world map of case spread (by date)


## 🔮 Future Enhancements

* Real-time data updates via APIs
* Dashboard with **Dash** or **Streamlit**
* Predictive modeling and trend forecasting



