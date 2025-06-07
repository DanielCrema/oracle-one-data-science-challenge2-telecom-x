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
import streamlit as st
from etl import etl
from app_ui import streamlit_header, sidebar_credits

global_demographics, churn_demographics, bi_statistics, fiber_statistics = etl()

# Initializing Streamlit app
# 
# Set page config
st.set_page_config(
    page_title="Telecom X",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# # Create header section
st.markdown(streamlit_header, unsafe_allow_html=True)

# Define page functions
@st.cache_data
def home():
    st.write("Os índices de evasão na Telecom X se tornaram preocupantes e precisam ser analisados.")

    st.subheader("O problema:", divider=True, anchor='problem')
    st.pyplot(bi_statistics[0])
    st.write("A empresa está perdendo clientes e precisa tomar medidas para reduzir a evasão.")
    st.subheader("Perda em faturamento", divider=True, anchor='revenue_loss')
    st.pyplot(bi_statistics[1])
    st.subheader("Insights:")
    st.write("O faturamento perdido é proporcionalmente menor entre os evadidos. Uma boa notícia que pode fornecer insights interessantes sobre o problema.")

    # Create sidebar summary section
    st.sidebar.markdown("""
    ### 📑 Sumário

    - [O problema](#problem)
    - [Analisando o faturamento](#revenue_loss)
    <hr/>
    """, unsafe_allow_html=True)

@st.cache_data
def demographic_analysis():
    st.write("Fizemos um levantamento demográfico comparativo analisando os dados da clientela geral da Telecom X, incluindo os evadidos, e a clientela que efetivamente evadiu.")
    st.write("A análise demográfica é uma parte essencial da análise de dados, pois ajuda a entender a composição da clientela e a identificar possíveis tendências ou padrões.")

    st.subheader("Distribuição demográfica geral", divider=True, anchor='general_demographics')
    # Columns layout setup
    col1, col2 = st.columns(2)
    col1.write("Dados demográficos gerais")
    col2.write("Dados demográficos de evadidos")
    col1.pyplot(global_demographics[0])
    col2.pyplot(churn_demographics[0])
    col1.pyplot(global_demographics[2])
    col2.pyplot(churn_demographics[2])
    col1.pyplot(global_demographics[1])
    col2.pyplot(churn_demographics[1])
    st.subheader("Insights:")
    st.write("""- Ressalta-se na análise a prevalência de clientes solteiros sem filhos entre os evadidos, provavelmente gente jovem, que está em busca de uma vida mais independente.""")
    st.write("""- Também se nota um maior volume de pessoas na terceira idade entre os evadidos.""")                
    st.write("""- Entre os que possuem parceiro e/ou filhos a correlação é negativa, ou seja, o índice de evasões neste grupo e proporcionalmente menor, com exceção dos idosos.""")
    st.subheader("Especificidades", divider=True, anchor='specific_demographics')
    col1, col2 = st.columns(2)
    col1.write("Dados demográficos gerais")
    col2.write("Dados demográficos de evadidos")
    st.pyplot(bi_statistics[2])
    col1.pyplot(global_demographics[3])
    col2.pyplot(churn_demographics[3])
    col1.pyplot(global_demographics[4])
    col2.pyplot(churn_demographics[4])
    st.subheader("Insights:")
    st.write("""- A análise coloca em evidência a evasão de pessoas casadas/amaziadas e idosos, enquanto que a correlação entre sexo e evasão é virtualmente nula.""")
    st.subheader("Conclusão", divider=True, anchor='conclusion')
    st.write("""
    ➡️ A análise de dados revelou que a maioria dos evadidos são solteiros sem filhos, representando 44.9% do total de evadidos. Dos 2800 clientes desta categoria, 862 evadiram. 
                                 
    Uma hipótese para justificar esta evasão pode ser o fato de esses jovens estarem começando a vida e terem menos dinheiro para se sustentarem, o que agravado pela crise econômica pode levar à necessidade de cortar custos e buscar alternativas mais baratas. Validar as hipóteses é importante para uma tomada de decisão mais informada, o que será mais explorado na próxima seção.""")
    st.write("""
    ➡️ A análise também demonstrou que em termos proporcionais a maioria dos evadidos são idosos. Embora representem 24.9% dos evadidos. Dos 1182 clientes desta categoria, 490 evadiram, o que significa perder quase a metade da clientela neste público.
             
    Levantar hipóteses para este público sem dados de negócio seria nebuloso, de forma que será mais prudente explorar o tema na próxima seção.""")

    st.sidebar.markdown("""
    ### 📑 Sumário

    - [Distribuição demográfica geral](#general_demographics)
    - [Especificidades](#specific_demographics)
    - [Conclusão](#conclusion)
    <hr/>
    """, unsafe_allow_html=True)

@st.cache_data
def bi_analysis():
    st.write("A análise de dados de negócio é uma parte essencial da análise de dados, pois ajuda a entender o comportamento de consumo da clientela e a identificar possíveis tendências ou padrões.")
    st.write("Fizemos uma análise de negócio comparativa analisando os dados da clientela geral da Telecom X, incluindo os evadidos, e a clientela que efetivamente evadiu.")

    st.subheader("Análise de negócio geral", divider=True, anchor='general_bi')
    col1, col2 = st.columns(2)
    col1.write("Dados de negócio gerais")
    col2.write("Dados de negócio de evadidos")
    col1.pyplot(bi_statistics[7])
    col2.pyplot(bi_statistics[8])
    col1.pyplot(bi_statistics[9])
    col2.pyplot(bi_statistics[10])
    st.subheader("Insights:")
    st.write("""- Ressalta-se na análise a prevalência de contratos mensais entre os clientes evadidos, especialmente clientes cujo tempo de contrato foi em torno de 6 meses. 87.9% das evasões ocorreram nesta categoria, o que é uma proporção considerável.""")
    st.write("""- Essas observações corroboram a hipótese de que a crise econômica pode estar influenciando a decisão de evasão dos clientes jovens, porém é também um alarmante indício de que algo pode estar errado com a experiência do cliente em relação aos serviços oferecidos e/ou preços estabelecidos.""")


    st.subheader("Serviços mais utilizados", divider=True, anchor='most_used_services')
    col1, col2 = st.columns(2)
    col1.write("Dados de negócio gerais")
    col2.write("Dados de negócio de evadidos")
    col1.pyplot(bi_statistics[3])
    col2.pyplot(bi_statistics[4])
    col1.pyplot(bi_statistics[5])
    col2.pyplot(bi_statistics[6])
    st.subheader("Insights:")
    st.write("""- Ressalta-se na análise a prevalência de clientes que utilizam o serviço de internet por fibra ótica, representando 68.7% dos evadidos. Um indicador considerável.""")
    st.write("- A correlação entre evasão e consumo de serviços de telefone é virtualmente nula.")

    st.subheader("Conclusão", divider=True, anchor='conclusion')
    st.write("""
    ➡️ Entre os clientes evadidos prevelece a incidência de contratos mensais tendo como serviço principal o fornecimento de internet por fibra ótica, isso pode ser um indício de que:""")
    st.write("a) A experiência do cliente com o serviço de internet por fibra ótica pode ser ruim, o que pode ser um indício de que a qualidade do serviço não está satisfazendo as expectativas dos clientes, o que explicaria o alto índice de idosos entre os evadidos.")
    st.write("b) A concorrência está oferecendo preços mais baratos para um serviço similar ao nosso, o que explicaria a evasão de clientes com contrato mensal, jovens e portanto com baixo nível de fidelização.")
    st.write("Na proxima seção será explorado o tema de forma mais aprofundada, analisando a distribuição demográfica da clientela que consome o serviço de internet por fibra ótica.")

    st.sidebar.markdown("""
    ### 📑 Sumário

    - [Análise de negócio geral](#general_bi)
    - [Serviços mais utilizados](#most_used_services)
    - [Conclusão](#conclusion)
    <hr/>
    """, unsafe_allow_html=True)

@st.cache_data
def fiber_analysis():
    st.write("Nosso levantamento até o momento nos levou à constatação de que a maioria dos evadidos são idosos e jovens sem filhos, o que nos levou a investigar a distribuição demográfica dessas categorias de clientes. O estudo também nos levou a constatar que a maioria dos evadidos são clientes que consomem o serviço de internet por fibra ótica em contratos mensais.")
    st.write("Nesta seção, exploraremos a distribuição demográfica dos clientes que consomem o serviço de internet por fibra ótica.")

    st.subheader("Recapitulando", divider=True, anchor='general_demographics')
    st.pyplot(fiber_statistics[0])

    st.subheader("Distribuição demográfica", divider=True, anchor='demographic_distribution')
    col1, col2 = st.columns(2)
    col1.write("Distribuição demográfica geral")
    col2.write("Distribuição demográfica dos evadidos")
    col1.pyplot(fiber_statistics[1])
    col2.pyplot(fiber_statistics[2])
    st.subheader("Insights:", anchor='demographic_insights')
    st.write("Os gráficos enfatizam um aumento expressivo de clientes jovens sem filhos e idosos entre os consumidores de internet por fibra ótica, reforçando as observações feitas anteriormente.")
    st.write("Na próxima seção serão apresentados de forma sumarizada os insights obtidos até o momento.")

    st.sidebar.markdown("""
    ### 📑 Sumário

    - [Recapitulando](#general_demographics)
    - [Distribuição demográfica](#demographic_distribution)
    - [Insights](#demographic_insights)
    <hr/>
    """, unsafe_allow_html=True)

def final_report():
    st.subheader("Relatório Final", divider=True, anchor='final_report')
    st.write("""
    ➡️ Este levantamento se debruçou sobre o problema partindo de uma abordagem demográfica a uma abordagem de negócios, visando compreender melhor as características do público egresso e seus comportamentos de consumo, de forma a figurar hipóteses para a causa da evasão.""")
    st.write("- Nas análises preliminares, constatamos que o impacto em faturamento, embora considerável, é proporcionalmente menor do que o impacto em número de clientes, o que aponta para a hipótese de que os clientes egressos pessoas de baixa renda.""")
    st.write("- No estudo demográfico, identificamos claramente que os clientes egressos são predominantemente jovens sem filhos e idosos.""")
    st.write("- A análise de negócios revelou que a maioria dos clientes egressos consomem o serviço de internet por fibra ótica em contratos mensais.")
    st.write("- O estudo sobre os consumidores de fibra ótica enfatizou que a maioria dos clientes egressos deste grupo são jovens sem filhos e idosos, reforçando as observações feitas anteriormente.")

    st.subheader("Considerações Finais", divider="green", anchor='final_considerations')
    st.write("➡️ Tendo em vista o cenário de evasão atual onde jovens sem filhos e idosos consumidores de serviço de fibra ótica em contratos mensais predominam entre os egressos, sugerimos as seguintes ações para mitigar a evasão:")
    st.write("- **Melhorar a experiência do cliente**: Investir em melhorias na qualidade do serviço de internet por fibra ótica, garantindo uma experiência de usuário mais satisfatória.")
    st.write("- **Oferecer planos mais acessíveis**: Oferecer planos de internet mais acessíveis para jovens sem filhos e idosos, incentivando a fidelização.")
    st.write("- **Personalização de ofertas**: Implementar estratégias de personalização de ofertas, oferecendo pacotes de serviços que atendam às necessidades específicas dos clientes.")
    st.write("- **Comunicação efetiva**: Implementar uma comunicação efetiva com os clientes egressos, incentivando a renovação de contratos e a fidelização.")

    # Download data section
    # 
    st.markdown("""<a name="download-data"></a><h1 style="font-size: 1.5rem; letter-spacing: 0.04rem; margin-top: 1.5rem">⬇️ Download dos Dados</h1>""", unsafe_allow_html=True)
    st.write("Baixe os **dados brutos** utilizados neste projeto para realizar análises adicionais.  ")
    # Read the JSON file from the root directory
    with open("TelecomX_Data.json", "rb") as f:
        json_data = f.read()
    # Create a download button
    st.download_button(
        label="📥 Download TelecomX_Data.json",
        data=json_data,
        file_name="TelecomX_Data.json",
        mime="application/json"
    )

    st.sidebar.markdown("""
    ### 📑 Sumário

    - [Relatório Final](#final_report)
    - [Considerações Finais](#final_considerations)
    - [Download dos Dados](#download-data)
    <hr/>
    """, unsafe_allow_html=True)


# Page dictionary
pages = {
    "Análises Preliminares": home,
    "Estudo Demográfico": demographic_analysis,
    "Análise de Negócio": bi_analysis,
    "Fibra ótica: Estudo": fiber_analysis,
    "Relatório Final": final_report,
}

# Configure sidebar
# 
# Sidebar navigation
st.sidebar.title("🧭 Navegação")
selection = st.sidebar.radio("Ir para:", list(pages.keys()))
# Run the selected page
pages[selection]()

# Create credits section
st.sidebar.markdown("""### 🎓 Créditos""")
st.sidebar.markdown(sidebar_credits, unsafe_allow_html=True)