from app.model.AnunciosModel import Anuncios

anuncios = Anuncios()


class ConsultarAnuncios():
    def consultaGeneral(self):

        anunciosSistem = anuncios.consultar()
        return anunciosSistem

    
    def consultaId(self, id):

        anuncioSistem = anuncios.ConsultaId(id)
        return anuncioSistem