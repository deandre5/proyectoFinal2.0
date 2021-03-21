from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import datetime
import jwt
import cloudinary
import cloudinary.uploader
import cloudinary.api
from werkzeug.utils import secure_filename

from app.controllers.registroPersocnasControllers import RegistroPersocnasControllers
from app.controllers.loginPersonasControllers import LoginPersonas
from app.controllers.calcularImcControllers import CalcularImc
from app.controllers.consultarTestControllers import ConsultarTest
from app.controllers.generarReporteTestControllers import ReporteTest
from app.controllers.generarAnuncio import GenerarAnuncio
from app.controllers.consultarAnunciosControllers import ConsultarAnuncios
from app.controllers.eliminarAnuncioControllers import EliminarAnuncios
from app.controllers.editarAnuncioControllers import EditarAnuncios
from app.controllers.EstadisticasControllers import Estadisticas

from app.validators.LoginValidator import CreateLoginSchema
from app.validators.ImcValidator import CreateImcSchema
from app.validators.AnuncioValidator import CreateAnuncioSchema

from app.config.config import KEY_TOKEN_AUTH

registroPersonas = RegistroPersocnasControllers()
loginPersonas = LoginPersonas()
calcularImc = CalcularImc()
consultarTests = ConsultarTest()
reporteTest = ReporteTest()
generarAnuncio = GenerarAnuncio()
consultaAnuncios = ConsultarAnuncios()
eliminarAnuncios = EliminarAnuncios()
actualizarAnuncios = EditarAnuncios()
estadistica = Estadisticas()


ImcValidator = CreateImcSchema()
loginSchema = CreateLoginSchema()
anuncioSchema = CreateAnuncioSchema()

app = Flask(__name__)
CORS(app)

cloudinary.config(
    cloud_name='hdjsownnk',
    api_key='926599253344788',
    api_secret='I8rBOy-rnozmrxhNL_Lg7hqtj7s'
)


def validacion(headers):
    token = headers.split(' ')

    try:
        # se devulve la informacion util del usuario
        data = jwt.decode(token[1], KEY_TOKEN_AUTH, algorithms=['HS256'])
        status = True
        print(data)
        return data
    except Exception as error:
        print(error)
        status = False
        return status


@app.route('/admin')
def index():
    encode_jwt = jwt.encode({'exp': datetime.datetime.utcnow(
    ) + datetime.timedelta(seconds=1500), "user": "admin"}, KEY_TOKEN_AUTH, algorithm='HS256')

    print(encode_jwt)

    return jsonify({"status": "ok", "token": encode_jwt})


