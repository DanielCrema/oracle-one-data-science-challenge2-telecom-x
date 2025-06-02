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
from generate_plots import donut_plot, pie_plot, bar_of_pie_plot

def get_business_intelligence_plots(data, data_churn):
    churn_counts = data['Churn'].value_counts().reset_index()
    churn_counts.columns = ['Churn', 'Count']
    fig_churn_distribution = donut_plot('Distribuição da Evasão', labels=['', 'Evasão'], sizes=churn_counts['Count'])

    # Revenue loss by churn
    churn_revenue = [(data['Total'].sum() - data_churn['Total'].sum()),  data_churn['Total'].sum()]
    fig_churn_distribution_by_revenue = bar_of_pie_plot(
        title_pie='Distribuição da Evasão',
        title_bar='Faturamento',
        pie_sizes=churn_counts['Count'],
        pie_labels=['', 'Evasão'],
        bar_sizes=churn_revenue,
        bar_labels=['', 'Evasão'],
        double_color_bar=True
    )

    # Churn by partner
    churn_partner = data_churn['Partner'].value_counts().reset_index()
    churn_partner.columns = ['Partner', 'Count']
    fig_churn_distribution_by_partner = bar_of_pie_plot(
        title_pie='Distribuição da Evasão',
        title_bar='Evasão: Parceiro',
        pie_sizes=churn_counts['Count'],
        pie_labels=['', 'Evasão'],
        bar_sizes=churn_partner['Count'],
        bar_labels=['Não Possui', 'Possui'],
    )

    # Contract types
    contract_types = list(data['Contract'].unique())
    global_contract_counts = []
    churn_contract_counts = []
    for type in contract_types:
        global_contract_counts.append(data.query('Contract == @type').shape[0])
        churn_contract_counts.append(data_churn.query('Contract == @type').shape[0])
        
    fig_global_contract_stats = pie_plot(
        title='Distribuição de Contratos\n(Global)',
        labels=contract_types,
        sizes=global_contract_counts,
    )

    fig_churn_contract_stats = pie_plot(
        title='Distribuição de Contratos\n(Evasões)',
        labels=contract_types,
        sizes=churn_contract_counts,
    )

    # Internet services
    internet_services = list(data['InternetService'].unique())
    global_internet_counts = []
    churn_internet_counts = []
    for type in internet_services:
        global_internet_counts.append(data.query('InternetService == @type').shape[0])
        churn_internet_counts.append(data_churn.query('InternetService == @type').shape[0])

    internet_services = [type.replace('No', 'Não Possui') for type in internet_services]
    fig_global_internet_services = donut_plot(
        title='Distribuição de Serviços de Internet\n(Global)',
        labels=internet_services,
        sizes=global_internet_counts,
    )

    fig_churn_internet_services = donut_plot(
        title='Distribuição de Serviços de Internet\n(Evasão)',
        labels=internet_services,
        sizes=churn_internet_counts,
    )

    # Phone services
    fig_global_phone_services = donut_plot(
        title='Distribuição de Serviços de Telefone\n(Global)',
        labels=['Possui', 'Não Possui'],
        sizes=[data.query('PhoneService == "Yes"').shape[0], data.query('PhoneService == "No"').shape[0]],
    )

    fig_churn_phone_services = donut_plot(
        title='Distribuição de Serviços de Telefone\n(Evasão)',
        labels=['Possui', 'Não Possui'],
        sizes=[data_churn.query('PhoneService == "Yes"').shape[0], data_churn.query('PhoneService == "No"').shape[0]],
    )

    return (fig_churn_distribution,
            fig_churn_distribution_by_revenue,
            fig_churn_distribution_by_partner,
            fig_global_contract_stats,
            fig_churn_contract_stats,
            fig_global_internet_services,
            fig_churn_internet_services,
            fig_global_phone_services,
            fig_churn_phone_services)