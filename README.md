# 📊 System Capacity & Care Load Analytics

An end-to-end **data analytics, forecasting, and machine learning platform** built with **Python, Pandas, Scikit-learn, Plotly, and Streamlit**.

The platform analyzes historical operational data, monitors care-load trends, evaluates system capacity, forecasts future requirements, and provides machine learning insights through an interactive dashboard.

---

## 🌐 Live Demo

🚀 **[Open the Live Streamlit Application](YOUR_STREAMLIT_APP_URL)**

The interactive application provides:

- 📊 Executive Dashboard
- 📈 Operational Analytics
- 🔮 Capacity Forecasting
- 🤖 Machine Learning Insights
- 📉 Model Performance Analysis
- 🎯 Prediction Drivers
- 🧠 Business Interpretation

---

## 🚀 Project Overview

**System Capacity & Care Load Analytics** transforms historical operational data into an interactive decision-support platform.

The application combines:

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Operational analytics
- Capacity monitoring
- Time-series forecasting
- Machine learning
- Interactive data visualization
- Business-oriented decision support

The platform is designed to help users understand historical operational behavior, identify changes in system demand, monitor capacity, and support future resource planning.

---

## 🎯 Business Problem

Operational systems generate large volumes of historical data, but raw datasets do not provide an immediate view of:

- Current care-load levels
- System capacity
- Changes in operational demand
- Transfer and discharge activity
- Historical trends
- Future capacity requirements
- Important predictive drivers

This project addresses that problem by converting raw operational data into a centralized analytics platform.

The overall analytical workflow is:

**Historical Data → Data Processing → Operational Analytics → Forecasting → Machine Learning → Decision Support**

---

# 🏗️ Project Architecture

```text
                        ┌──────────────────────┐
                        │      Raw Data        │
                        │   HHS Open Data      │
                        └──────────┬───────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │   Data Processing    │
                        │ Cleaning & Validation │
                        └──────────┬───────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │ Feature Engineering  │
                        │ Lag / Rolling / KPI  │
                        └──────────┬───────────┘
                                   │
                  ┌────────────────┼────────────────┐
                  │                │                │
                  ▼                ▼                ▼
          ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
          │ Operational  │ │ Forecasting  │ │ Machine      │
          │ Analytics    │ │              │ │ Learning     │
          └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
                 │                │                │
                 └────────────────┼────────────────┘
                                  ▼
                       ┌──────────────────────┐
                       │ Streamlit Dashboard  │
                       │ Decision Intelligence│
                       └──────────────────────┘
```

---

# 📊 Dashboard

The application is organized into five major sections.

## 1. 📊 Executive Dashboard

Provides a high-level operational overview of the system.

### Key Performance Indicators

- Current HHS Care
- Current CBP Custody
- Transfers
- Discharges
- Occupancy / Capacity

### Visualizations

- Daily Children in HHS Care
- CBP Custody vs HHS Population
- Transfers vs Discharges
- Executive Summary
- Operational Recommendations
- Recent Operational Data

The dashboard provides a quick overview of current operational conditions and historical trends.

---

## 2. 📈 Operational Analytics

Provides a deeper analysis of operational activity and historical patterns.

The section focuses on relationships between:

- Children in CBP custody
- Children in HHS Care
- Children transferred out of CBP custody
- Children discharged from HHS Care

The objective is to identify operational trends, changes in demand, and relationships between key activities.

---

## 3. 🔮 Forecasting

The forecasting module provides a forward-looking view of expected system demand.

It uses historical operational patterns to generate future estimates and supports:

- Forecasted care-load levels
- Historical vs forecast comparison
- Future capacity planning
- Trend analysis
- Resource planning

Forecasting helps transform historical observations into forward-looking operational insights.

---

## 4. 🤖 Machine Learning Insights

The machine learning module uses a **Random Forest Regression** model to analyze relationships between engineered operational features and the target variable.

### Model

**Random Forest Regression**

### Evaluation Metrics

| Metric | Score |
|---|---:|
| MAE | 79.61 |
| RMSE | 101.52 |
| R² Score | 0.985 |

### Model Interpretation

The model demonstrates a strong predictive relationship on the evaluation dataset.

An **R² score of 0.985** indicates that approximately **98.5% of the variance in the target variable is explained by the model on the test dataset**.

### ML Analysis Includes

- Feature importance
- Actual vs predicted values
- Feature relationships
- Prediction drivers
- Model evaluation
- Business interpretation

---

## 5. ℹ️ About

The About section provides project documentation and information about:

- Project objectives
- Data source
- Technology stack
- Analytics workflow
- Machine learning approach
- Project architecture
- Developer information

---

# 🧮 Data & Feature Engineering

The project processes historical operational data before using it for analytics and machine learning.

The workflow includes:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Data Validation
     ↓
Exploratory Analysis
     ↓
Feature Engineering
     ↓
Analytics / Forecasting / ML
```

Feature engineering incorporates historical operational information such as:

- Lag features
- Rolling statistics
- Historical trends
- Daily changes
- Percentage changes
- Operational indicators

These features provide additional temporal context for machine learning.

---

# 🤖 Machine Learning Workflow

```text
              Feature Engineered Data
                        │
                        ▼
                Data Validation
                        │
                        ▼
                 Feature Selection
                        │
                        ▼
             Chronological Train/Test
                        │
                        ▼
             Random Forest Regression
                        │
                        ▼
                   Predictions
                        │
                        ▼
                Model Evaluation
                   ┌────┼────┐
                   ▼    ▼    ▼
                  MAE  RMSE  R²
