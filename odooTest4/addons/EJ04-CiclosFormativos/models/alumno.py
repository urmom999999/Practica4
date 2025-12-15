from odoo import models, fields

class Alumno(models.Model):
    _name = 'alumno'
    _description = 'Alumno'
    
    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    dni = fields.Char(string='DNI', required=True, size=9)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')