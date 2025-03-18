import streamlit as st
import time

# Configuração da página
st.set_page_config(
    page_title='Quiz de Doação de Sangue',
    layout='centered',
    page_icon="🩸"
)

# Estilos personalizados
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #ff1a1a;
    }
    .stRadio div {
        background-color: #2e2e2e;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        color: #ffffff;
    }
    .stMarkdown h2 {
        color: #ff4b4b;
    }
    .stMarkdown h3 {
        color: #ffffff;
    }
    .stMarkdown p {
        color: #ffffff;
    }
    .stWarning {
        background-color: #ff4b4b;
        color: #ffffff;
    }
    .stSuccess {
        background-color: #4caf50;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# Função principal
st.title('Quiz sobre Doação de Sangue 🩸')
st.markdown("**Descubra se você está apto para doar sangue!**")

# Inicializando a variável que indica a aptidão para doar sangue
if 'aptidoes' not in st.session_state:
    st.session_state.aptidoes = True

# Inicializando o estado da pergunta atual
if 'current_question' not in st.session_state:
    st.session_state.current_question = 1

# Função para avançar para a próxima pergunta
def next_question():
    # Simulando uma breve transição para a próxima pergunta
    time.sleep(0.3)
    st.session_state.current_question += 1
    st.experimental_rerun()

# Pergunta 1: Idade
if st.session_state.current_question == 1:
    st.subheader('Primeiros critérios')
    st.write('**Qual a sua idade?**')
    idade = st.radio('', options=['Menos de 18 anos', '18 a 70 anos', '71 anos ou mais'], key='idade')
    
    if st.button('Próxima Pergunta ➡️', key='button1'):
        if idade == 'Menos de 18 anos':
            st.warning('Infelizmente, você não pode doar sangue. O limite mínimo é 18 anos.')
            st.session_state.aptidoes = False
            st.session_state.current_question = 5  # Pula para a conclusão
        elif idade == '71 anos ou mais':
            st.warning('Infelizmente, você não pode doar sangue. O limite máximo é 70 anos.')
            st.session_state.aptidoes = False
            st.session_state.current_question = 5  # Pula para a conclusão
        else:
            next_question()

# Pergunta 2: Peso
if st.session_state.current_question == 2:
    st.subheader('Critérios adicionais')
    st.write('**Você pesa mais de 50 kg?**')
    peso = st.radio('', options=['Sim', 'Não'], key='peso')
    
    if st.button('Próxima Pergunta ➡️', key='button2'):
        if peso == 'Não':
            st.warning('Infelizmente, você não pode doar sangue. O peso mínimo exigido é 50 kg.')
            st.session_state.aptidoes = False
            st.session_state.current_question = 5  # Pula para a conclusão
        else:
            next_question()

# Pergunta 3: Frequência de doação
if st.session_state.current_question == 3:
    st.subheader('Critérios adicionais')
    st.write('**Você já doou sangue nos últimos 3 meses (homem) ou nos últimos 4 meses (mulher)?**')
    doacao_recente = st.radio('', options=['Sim', 'Não'], key='doacao_recente')
    
    if st.button('Próxima Pergunta ➡️', key='button3'):
        if doacao_recente == 'Sim':
            st.warning('Você deve esperar o período necessário antes de doar novamente.')
            st.session_state.aptidoes = False
            st.session_state.current_question = 5  # Pula para a conclusão
        else:
            next_question()

# Pergunta 4: Doenças infecciosas
if st.session_state.current_question == 4:
    st.subheader('Critérios de saúde')
    st.write('**Você tem ou teve recentemente alguma doença infecciosa como HIV, Hepatite, Malária?**')
    doenca_infecciosa = st.radio('', options=['Sim', 'Não'], key='doenca_infecciosa')
    
    if st.button('Próxima Pergunta ➡️', key='button4'):
        if doenca_infecciosa == 'Sim':
            st.warning('Infelizmente, você não pode doar sangue devido ao histórico de doenças infecciosas.')
            st.session_state.aptidoes = False
        st.session_state.current_question = 5  # Vai para a conclusão

# Conclusão
if st.session_state.current_question == 5:
    st.subheader('Obrigado por participar! 🎉')
    if st.session_state.aptidoes:
        st.success('**Você está apto(a) para doar sangue!** Consulte um profissional de saúde para mais detalhes.')
    else:
        st.warning('**Infelizmente, você não está apto(a) para doar sangue.** Consulte um profissional de saúde para mais detalhes.')
    
    if st.button('Reiniciar Quiz 🔄', key='button5'):
        st.session_state.current_question = 1
        st.session_state.aptidoes = True
        st.experimental_rerun()