```

A chronological train/test split is used to preserve the temporal nature of the operational dataset.

This approach evaluates the model on later observations rather than randomly mixing historical records.

---

# 📈 Model Performance

The current Random Forest model achieves the following evaluation results:

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | **79.61** |
| Root Mean Squared Error (RMSE) | **101.52** |
| R² Score | **0.985** |

### Interpretation

- **MAE = 79.61**  
  The model's average absolute prediction error is approximately 79.61 units.

- **RMSE = 101.52**  
  The RMSE indicates the magnitude of prediction errors while giving greater weight to larger errors.

- **R² = 0.985**  
  The model explains approximately 98.5% of the variance in the target variable on the evaluation dataset.

> Model performance should be interpreted in the context of the historical dataset and evaluation methodology.

---

# 🛠️ Technology Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- Random Forest Regression
- Joblib

### Visualization

- Plotly
- Streamlit

### Dashboard

- Streamlit
- Custom CSS
- Modular Python components

---

# 📁 Project Structure

```text
system-capacity-care-load-analytics/
│
├── dashboard/
│   │
│   ├── app.py
│   ├── utils.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── cards.py
│   │   ├── charts.py
│   │   ├── layout.py
│   │   ├── sidebar.py
│   │   └── styles.py
│   │
│   └── pages/
│       ├── 1_Executive_Dashboard.py
│       ├── 2_Operational_Analytics.py
│       ├── 3_Forecasting.py
│       ├── 4_ML_Insights.py
│       └── 5_About.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── feature_engineered/
│
├── models/
│
├── notebooks/
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <https://github.com/swimmysahaniya/system-capacity-care-load-analytics>
```

Navigate to the project:

```bash
cd system-capacity-care-load-analytics
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

From the project root:

```bash
streamlit run dashboard/app.py
```

The Streamlit application will open in your browser.

---

# 📊 Application Navigation

The dashboard contains:

```text
📊 Executive Dashboard
        │
        ▼
📈 Operational Analytics
        │
        ▼
🔮 Forecasting
        │
        ▼
🤖 ML Insights
        │
        ▼
ℹ️ About
```

All sections are accessible through the application's navigation menu.

---

# 💡 Business Value

The platform provides several potential operational benefits.

### Capacity Monitoring

Monitor current care-load levels and compare them against historical capacity patterns.

### Operational Monitoring

Track:

- CBP custody
- HHS care
- Transfers
- Discharges

### Forecasting

Use historical trends to support future capacity planning.

### Machine Learning

Identify important predictive features and analyze relationships within operational data.

### Decision Support

Bring descriptive analytics, forecasting, and machine learning into a single dashboard.

---

# 🔍 Key Analytical Workflow

The project demonstrates an end-to-end analytics workflow:

```text
        Raw Data
           │
           ▼
    Data Cleaning
           │
           ▼
   Exploratory Analysis
           │
           ▼
 Feature Engineering
           │
           ├───────────────┐
           ▼               ▼
   Operational        Forecasting
    Analytics             │
           │              │
           └───────┬──────┘
                   ▼
          Machine Learning
                   │
                   ▼
          Business Insights
                   │
                   ▼
        Streamlit Dashboard
```

---

# ⚠️ Limitations

This project is intended as an **analytical and decision-support platform**.

Forecasts and machine learning predictions should be interpreted alongside operational context.

Model performance may change when future observations differ significantly from the historical patterns represented in the training data.

The current evaluation results should therefore not be interpreted as a guarantee of future predictive performance.

---

# 🔮 Future Enhancements

Potential future improvements include:

- Automated data ingestion
- Automated model retraining
- Advanced time-series forecasting
- XGBoost / LightGBM model comparison
- SHAP-based model explainability
- Automated anomaly detection
- Model performance monitoring
- Forecast monitoring
- Automated reporting
- Cloud deployment
- Real-time data pipelines
- Role-based access control

---

# 👨‍💻 Developer

**Swimmy Sahaniya**

Machine Learning / Full Stack Developer

### Areas of Interest

- Machine Learning
- Data Analytics
- Predictive Modeling
- Python
- Data Visualization
- Streamlit
- Full Stack Development

---

# 📌 Project Status

| Item | Status |
|---|---|
| Data Processing | ✅ Completed |
| Exploratory Analytics | ✅ Completed |
| Operational Dashboard | ✅ Completed |
| Forecasting | ✅ Completed |
| Machine Learning | ✅ Completed |
| Interactive Dashboard | ✅ Completed |
| Documentation | ✅ Completed |
| Version | **1.0.0** |

---

## 🎥 Project Walkthrough

A complete walkthrough of the **System Capacity & Care Load Analytics** platform.

▶️ **[Watch the Full Project Demo](YOUR_VIDEO_URL_HERE)**

The walkthrough covers the complete analytics pipeline:

**Data Processing → Feature Engineering → Operational Analytics → Forecasting → Machine Learning → Decision Support**

---

## 📄 License

This project is intended for **educational, analytical, and portfolio purposes**.