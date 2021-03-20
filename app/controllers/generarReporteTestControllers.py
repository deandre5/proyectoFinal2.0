from app.model.PersonasModel import Personas

import io
import xlwt

personas = Personas()

class ReporteTest():
    def generarReporte(self):

        

        consulta = personas.consultarTest()

        output = io.BytesIO()

        workbook = xlwt.Workbook()
        sh = workbook.add_sheet("reporte de test")

        sh.write(0, 0, "Nombres")
        sh.write(0, 1, "Apellidos")
        sh.write(0, 2, "Documento")
        sh.write(0, 3, "Peso")
        sh.write(0, 4, "Talla")
        sh.write(0, 5, "IMC")

        idx = 0

        for item in consulta:

            sh.write(idx+1, 0, str(item.get('nombres')))
            sh.write(idx+1, 1, str(item.get('apellidos')))
            sh.write(idx+1, 2, str(item.get('documento')))
            sh.write(idx+1, 3, str(item.get('peso')))
            sh.write(idx+1, 4, str(item.get('talla')))
            sh.write(idx+1, 5, str(item.get('imc')))

            idx += 1
        workbook.save(output)
        output.seek(0)

        return output
