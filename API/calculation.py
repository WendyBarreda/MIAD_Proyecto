#!/usr/bin/python

import sys
import os
import numpy as np
import pandas as pd

UPLOAD_FOLDER = os.getcwd()

def get_proba_adicion(args):

    df = pd.DataFrame([[args['Modalidad de contratación'],
                                args['Tipo de contrato'],
                                args['Municipio ejecución'],
                                args['Cuantia proceso'],
                                args['Departamento y municipio contratista'],
                                args['Municipio entidad'],
                                args['Departamento entidad'],
                                args['Departamento ejecución']]], 
                      columns=['modalidad_contratación',
                               'tipo_de_contrato',
                               'municipio_ejecucion',
                               'cuantia_proceso',
                               'departamento_y_municipio_contratista',
                               'municipio_entidad',
                               'departamento_entidad',
                               'departamento_ejecucion'])
    
    prob = get_proba_adicion_df(df)
    
    return prob

def get_proba_adicion_df(df):
    
    print(df)
    
    return '0.95'

if __name__ == "__main__":

    if len(sys.argv) == 0:
        print('Please add values')
    else:
        modalidad_contratacion = sys.argv[1]
        tipo_de_contrato = sys.argv[2]
        municipio_ejecucion = sys.argv[3]
        cuantia_proceso = sys.argv[4]
        departamento_y_municipio_contratista = sys.argv[5]
        municipio_entidad = sys.argv[6]
        departamento_entidad = sys.argv[7]
        departamento_ejecucion = sys.argv[8]
        
        p1 = get_proba_adicion(modalidad_contratacion,
                              tipo_de_contrato,
                              municipio_ejecucion,
                              cuantia_proceso, 
                              departamento_y_municipio_contratista,
                              municipio_entidad,
                              departamento_entidad,
                              departamento_ejecucion)
        
        print('Predicción de adiciones', p1)
        