from flask import Blueprint, render_template, send_file
from models.prestamo_model import Prestamo
from io import BytesIO
from xlsxwriter import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

reporte_bp = Blueprint('reporte_controller', __name__)

@reporte_bp.route('/reportes/prestamos/pdf')
def reporte_prestamos_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    prestamos = Prestamo.query.all()

    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, 750, "Reporte de Préstamos")
    p.setFont("Helvetica", 10)

    y = 720
    for prestamo in prestamos:
        linea = f"{prestamo.usuario} - {prestamo.copia.codigo_interno} - {prestamo.fecha_prestamo} - {prestamo.estado}"
        p.drawString(40, y, linea)
        y -= 15
        if y < 50:
            p.showPage()
            y = 750

    p.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='prestamos.pdf', mimetype='application/pdf')

@reporte_bp.route('/reportes/prestamos/excel')
def reporte_prestamos_excel():
    buffer = BytesIO()
    workbook = Workbook(buffer)
    worksheet = workbook.add_worksheet()

    worksheet.write_row(0, 0, ['Usuario', 'Código Copia', 'Fecha Préstamo', 'Fecha Devolución', 'Estado'])
    row = 1
    for p in Prestamo.query.all():
        worksheet.write_row(row, 0, [
            p.usuario,
            p.copia.codigo_interno,
            str(p.fecha_prestamo),
            str(p.fecha_devolucion),
            p.estado
        ])
        row += 1

    workbook.close()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='prestamos.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
