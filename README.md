📊 Projeto Final - Datathon FIAP: Recrutamento Inteligente com IA
==================================================================

Este projeto foi desenvolvido como entrega do **Tech Challenge do curso de Pós-Graduação em Data Analytics da FIAP**. O desafio consistiu em aplicar técnicas de ciência de dados para melhorar o processo de recrutamento e seleção, utilizando dados da empresa Decision.

📌 Objetivo
-----------
Construir uma aplicação de inteligência artificial que avalie, com base no perfil dos candidatos e nas exigências das vagas, a probabilidade de contratação, oferecendo aos recrutadores uma ferramenta de apoio à decisão no processo de recrutamento.

⚙️ Tecnologias e Bibliotecas Utilizadas
---------------------------------------
- Python 3.10
- Pandas / NumPy
- Scikit-learn
- Streamlit
- Joblib

📈 Abordagem e Modelo
---------------------
- Foi utilizada uma base unificada de dados contendo candidatos, vagas e interações (prospects).
- Após análises e testes, utilizou-se um modelo de **Regressão Logística com balanceamento de classes**.
- As variáveis foram reduzidas para as mais relevantes, de modo a melhorar a performance e reduzir o tamanho do modelo (limitado a 25MB pelo Streamlit Cloud).
- O modelo foi treinado com pipeline de transformação categórica via OneHotEncoder.

📄 Variáveis utilizadas no modelo
---------------------------------
- formacao_e_idiomas_nivel_academico  
- formacao_e_idiomas_nivel_ingles  
- formacao_e_idiomas_nivel_espanhol  
- informacoes_profissionais_area_atuacao  
- informacoes_profissionais_nivel_profissional  
- informacoes_profissionais_conhecimentos_tecnicos  
- informacoes_basicas_tipo_contratacao  
- perfil_vaga_nivel profissional  
- perfil_vaga_nivel_ingles  
- perfil_vaga_areas_atuacao  

⚠️ Ajuste de Aderência no Frontend
----------------------------------
Para contornar limitações do modelo e simular um sistema mais robusto, foram aplicados **ajustes condicionais no frontend (Streamlit)** que aumentam a probabilidade final em casos de alta aderência entre os dados do candidato e os requisitos da vaga. Por exemplo:
- Quando o candidato possui fluência em inglês e a vaga exige nível técnico ou intermediário.
- Quando o nível profissional do candidato supera ou corresponde ao exigido na vaga.

🔬 Detalhes do Treinamento
--------------------------
Para mais informações sobre o pipeline de treinamento, avaliação e salvamento do modelo, consulte o notebook [`model.ipynb`](model.ipynb).
