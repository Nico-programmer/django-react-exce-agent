import openai
import pandas as pd
from django.conf import settings
import os

openai.api_key = settings.OPENAI_API_KEY

def process_excel_with_instruction(file_path, instruction):
    # Read excel file
    df = pd.read_excel(file_path)
    
    # Convert the fist few rows to text to give context to the model
    context = df.head(20).to_csv(index=False)
    
    # Prompt to model
    prompt = f"""
        Eres un asistente que modifica archivos Excel. A continuación tienes una tabla en formato CSV (solo las primeras filas)
        
        Tabla:
        {context}
        
        Instrucción del usuario:
        {instruction}
        
        Describe que cambios hacer (en formato código Python usando pandas)
    """
    
    response = openai.ChatCompletion.create(
        model = "gpt-3",
        messages = [{"role": "user", "content":prompt}],
        temperature = 0.2,
    )
    
    code = response["choices"][0]["message"]["content"]
    
    # Create a safe execution environment to run only code on `df`
    local_vars = {"df": df}
    
    try:
        exec(code, {}, local_vars)
        df_modified = local_vars["df"]
    except Exception as e:
        raise ValueError(f"Error al ejecutar código generado por IA: {e}")
    
    # Save the new file
    output_path = os.path.splitext(file_path)[0] + "_modified.xlsx"
    df_modified.to_excel(output_path, index=False)
    return output_path