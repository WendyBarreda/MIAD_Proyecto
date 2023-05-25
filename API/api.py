#!/usr/bin/python
#pip install flask-wtf -- En Console

from flask import Flask, request
from flask_restx import Api, Resource, fields
from calculation import get_proba_adicion,get_proba_adicion_df

import os
from werkzeug.utils import secure_filename
import pandas as pd
from werkzeug.datastructures import FileStorage
import joblib

from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = set(['xlsx'])

# Cargar las distintas opciones para los drop down desde los archivos pkl
opciones_cargadas                  = joblib.load(os.path.dirname(__file__) + '/opciones.pkl') 
nivel_entidad_cargadas             = joblib.load(os.path.dirname(__file__) + '/lista_nivelEntidad.pkl')
orden_entidad_cargadas             = joblib.load(os.path.dirname(__file__) + '/lista_ordenEntidad.pkl')
modalidad_de_contratacion_cargadas = joblib.load(os.path.dirname(__file__) + '/lista_modalidadContratacion.pkl')
nombre_clase_cargadas              = joblib.load(os.path.dirname(__file__) + '/lista_nombreClase.pkl')
    
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class MyForm(FlaskForm):
    departamento_ejecucion    = SelectField('Departamento de Ejecución', choices=opciones_cargadas, validators=[DataRequired()])
    nivel_entidad             = SelectField('Nivel entidad', choices=nivel_entidad_cargadas, validators=[DataRequired()])
    orden_entidad             = SelectField('Orden entidad', choices=orden_entidad_cargadas, validators=[DataRequired()])
    modalidad_de_contratacion = SelectField('Modalidad de contratación', choices=modalidad_de_contratacion_cargadas, validators=[DataRequired()])
    nombre_clase              = SelectField('Nombre clase', choices=nombre_clase_cargadas, validators=[DataRequired()])

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
    help='Por favor ingrese un valor valido para la Modalidad de contratación', 
    location='args',
    choices=modalidad_de_contratacion_cargadas)

parser.add_argument(
    'Nivel entidad', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el Nivel de la entidad', 
    location='args',
    choices=nivel_entidad_cargadas)

parser.add_argument(
    'Orden entidad', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el Orden de la entidad.', 
    location='args',
    choices=orden_entidad_cargadas)

parser.add_argument(
    'Nombre clase', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el nombre de la clase.', 
    location='args',
    choices=nombre_clase_cargadas)

parser.add_argument(
    'Cuantia contrato', 
    type=int, 
    required=True, 
    help='Por favor ingrese un valor valido para la cuantia del contrato.', 
    location='args')

parser.add_argument(
    'Departamento ejecución', 
    type=str, 
    required=True, 
    help='Por favor ingrese un valor valido para el Departamento de ejecución.', 
    location='args',
    choices=opciones_cargadas)


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