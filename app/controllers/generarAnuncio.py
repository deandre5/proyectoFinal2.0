from app.model.AnunciosModel import Anuncios
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader
import cloudinary.api
import datetime
import bcrypt

anuncios = Anuncios()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

cloudinary.config(
    cloud_name='hdjsownnk',
    api_key='926599253344788',
    api_secret='I8rBOy-rnozmrxhNL_Lg7hqtj7s'
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class GenerarAnuncio():
    def generar(self, content, file):
        try:

            if allowed_file(file.filename):

                filename = secure_filename(file.filename)

                titulo = content["titulo"]
                descripcion = content["descripcion"]

                dia = datetime.datetime.utcnow()
                salt = bcrypt.gensalt()
                hash = bcrypt.hashpw(
                    bytes(str(dia), encoding='utf-8'), salt)

                h = str(hash).split('/')

                if len(h) > 2:
                    t = h[1]+h[2]
                else:
                    t = h[0]

                filename = str(t)

                cloudinary.uploader.upload(file, public_id=filename)
                url = cloudinary.utils.cloudinary_url(filename)

                consulta = anuncios.consultar()

                if consulta:
                    for i in consulta:
                        id_bd = i.get('id')+1
                # si no hay ejercicios registrados, este toma el valor de 1
                else:
                    id_bd = 1

                registrar = anuncios.insert(id_bd, titulo, descripcion, url[0])

                return registrar

        except Exception as error:
            status = False
            return status

    def consultnombre(self, content):
        nombre = content['titulo']

        consult = anuncios.consultarAnuncios(nombre)
        return consult
