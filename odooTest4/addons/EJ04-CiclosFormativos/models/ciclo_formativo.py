from odoo import models, fields

class CicloFormativo(models.Model):
    _name = 'ciclo.formativo'
    _description = 'Ciclo Formativo'
    
    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código', required=True)
    descripcion = fields.Text(string='Descripción')
    modulo_ids = fields.One2many('modulo', 'ciclo_id', string='Módulos')