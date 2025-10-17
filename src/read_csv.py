import pandas as pd
import streamlit as st
from validator import PlanilhaVendas
from pydantic import ValidationError

def read_data(df):
    progress_bar = st.progress(0)
    total_rows = len(df)
    error = []
    valid_rows = []

    for i, row in df.iterrows():
        progress_bar.progress((i + 1) / total_rows)
        
        try:
            data = row.to_dict()
            
            valid_schema = PlanilhaVendas(**data)
            valid_rows.append(valid_schema)
            
        except ValidationError as e:
            error.append(f"Erro na linha {i + 2}: {str(e)}")
            
    return valid_rows, error

def main():
    st.title("Validação de dados da Campanha")
    st.write("Faça upload do arquivo CSV para validação dos dados.")
    
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            st.write("Preview dos dados:")
            st.dataframe(df.head())
            
            if st.button("Validar Dados:"):
                with st.spinner("Validando..."):
                    valid_rows, errors = read_data(df)
                    
                    if errors:
                        st.error("Foram encontrados erros na validação:")
                        for err in errors:
                            st.write(err)
                    else:
                        st.success("Todos os dados são válidos!")
                    
                        st.write(f"Número de registros válidos: {len(valid_rows)}")
                        
                        valid_df = pd.DataFrame([data.model_dump() for data in valid_rows])
                        st.download_button(
                            label="Baixar dados válidos como CSV",
                            data=valid_df.to_csv(index=False),
                            file_name='dados_validos.csv',
                            mime='text/csv'
                        )
                    
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")
            
if __name__ == "__main__":
    main()