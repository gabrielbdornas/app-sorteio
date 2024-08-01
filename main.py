import streamlit as st
from sorteio import sorteio_unico, sorteio_ordenado


with st.form("my_form"):
    st.write("Formulário de sorteio de organização HH!")
    names = st.text_input(
        'Informe os participantes do sorteio: ',
        placeholder='Separe os nomes dos participantes por vírgula.'
        )
    ordenar = st.toggle(
        'Ordenar lista de sorteados?'
    )
    submit = st.form_submit_button('Enviar')

    if submit:
        if ordenar:
            sorteados = sorteio_ordenado(names.split(','))
            st.write('A ordem dos sorteados foi:')
            count = 1
            for sorteado in sorteados:
                st.write(f'{count}° sorteado: {sorteado}.')
                count +=1
        else:
            sorteado = sorteio_unico(names.split(','))
            st.write(f'O nome sorteado foi: {sorteado}')
