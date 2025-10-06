import streamlit as st 
from crud import criar_aluno, listar_alunos, atualiza_idade, deletar_aluno

st.set_page_config(page_title="gerenciamento de alunos", page_icon="👩‍🎓")

st.title("sistema de alunos com PostgreSQL")

menu = st.sidebar.radio("menu", ["inserir", "listar", "atualizar", "deletar"])

if menu == "inserir":
    st.subheader("➕ inserir alunos")
    nome = st.text_input("nome", placeholder="seu nome")
    idade = st.number_input("idade", min_value=16, step=1)
    if st.button("cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"aluno {nome} inserido com sucesso! ")
        else: 
            st.warning("o campo nome não pode ser vazio.")

elif menu == "listar":
    st.subheader("listar alunos")
    alunos = listar_alunos()
    if alunos:
        st.dataframe(alunos)
        # for linha in alunos:
        #     st.write(f"id={linha[0]} | nome={linha[1]} | idade={linha[2]}")
    else:
        st.info("nenhhum aluno encontrado!")

elif menu == "atualizar":
    st.subheader("atualizar idade")
    alunos = listar_alunos()
    st.dataframe(alunos)
    if alunos:
        id_aluno = st.selectbox("escolha o id do aluno para atualizar", [linha[0]for linha in alunos])
        nova_idade = st.number_input("nova idade", min_value=16, step=1)
        if st.button("atualizar"):
            atualiza_idade(id_aluno, nova_idade)
            st.success(f"idade do aluno atualizada com sucesso.")
    else: 
        st.info("nenhum aluno disponivel para atualizar")

elif menu == "deletar":
    st.subheader("deletar aluno")
    alunos = listar_alunos()
    st.dataframe(alunos)
    if alunos:
        id_aluno = st.selectbox("escolha o id do aluno que deseja deletar", [linha[0] for linha in alunos])
        if st.button("deletar"):
            deletar_aluno(id_aluno)
            st.success("aluno deletado com sucesso😃!")
    else:
        st.info("nenhum aluno disponivel para deletar")
