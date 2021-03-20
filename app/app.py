from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
import jwt

from app.controllers.registroPersocnasControllers import RegistroPersocnasControllers
from app.controllers.loginPersonasControllers import LoginPersonas
from app.controllers.calcularImcControllers import CalcularImc

from app.validators.LoginValidator import CreateLoginSchema
from app.validators.ImcValidator import CreateImcSchema

from app.config.config import KEY_TOKEN_AUTH

registroPersonas = RegistroPersocnasControllers()
loginPersonas = LoginPersonas()
calcularImc = CalcularImc()


ImcValidator = CreateImcSchema()
loginSchema = CreateLoginSchema()

app = Flask(__name__)
CORS(app)


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
            ) + datetime.timedelta(seconds=1500), "user": consulta.get('user'), "rutina": consulta.get('rutina'), "dieta": consulta.get('dieta'), "test": consulta.get('test'), 'documento':consulta.get('documento')}, KEY_TOKEN_AUTH, algorithm='HS256')

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
                    print (error)
                    return jsonify({"error": Errorjson})

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})
