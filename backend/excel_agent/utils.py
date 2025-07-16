import pandas as pd
from io import BytesIO

# Function to process excel
def process_excel(file, instruction):
    # Read File
    df = pd.read_excel(file)
    
    # 🔧 Simulation of instruction interpretation
    if "suma" in instruction.lower() and "columna" in instruction.lower():
        # Validation try-except
        try:
            col = instruction.lower().split("columna")[-1].strip()[0].upper()
            col_index = ord(col) - ord('A')
            column_name = df.columns[col_index]
            suma = df[column_name].sum()
            df.loc[len(df)] = [None] * len(df.columns)
            df.loc[len(df)] = [f"Suma de {column_name}", suma] + [None] * (len(df.columns) - 2)
        except Exception as e:
            print("Error interpretando la columna:", e)
    
    # Save modified file in memory
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return output