@app.route("/registrar", methods=["POST"])
def registrar():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:

                    content = request.get_json()

                    consulta = registroPersonas.consultar(content)

                    if (consulta):
                        return jsonify({"status": "BAD", "message": 'El correo o el documento ya estan registrdos'}), 200

                    else:

                        registro = registroPersonas.registrar(content)

                        if (registro):

                            return jsonify({"status": "OK"}), 200
                        else:
                            return jsonify({"status": str(registro)}), 500

                except Exception as error:
                    Errorjson = str(error)
                    return jsonify({"error": Errorjson})

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route('/login', methods=['POST'])
def login():

    try:
        content = request.get_json()
        validate = loginSchema.load(content)

        consulta = loginPersonas.login(content)

        if (consulta):

            encode_jwt = jwt.encode({'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(seconds=1500), "user": consulta.get('user'), "rutina": consulta.get('rutina'), "dieta": consulta.get('dieta'), "test": consulta.get('test'), 'documento': consulta.get('documento')}, KEY_TOKEN_AUTH, algorithm='HS256')

            return jsonify({"status": "OK", "token": encode_jwt}), 200

        else:
            return jsonify({"status": "User not valid"})

    except Exception as Error:
        tojson = str(Error)
        return jsonify({"status": "Error", "message": tojson})


@app.route('/calcularimc/<int:id>', methods=['POST'])
def imc(id):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:
                    content = request.get_json()
                    validator = ImcValidator.load(content)
                    documento = str(id)

                    registrar = calcularImc.calcular(content, documento)

                    if isinstance(registrar, str):
                        return jsonify({"status": "No existe el usuario"}), 406

                    if (registrar):
                        return jsonify({"status": "OK"})
                    else:
                        return jsonify({"status": "Error"})

                except Exception as error:
                    Errorjson = str(error)
                    print(error)
                    return jsonify({"error": Errorjson})

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route('/consultarTest', methods=['GET'])
def consultarTest():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:

                    tests = consultarTests.consultar()

                    if (tests):
                        return jsonify({"status": "OK", "test": tests})
                    else:
                        return jsonify({"status": "ERROR"})

                except Exception as error:
                    Errorjson = str(error)
                    print(error)
                    return jsonify({"error": Errorjson})

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route('/consultarTestId', methods=['GET'])
def consultarTestId():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            idtest = validar.get('test')

            if idtest == "null":
                return jsonify({"status": "porfavor acerquese a un instructor para realizar su test"})

            test = consultarTests.consultarTestId(idtest)

            if (test):
                return jsonify({"status": "OK", "test": test})
            else:
                return jsonify({"status": "ERROR, no existe el test"})
        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route('/generarReporte', methods=['GET'])
def generarReporte():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:

                    reporte = reporteTest.generarReporte()
                    return Response(reporte, mimetype="application/ms-excel", headers={"content-Disposition": "attachment; filename=reporteTest.csv"})

                except Exception as error:
                    Errorjson = str(error)
                    print(error)
                    return jsonify({"error": Errorjson})
            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                consulta = estadistica.generarEstadisticas()

                if (consulta):
                    return jsonify({"status": "OK", "estadisticas": consulta})
                else:
                    return jsonify({"status": "ERROR"})

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route('/crearAnuncio', methods=['POST'])
def crearAnuncio():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:
                    validarSchema = anuncioSchema.validate(request.form)

                    content = request.form

                    if (request.files):

                        file = request.files['imagen']

                        consultnombre = generarAnuncio.consultnombre(content)

                        if consultnombre:
                            return jsonify({"status": "BAD", "message": "Nombe ya se encuentra registrado"})

                        else:
                            registro = generarAnuncio.generar(content, file)

                            if (registro):
                                return jsonify({'status': 'ok'}), 200

                except Exception as error:
                    tojson = str(error)
                    print(tojson)
                    return jsonify({"status": "no es posible validar", "error": tojson}), 406

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route("/editarAnuncio/<int:id>", methods=["PUT"])
def editarAnuncioID(id):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:
                    id = str(id)
                    validarSchema = anuncioSchema.validate(request.form)
                    content = request.form

                    if len(request.files) > 0:
                        file = request.files['imagen']

                        actualizar = actualizarAnuncios.editarConFoto(
                            id, content, file)

                        if actualizar == 0:

                            return jsonify({"status": "error, ingrese un archivo valido"}), 400

                        if isinstance(actualizar, str):
                            print("STR")
                            return jsonify({"status": "error, ya hay un anuncio con ese nombre"}), 400

                        if actualizar:
                            return jsonify({"status": "OK"})
                        else:
                            return jsonify({"status": "Error, no existe el anuncio", })

                    else:
                        actualizar = actualizarAnuncios.editarSinFoto(
                            id, content)

                        if isinstance(actualizar, str):
                            return jsonify({"status": "error, ya hay un anuncio con ese nombre"}), 400

                        if (actualizar):
                            return jsonify({"status": "OK"}), 200
                        else:
                            return jsonify({"status": "Error, no existe el anuncio", })
                except Exception as error:
                    tojson = str(error)
                    print(tojson)
                    return jsonify({"status": "no es posible validar", "error": tojson}), 406

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route('/consultarAnuncios', methods=['GET'])
def consultarAnuncios():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):

            anuncios = consultaAnuncios.consultaGeneral()

            if (anuncios):

                return jsonify({"status": "OK", "anuncios": anuncios})

            else:
                return jsonify({"status": "ERROR"}), 400

        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route('/consultarAnuncios/<int:id>', methods=['GET'])
def consultarAnunciosID(id):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            id = str(id)
            anuncios = consultaAnuncios.consultaId(id)

            if (anuncios):

                return jsonify({"status": "OK", "anuncios": anuncios})

            else:
                return jsonify({"status": "No existe el anuncio"}), 400

        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})


@app.route("/eliminar/<int:id>", methods=['DELETE'])
def eliminarAnuncio(id):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validacion(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                id = str(id)

                eliminar = eliminarAnuncios.eliminar(id)

                if (eliminar):
                    return jsonify({"status": "OK"})

                else:
                    return jsonify({"status": "No existe el anuncio"})

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})
