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
from modules.generate_plots import pie_plot, bar_plot, barh_plot, nested_pie_plot

def get_demographics_plots(df, title, xlim):
    # General Demographics
    demographics_counts = df['Demographics'].value_counts().reset_index()
    demographics_counts.columns = ['Group', 'Count']
    fig_general_demographics = bar_plot(
        title=title,
        legend_title="Pessoas",
        x=demographics_counts['Group'],
        y=demographics_counts['Count'],
        xlabel='Grupos: P=Parceiro, T=Terceira Idade, D=Dependentes',
        ylabel=''
    )

    # Demographics distribution
    def get_values(query):
        return df.query(query).shape[0]
    vals = [
        [(get_values('Demographics == "PT"') + (get_values('Demographics == "PTD"') / 2)), (get_values('Demographics == "PD"') + (get_values('Demographics == "PTD"') / 2)), get_values('Demographics == "P"')],
        [get_values('Demographics == "Outros"'), (get_values('Demographics == "D"') + (get_values('Demographics == "TD"') / 2)), (get_values('Demographics == "T"') + (get_values('Demographics == "TD"') / 2))],
    ]

    outer_labels = ['Parceiro', 'Solteiros']
    inner_labels = ['T', 'D', 'Outros', 'Outros', 'D', 'T']
    try:
        fig_distribution_demographics = nested_pie_plot(title, vals=vals, inner_labels=inner_labels, outer_labels=outer_labels, subtitle="Grupos: T=Terceira Idade, D=Dependentes")
    except ValueError as e:
        print("Caught ValueError:", e)

    # Positive distribution (is X)
    binary_columns = [col for col in df.columns if set(df[col].dropna().unique()) <= {'Yes', 'No'}]
    senior_partner_dependents_columns = binary_columns[1:-2]

    positive_values = []
    for col in senior_partner_dependents_columns:
        positive = df.query(f'{col} == "Yes"').shape[0]
        positive_values.append(positive)
    positive_values.append(df.query('Demographics == "Outros"').shape[0])
    
    senior_partner_dependents_columns = ['Idosos', 'Parceiro', 'Dependentes', 'Outros']
    positive_pairs = list(zip(senior_partner_dependents_columns, positive_values))
    positive_pairs.sort(key=lambda x: x[1], reverse=False)

    positive_columns, positive_values = zip(*positive_pairs)
    fig_positive_demographics = barh_plot(title, x=positive_values, y=positive_columns, xlabel='É / Possui', ylabel='', xlim=xlim)

    # Seniority Demographics
    fig_seniority_demographics = pie_plot(
        title=title,
        labels=['Idosos', ''],
        sizes=[df.query('SeniorCitizen == "Yes"').shape[0], df.query('SeniorCitizen == "No"').shape[0]]
        )
    
    # Gender Demographics
    fig_gender_demographics = pie_plot(
        title=title,
        labels=['Homens', 'Mulheres'],
        sizes=[df.query('Gender == "Male"').shape[0], df.query('Gender == "Female"').shape[0]]
        )

    return (fig_general_demographics,
            fig_distribution_demographics, # type: ignore
            fig_positive_demographics,
            fig_seniority_demographics,
            fig_gender_demographics)