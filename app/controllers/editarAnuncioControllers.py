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


class EditarAnuncios():
    def editarConFoto(self, id, content, file):

        anuncio = anuncios.ConsultaId(id)

        if (len(anuncio) < 1):
            return False

        titulo = content["titulo"]

        verificarNombre = anuncios.consultarAnuncios(titulo)

        if (verificarNombre):
            return 'NO'

        if allowed_file(file.filename):

            descripcion = content["descripcion"]

            filename = secure_filename(file.filename)

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

            actualizacion = anuncios.actualizacion(
                id, titulo, descripcion, url[0])

            if actualizacion:

                return actualizacion

        else:

            status = int(0)
            return status

    def editarSinFoto(self, id, content):
        anuncio = anuncios.ConsultaId(id)

        if (len(anuncio) < 1):
            return False

        titulo = content["titulo"]
        descripcion = content["descripcion"]
        imagen = content["url"]

        verificarNombre = anuncios.consultarAnuncios(titulo)

        if (verificarNombre):
            return 'NO'

        actualizacion = anuncios.actualizacion(id, titulo, descripcion, imagen)

        return actualizacion
