from odoo import models, fields

class Profesor(models.Model):
    _name = 'profesor'
    _description = 'Profesor'
    
    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    dni = fields.Char(string='DNI', required=True, size=9)
    especialidad = fields.Char(string='Especialidad')
    modulo_ids = fields.One2many('modulo', 'profesor_id', string='Módulos que imparte')