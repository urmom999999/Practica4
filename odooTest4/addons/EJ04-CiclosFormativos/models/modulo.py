from odoo import models, fields

class Modulo(models.Model):
    _name = 'modulo'
    _description = 'Módulo'
    
    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código', required=True)
    horas = fields.Integer(string='Horas totales')
    ciclo_id = fields.Many2one('ciclo.formativo', string='Ciclo Formativo')
    profesor_id = fields.Many2one('profesor', string='Profesor')
    alumno_ids = fields.Many2many('alumno', string='Alumnos matriculados')