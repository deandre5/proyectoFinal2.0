from app.model.AnunciosModel import Anuncios

anuncios = Anuncios()


class EliminarAnuncios():
    def eliminar(self, id):

        consulta = anuncios.ConsultaId(id)

        if (len(consulta) > 0):
            anuncios.remove(id)
            return True

        else:
            return False