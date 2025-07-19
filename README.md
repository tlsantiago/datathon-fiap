# Decision Datathon - Previsão de Contratação com IA

Este projeto foi desenvolvido como parte do Desafio Datathon da fase 05 da FIAP. O objetivo era utilizar algum modelo de IA para auxiliar em processo de recrutamento e seleção. 
Para isso, desenvolvi um modelo que foca em prever se um candidato tem aderência e fortes chances de contratação com base em seu perfil e os requisitos da vaga.

## 🧠 Técnicas utilizadas

- XGBoost com tuning via RandomizedSearchCV
- SMOTE para lidar com desbalanceamento de classes
- Pipeline com ColumnTransformer para tratar variáveis categóricas
- Interface interativa com Streamlit

## 📈 Resultados

- Recall para candidatos contratados: **90%**
- Threshold ajustado no app para aumentar precisão
- Modelo salvo como `modelo_decision.pkl` para leitura no app.py do streamlit
