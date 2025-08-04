# Telecom X 📊📡
This project offers a complete **statistical analysis** platform about the churn in a telecomunications company, helping to visualize, compare, and download key data about demographical and business intelligence metrics of customers.

Developed with **Streamlit**, it provides an intuitive, interactive, and responsive web application, accessible on desktops, laptops, tablets, and smartphones.

## ➡️ Data Pipeline
This project features an **organized modular structure** for data processing and analysis, separating logic into clearly defined layers and modules.

### Data Flow:
- 🛒 Load and preprocess raw store data.

- 🔍 Analyze demographical and BI statistics.

- 🏛️ Build comparative global and churn statistics.

- 📈 Generate professional charts and plots.

- 📦 Provide downloadable raw JSON file.

*🎞️ Explore a comprehensive dashboard with real-time chart generation in a comprehensive pipeline!*

## 🌐 Access
🔗 [Application](https://telecom-x.streamlit.app)

🔗 [Code: For students and analysts](https://github.com/DanielCrema/oracle-one-data-science-challenge2-telecom-x)

## ✨ Features
- 📂 Load and preprocess dataset.

- 📊 Interactive data visualizations:

    - Average ticket proportions analysis.
        - Pie chart churn visualization.
        - Bar of pie chart revenue comparison.

    - Demographic distribution analysis.
        - Bar charts of groups.
        - Horizontal bar charts of groups.
        - Nested pie charts of subgroups.
        - Pie charts of specific subgroups.
        - Bar of pie chart of specific subgroups.

    - Business analytics.
        - Pie chart contract analysis.
        - Horizontal bar chart contract analysis.
        - Donut charts of service analysis.

    - Optic Fiber focused analysis.
        - Bar charts of fiber optic analysis.

- 📈 Multipage application for segmented analysis.

- 📥 Download raw data (JSON).

- 📄 Final report section with overall insights.

## 🛠️ Stack
[Python 3](https://www.python.org)

[Numpy](https://numpy.org/) – Numerical computing.

[Pandas](https://pandas.pydata.org) – Data manipulation.

[Matplotlib](https://matplotlib.org) – Chart generation.

[Seaborn](https://seaborn.pydata.org) – Enhanced statistical plotting.

[Streamlit](https://streamlit.io) – Web application framework.


## 🗂️ Project Structure
```bash
.
├── main.py             # Main Streamlit application
│
├── modules/
│   ├── generate_plots.py                   # Abstracts chart generation
│   ├── get_business_intelligence_plots.py  # Generate business charts
│   ├── get_demographics_plots.py           # Generate demographic charts
│   └── optic_fiber_analysis.py             # Optic fiber analysis
│
├── etl.py               # ETL functions
│
├── app_ui.py            # Streamlit UI HTML elements
│
└── TelecomX_Data.json   # Raw data
```

## 📑 How to Run Locally
1. Clone the repository:

```bash
git clone https://github.com/DanielCrema/oracle-one-data-science-challenge2-telecom-x.git
cd oracle-one-data-science-challenge2-telecom-x
```

2. Install the requirements:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run main.py
```

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🎓 Credits
Developed by [**Daniel Crema**](https://github.com/DanielCrema) for educational and analytical purposes as part of the Alura Challenge 2 of the **ONE - Oracle Next Education** program.

*Special thanks* to:  
🕋🤲 **Almighty God** (ﷻ), for having given me intelligence and persistence to persevere.

Then:
- [**Oracle**](https://www.oracle.com/) for sponsoring the course and curating the course materials.
- [**Alura**](https://www.alura.com.br/) for providing the course materials and support.
- [**Python community**](https://www.python.org/) for providing top-tier open-source libraries and resources.


<img src="https://raw.githubusercontent.com/devicons/devicon/ca28c779441053191ff11710fe24a9e6c23690d6/icons/oracle/oracle-original.svg" alt="logo-oracle" style="width: 70px; font-size: 10px"/>  

<img src="https://moebius78.github.io/moebius78-sprint03-aluraONE.github.io/assets/Oracle_Alura.png" alt="logo-oracle-alura-latam" style="width: 115px; background: #FCFCFC; color: #333; font-size: 10px; padding: 2px 3px"/>