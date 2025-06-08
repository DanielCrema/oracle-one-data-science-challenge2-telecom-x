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
from modules.generate_plots import donut_plot, bar_plot

def optic_fiber_analysis(data, data_churn):
    # Churn internet service (emphasis on fiber optic)
    data_churn_internet_service = data_churn['InternetService'].value_counts().reset_index()
    pie_sizes = [ # index  0 = Fibra Ótica, index 1 = DSL + Sem Internet (outros)
        data_churn_internet_service.loc[data_churn_internet_service['InternetService'] == 'DSL']['count'].values[0] + data_churn_internet_service.loc[data_churn_internet_service['InternetService'] == 'No']['count'].values[0],
        data_churn_internet_service.loc[data_churn_internet_service['InternetService'] == 'Fibra Ótica']['count'].values[0]
    ]
    fig_churn_by_fiber = donut_plot(
        title="Distribuição da Evasão",
        sizes=pie_sizes,
        labels=['Outros', 'Fibra Ótica'],
    )

    # Fiber global demographics
    data_fiber = data.query('InternetService == "Fibra Ótica"')
    fiber_demographics_counts = data_fiber['Demographics'].value_counts().reset_index()
    fiber_demographics_counts.columns = ['Group', 'Count']
    fig_global_distribution_by_fiber = bar_plot(
        title="Distribuição de Usuários - Fibra Ótica\n(Global)",
        x=fiber_demographics_counts['Group'],
        y=fiber_demographics_counts['Count'],
        xlabel="Grupos: P=Parceiro, T=Terceira Idade, D=Dependentes",
        ylabel="",
        legend=False
    )

    # Fiber churn demographics
    data_churn_fiber = data_churn.query('InternetService == "Fibra Ótica"')
    fiber_churn_demographics_counts = data_churn_fiber['Demographics'].value_counts().reset_index()
    fiber_churn_demographics_counts.columns = ['Group', 'Count']
    fig_churn_distribution_by_fiber = bar_plot(
        title="Distribuição de usuários de Fibra\n(Evasão)",
        legend_title="Grupo",
        x=fiber_churn_demographics_counts['Group'],
        y=fiber_churn_demographics_counts['Count'],
        xlabel="Grupos: P=Parceiro, T=Terceira Idade, D=Dependentes",
        ylabel="",
    )

    return (fig_churn_by_fiber, fig_global_distribution_by_fiber, fig_churn_distribution_by_fiber)