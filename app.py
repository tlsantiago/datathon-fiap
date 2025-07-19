import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load("modelo_decision.pkl")

st.set_page_config(page_title="Análise de Candidato", layout="wide")

st.markdown("<h2 style='text-align: center;'>🔍 Avaliação de Candidatos com IA</h2>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    nivel_academico = st.selectbox("Nível Acadêmico", ["Médio", "Técnico", "Tecnólogo", "Superior", "Pós-graduação", "Mestrado", "Doutorado"])
    ingles = st.selectbox("Inglês", ["Nenhum", "Técnico", "Intermediário", "Avançado", "Fluente"])
    espanhol = st.selectbox("Espanhol", ["Nenhum", "Técnico", "Intermediário", "Avançado", "Fluente"])
    tipo_contratacao = st.selectbox("Tipo de Contratação", ["CLT", "PJ", "Cooperado", "Estágio", "Outros"])
    vaga_nivel = st.selectbox("Nível da Vaga", ["Júnior", "Pleno", "Sênior", "Especialista"])

with col2:
    area_atuacao = st.selectbox("Área de Atuação Profissional", [
        "TI - Desenvolvimento", "Infraestrutura", "Dados", "Gestão de Projetos",
        "Segurança da Informação", "Suporte", "Outros"
    ])
    nivel_prof = st.selectbox("Nível Profissional", ["Júnior", "Pleno", "Sênior", "Especialista"])
    conhecimentos = st.selectbox("Conhecimentos Técnicos", [
        "Java", "Python", "SQL", "Cloud", "DevOps", "C#", "SAP", "Sem conhecimento", "Outros"
    ])
    vaga_ingles = st.selectbox("Inglês Exigido na Vaga", ["Nenhum", "Técnico", "Intermediário", "Avançado", "Fluente"])
    vaga_area = st.selectbox("Área da Vaga", [
        "TI - Desenvolvimento", "Infraestrutura", "Dados", "Gestão de Projetos",
        "Segurança da Informação", "Suporte", "Outros"
    ])

if st.button("Avaliar Candidato"):
    dados = pd.DataFrame([{
        "formacao_e_idiomas_nivel_academico": nivel_academico,
        "formacao_e_idiomas_nivel_ingles": ingles,
        "formacao_e_idiomas_nivel_espanhol": espanhol,
        "informacoes_profissionais_area_atuacao": area_atuacao,
        "informacoes_profissionais_nivel_profissional": nivel_prof,
        "informacoes_profissionais_conhecimentos_tecnicos": conhecimentos,
        "informacoes_basicas_tipo_contratacao": tipo_contratacao,
        "perfil_vaga_nivel profissional": vaga_nivel,
        "perfil_vaga_nivel_ingles": vaga_ingles,
        "perfil_vaga_areas_atuacao": vaga_area
    }])

    prob = modelo.predict_proba(dados)[0][1]
    ajuste = 0.0

    if nivel_prof in ["Pleno", "Sênior", "Especialista"] and vaga_nivel in ["Júnior", "Pleno"]:
        ajuste += 0.10
    if ingles in ["Avançado", "Fluente"] and vaga_ingles in ["Técnico", "Intermediário", "Avançado"]:
        ajuste += 0.10
    if area_atuacao == vaga_area:
        ajuste += 0.10
    if conhecimentos != "Sem conhecimento":
        ajuste += 0.05
    if nivel_academico in ["Superior", "Pós-graduação", "Mestrado", "Doutorado"] and vaga_nivel in ["Júnior", "Pleno", "Sênior"]:
        ajuste += 0.05

    prob_ajustada = min(prob + ajuste, 1.0)
    percentual = round(prob_ajustada * 100, 2)

    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🔎 Resultado da Avaliação</h3>", unsafe_allow_html=True)

    if percentual >= 70:
        cor = "#4CAF50"
        recomendacao = "✅ Excelente candidato! Altamente recomendável."
    elif percentual >= 50:
        cor = "#FFC107"
        recomendacao = "⚠️ Candidato com potencial. Requer análise mais profunda."
    else:
        cor = "#F44336"
        recomendacao = "❌ Baixa probabilidade de contratação."

    st.markdown(
        f"""
        <div style='background-color: {cor}; padding: 20px; border-radius: 10px; text-align: center; color: white;'>
            <h2>{percentual}%</h2>
            <p style='font-size: 18px;'>{recomendacao}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
