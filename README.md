# 📊 Projeto Final - Datathon FIAP: Recrutamento Inteligente com IA

Este projeto foi desenvolvido como entrega do **Tech Challenge do curso de Pós-Graduação em Data Analytics da FIAP**. O desafio consistiu em aplicar técnicas de ciência de dados para **melhorar o processo de recrutamento e seleção de candidatos**, utilizando inteligência artificial.

## 🚀 Objetivo

Desenvolver um modelo preditivo capaz de **avaliar automaticamente a probabilidade de contratação** de um candidato com base em atributos como formação, experiência, idiomas e requisitos da vaga. A interface do sistema foi implementada com **Streamlit**, simulando um sistema de apoio à decisão para recrutadores.

---

## 🧠 Abordagem

1. **Fonte de Dados**: Foram utilizados três arquivos `.json` com dados anonimizados de candidatos, vagas e interações.
2. **Tratamento e Engenharia de Atributos**: Após análise exploratória, as variáveis mais relevantes foram selecionadas.
3. **Modelagem**:
   - Modelo: `RandomForestClassifier` com `n_estimators=30` e `max_depth=7`.
   - Pipeline com `OneHotEncoder` para tratamento de variáveis categóricas.
   - Balanceamento aplicado para lidar com desbalanceamento da variável-alvo.
   - Compressão aplicada para permitir deploy no Streamlit (arquivo final < 6MB).
4. **Interface**: Desenvolvida com Streamlit, conta com simulação visual e ajustes de score para refletir a aderência real do candidato à vaga.
5. **Deploy**: Aplicação publicada no [Streamlit Cloud](https://streamlit.io/).

---

## 📋 Variáveis Utilizadas no Modelo

| Categoria                     | Variáveis                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| Formação e Idiomas           | `formacao_e_idiomas_nivel_academico`, `formacao_e_idiomas_nivel_ingles`, `formacao_e_idiomas_nivel_espanhol` |
| Experiência Profissional     | `informacoes_profissionais_area_atuacao`, `informacoes_profissionais_nivel_profissional`, `informacoes_profissionais_conhecimentos_tecnicos` |
| Dados da Vaga                | `informacoes_basicas_tipo_contratacao`, `perfil_vaga_nivel profissional`, `perfil_vaga_nivel_ingles`, `perfil_vaga_areas_atuacao` |

