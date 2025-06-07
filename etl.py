# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# #
# Imports
import random
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from modules.get_demographics_plots import get_demographics_plots as demographics
from modules.get_business_intelligence_plots import get_business_intelligence_plots as business_intelligence
from modules.optic_fiber_analysis import optic_fiber_analysis as optic_fiber

@st.cache_data
def etl():
    # #
    # Extract
    data = pd.read_json('TelecomX_Data.json')
    data = pd.json_normalize(data.to_dict('records'))
    data.columns = [col.split('.')[-1] if '.' in col else col for col in data.columns]
    data.columns = [col[0].upper() + col[1:] for col in data.columns]

    # #
    # Transform
    
    # Normalize SeniorCitizen status
    data['SeniorCitizen'] = ['Yes' if x == 1 else 'No' for x in data['SeniorCitizen']]

    # Normalize Total and convert to Float
    data['Total'] = data['Total'].replace(r'^\s*$', 0, regex=True)
    data['Total'] = data['Total'].astype(float)

    # Normalize Churn status
    missing_indices = data[data['Churn'] == ''].index # Find indices with missing values
    known_churn = data[data['Churn'].isin(['Yes', 'No'])]
    yes_ratio = len(known_churn[known_churn['Churn'] == 'Yes']) / len(known_churn) # Find the  ratio of "Yes" to "No"
    churn_interpolation = ['Yes' if x < len(missing_indices) * yes_ratio else 'No' for x in range(len(missing_indices))] # Interpolate missing values
    churn_interpolation = random.sample(churn_interpolation, len(churn_interpolation)) # Randomize the order of the values
    data.loc[missing_indices, 'Churn'] = churn_interpolation

    # Create daily statistics
    data['Daily'] = data['Monthly'] / 30

    # Create demographic information column
    data['Demographics'] = (
        data['Partner'].astype(str).map({'Yes': 'P', 'No': ''}) +
        data['SeniorCitizen'].astype(str).map({'Yes': 'T', 'No': ''}) +
        data['Dependents'].astype(str).map({'Yes': 'D', 'No': ''})
    )
    data['Demographics'] = data['Demographics'].replace('', 'Outros')

    # Normalize InternetService and Contract columns to portuguese
    data['InternetService'] = data['InternetService'].replace('Fiber optic', 'Fibra Ótica')
    data['Contract'] = data['Contract'].replace('Month-to-month', 'Mensal')
    data['Contract'] = data['Contract'].replace('One year', 'Anual')
    data['Contract'] = data['Contract'].replace('Two year', 'Bianual')


    # Transform columns to categorical
    data[['Churn', 'Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']] = data[['Churn', 'Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']].astype('category')

    # #
    # Load

    # Isolate churn for analysis
    data_churn = data.query('Churn == "Yes"')

    # Generate Plots
    global_demographics = demographics(
        data,
        title="Dados Demográficos\n(Global)",
        xlim=(800, data.shape[0])
        )
    plt.close('all')

    churn_demographics = demographics(
        data_churn,
        title="Dados Demográficos\n(Evasões)",
        xlim=(200, data_churn.shape[0])
        )
    plt.close('all')

    bi_statistics = business_intelligence(data, data_churn)
    plt.close('all')

    fiber_statistics = optic_fiber(data, data_churn)

    return global_demographics, churn_demographics, bi_statistics, fiber_statistics

# # Unpacking
# # 
# fig_global_general_demographics = global_demographics[0]
# fig_global_distribution_demographics = global_demographics[1]
# fig_global_positive_demographics = global_demographics[2]
# fig_global_seniority_demographics = global_demographics[3]
# fig_global_gender_demographics = global_demographics[4]

# fig_churn_general_demographics = churn_demographics[0]
# fig_churn_distribution_demographics = churn_demographics[1]
# fig_churn_positive_demographics = churn_demographics[2]
# fig_churn_seniority_demographics = churn_demographics[3]
# fig_churn_gender_demographics = churn_demographics[4]

# fig_churn_distribution = bi_statistics[0]
# fig_churn_distribution_by_revenue = bi_statistics[1]
# fig_churn_distribution_by_partner = bi_statistics[2]
# fig_global_internet_services = bi_statistics[3]
# fig_churn_internet_services = bi_statistics[4]
# fig_global_phone_services = bi_statistics[5]
# fig_churn_phone_services = bi_statistics[6]
# fig_global_contract_stats = bi_statistics[7]
# fig_churn_contract_stats = bi_statistics[8]
# fig_global_tenure_stats = bi_statistics[9]
# fig_churn_tenure_stats = bi_statistics[10]


# Display
# 

# # Distributions
# fig_churn_distribution
# fig_churn_distribution_by_revenue
# fig_churn_distribution_by_partner

# # Global stats
# # 
# # Demography
# fig_global_general_demographics
# fig_global_distribution_demographics
# fig_global_positive_demographics
# fig_global_seniority_demographics
# fig_global_gender_demographics

# # Business Intelligence
# fig_global_internet_services
# fig_global_phone_services
# fig_global_contract_stats
# fig_global_tenure_stats

# # Churn stats
# # 
# # Demography
# fig_churn_general_demographics
# fig_churn_distribution_demographics
# fig_churn_positive_demographics
# fig_churn_seniority_demographics
# fig_churn_gender_demographics

# # Business Intelligence
# fig_churn_internet_services
# fig_churn_phone_services
# fig_churn_contract_stats
# fig_churn_tenure_stats