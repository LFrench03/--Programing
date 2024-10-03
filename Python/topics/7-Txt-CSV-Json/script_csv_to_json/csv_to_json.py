import pandas as pd
import json

def csv_to_json(ruta_csv, ruta_json):
    try:
        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(ruta_csv)

        # Generando el diccionario a partir del DataFrame completo
        titanic_json = df.to_dict(orient='records')

        # Guardando en archivo Json
        with open(ruta_json, 'w') as archivo_json:
            json.dump(titanic_json, archivo_json, indent=4)
        
        print("Archivo JSON creado exitosamente.")
    except Exception as e:
        print(f"Error al procesar el archivo CSV: {e}")
#Prueba:
ruta_csv = 'titanic.csv'
ruta_json = 'sample.json'
csv_to_json(ruta_csv,ruta_json)

