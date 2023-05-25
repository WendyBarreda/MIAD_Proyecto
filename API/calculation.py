#!/usr/bin/python

import sys
import os
import numpy as np
import pandas as pd
import joblib
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder


UPLOAD_FOLDER = os.getcwd()

def get_region(depto):
    if depto in ["Sucre", "Magdalena", "La Guajira", "Córdoba", "Cesar", "Bolívar", "Atlántico", "San Andrés, Providencia y Santa Catalina"]:
        return "Region_caribe"
    elif depto in ["Quindío", "Antioquia", "Caldas", "Risaralda"]:
        return "Region_eje_cafetero"
    elif depto in ["Cauca", "Chocó", "Valle del Cauca", "Nariño"]:
        return "Region_pacifica"
    elif depto in ["Cundinamarca", "Boyacá", "Santander", "Norte de Santander", "Huila", "Tolima", "Bogotá D.C."]:
        return "Region_central"
    elif depto in ["Casanare", "Caquetá", "Meta", "Arauca", "Vichada"]:
        return "Region_llanos"
    elif depto in ["Guaviare", "Guanía", "Amazonas", "Putumayo", "Vaupés"]:
        return "Region_amazonia"
    else:
        return "Multiples_departamentos"

def get_proba_adicion(args):
    
    df = pd.DataFrame([[args['Cuantia contrato'],
                                args['Nivel entidad'],
                                args['Orden entidad'],
                                args['Modalidad de contratación'],
                                args['Nombre clase'],
                                args['Departamento ejecución']]], 
                      columns=['cuantia_contrato',
                               'nivel_entidad',
                               'orden_entidad',
                               'modalidad_de_contratacion', 
                               'nombre_clase',
                               'departamento_ejecucion'])
    
    prob = get_proba_adicion_df(df)
    
    return prob

def get_proba_adicion_df(df):
    
    #Preprocesamiento de los datos --------------------------------
    
    #Obtención de región
    df["region_ejecucion"] = df["departamento_ejecucion"].apply(get_region)
    df = df.drop("departamento_ejecucion", axis=1)
    
    #Separamos cuantia contrato 
    cuantia_df = df[['cuantia_contrato']].copy()
    df = df.drop('cuantia_contrato',axis=1)

    # Identificar variables de tipo objeto
    obj_cols = df.select_dtypes(include=['object']).columns
    unique_values = joblib.load(os.path.dirname(__file__) + '/unique_values.pkl') 
    for col in obj_cols:
        if col in df.columns:
            df[col] = pd.Categorical(df[col], categories=unique_values[col])
            df[col] = df[col].cat.codes
    
    #Obtención de dummies
    encoder = joblib.load(os.path.dirname(__file__) + '/encoder.pkl') 
    
    #Codificar el nuevo registro
    categorical_cols = ['nivel_entidad','orden_entidad','modalidad_de_contratacion','nombre_clase','region_ejecucion']
    encoded_nuevo_registro = encoder.transform(df)
    df_encoded = pd.DataFrame(encoded_nuevo_registro, columns=encoder.get_feature_names_out(categorical_cols))
    
    #Adición de la columna cuantia 
    df_encoded = cuantia_df.join(df_encoded)
    
    #Normalización
    scaler = joblib.load(os.path.dirname(__file__) + '/scaler.pkl') 
    df_scaled = scaler.transform(df_encoded)
    
    #Predicción
    model = joblib.load(os.path.dirname(__file__) + '/clf0.pkl') 
    prediccionesProb= model.predict_proba(df_scaled)
    
    #print(prediccionesProb)
    
    #probabilidad = prediccionesProb[0, 0]
    Resultado=set()

    for fila in prediccionesProb:
        Resultado.add(fila[0])
    
    return Resultado

if __name__ == "__main__":

    if len(sys.argv) == 0:
        print('Please add values')
    else:
        modalidad_contratacion = sys.argv[1]
        nivel_entidad = sys.argv[2]
        orden_entidad = sys.argv[3]
        nombre_clase = sys.argv[4]
        cuantia_contrato = sys.argv[5]
        departamento_ejecucion = sys.argv[6]
        
        p1 = get_proba_adicion(modalidad_contratacion,
                              nivel_entidad,
                              orden_entidad,
                              nombre_clase, 
                              cuantia_contrato,
                              departamento_ejecucion)
        
        print('Predicción de adiciones', p1)