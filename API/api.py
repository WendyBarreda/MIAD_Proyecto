#!/usr/bin/python
from flask import Flask, request
from flask_restx import Api, Resource, fields
from calculation import get_proba_adicion,get_proba_adicion_df

import os
from werkzeug.utils import secure_filename
import pandas as pd
from werkzeug.datastructures import FileStorage


UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = set(['xlsx'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

api = Api(
    app, 
    version='1.0', 
    title='Predicción de adiciones',
    description='Esta API retorna la probabilidad de presentar adciones')

ns = api.namespace('adiciones', description='Retorna probabilidad de tener una adición')


#Parametros para caso unico
parser = api.parser()

parser.add_argument(
    'Modalidad de contratación', 
    type=str, 
    required=True, 
    help='Modalidad de contratación', 
    location='args')

parser.add_argument(
    'Tipo de contrato', 
    type=str, 
    required=True, 
    help='Tipo de contrato', 
    location='args')

parser.add_argument(
    'Municipio ejecución', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el municipio de ejecución.', 
    location='args')

parser.add_argument(
    'Cuantia proceso', 
    type=int, 
    required=True, 
    help='Por favor ingrese un valor valido para la cuantia del proceso.', 
    location='args')

parser.add_argument(
    'Departamento y municipio contratista', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el departamento y municipio del contratista.', 
    location='args')

parser.add_argument(
    'Municipio entidad', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el municipio de la entidad.', 
    location='args')

parser.add_argument(
    'Departamento entidad', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el departamento de la entidad.', 
    location='args')

parser.add_argument(
    'Departamento ejecución', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el departamento de ejecución.', 
    location='args')


#Parametros para archivo
parserf = api.parser()
parserf.add_argument('Archivo', type=FileStorage, location='files',required=True, action='append')



resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PredicAdicionesAPI(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": get_proba_adicion(args)
        }, 200
    
@ns.route('/file')
class PredicAdicionesAPIFile(Resource):
    
    @api.doc(parser=parserf)
    @api.marshal_with(resource_fields)
    def post(self):
        #Lectura del archivo 
        file = request.files['Archivo']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
            df = pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
            return {
             "result": get_proba_adicion_df(df)
            }, 200
        else:
            return {
             "result": "Carga un archivo xlsx"
            }, 200
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)