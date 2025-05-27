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
import pandas as pd


# #
# Extract
data = pd.read_json('TelecomX_Data.json')
data = pd.json_normalize(data.to_dict('records'))
data.columns = [col.split('.')[-1] if '.' in col else col for col in data.columns]
data.columns = [col[0].upper() + col[1:] for col in data.columns]

# #
# Transform
data.head()
data.info()
data.describe()
columns = list(data.columns)
for column in columns:
    print(f'\n\n=> Column "{column}":')
    print(f'// Unique\n{data[column].unique()}\n')
    print(f'// Value Counts\n{data[column].value_counts()}\n')
    print(f'// Description\n{data[column].describe()}')

# Transform columns to categorical
data[['Churn', 'Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']] = data[['Churn', 'Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']].astype('category')

# Normalize SeniorCitizen status
data['SeniorCitizen'] = ['Yes' if x == 1 else 'No' for x in data['SeniorCitizen']]

# Normalize Churn status
missing_indices = data[data['Churn'] == ''].index # Find indices with missing values
alternating_values = ['Yes' if x % 2 == 1 else 'No' for x in range(len(missing_indices))]
data.loc[missing_indices, 'Churn'] = alternating_values

# #
# Load