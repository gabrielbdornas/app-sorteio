import streamlit as st
from sorteio import sorteio


with st.form("my_form"):
    st.write("Formulário de sorteio de organização HH!")
    names = st.text_input(
        'Informe os participantes do sorteio: ',
        placeholder='Separe os nomes dos participantes por vírgula.'
        )
    submit = st.form_submit_button('Enviar')

    if submit:
        sorteado = sorteio(names.split(','))
        st.write(f'O nome sorteado foi: {sorteado}')
