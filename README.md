# ETL com Python, CSV e Dashboard
Este projeto é uma aplicação web interativa para análise de dados de campanhas de marketing digital, construída com Streamlit, Pandas e Plotly. Feito através de um Worshop da Jornada de Dados
## 📋 Requisitos
```bash
pip install -r requirements.txt
```
## 🚀 Como Executar
1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/etl-python-excel.git

cd etl-python-excel
```
2. Instale as dependências
```bash
pip install -r requirements.txt
```
3. Execute a aplicação
```bash
streamlit run dashboard.py
```
## 📊 Funcionalidades
- **Upload de Dados**: Suporte para arquivos CSV
- **KPIs Principais**:
    - Mês com Maior Gasto
    - Total de Conversões
    - Total de Cliques
    - Custo por Conversão Médio
- **Visualizações**:
    - Gráfico de Gastos Diários
    - Análise de Segmentação
    - Métricas de Performance (CPC, CPM, CPA)
    - Análise Mensal Interativa
## 🛠 Tecnologias Utilizadas
- [Streamlit](vscode-file://vscode-app/c:/Users/admin/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
- [Pandas](vscode-file://vscode-app/c:/Users/admin/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
- [Plotly](vscode-file://vscode-app/c:/Users/admin/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
- [Pydantic](vscode-file://vscode-app/c:/Users/admin/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
- [YData Profiling](vscode-file://vscode-app/c:/Users/admin/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)

## 📊 Formato dos Dados
O arquivo CSV deve conter as seguintes colunas:
- Organizador
- Ano_Mes
- Dia_da_Semana
- Tipo_Dia
- Objetivo
- Date
- AdSet_name
- Amount_spent
- Link_clicks
- Impressions
- Conversions
- Segmentação
- Tipo_de_Anúncio
- Fase
