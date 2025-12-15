from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class BibliotecaComic(models.Model):
    _name = 'biblioteca.comic'
    _description = 'Comic'
    
    nombre = fields.Char(string="Título", required=True)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado')
    ], string="Estado", default='borrador')
    paginas = fields.Integer(string="Número de páginas")
    activo = fields.Boolean(string="Activo", default=True)
    autor_ids = fields.Many2many('biblioteca.autor', string="Autores")
    
    def archivar(self):
        self.write({'activo': False, 'estado': 'archivado'})

class BibliotecaAutor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'Autor'
    
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio'
    
    identificador = fields.Char(string="ID Socio", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)

class BibliotecaEjemplar(models.Model):
    _name = 'biblioteca.ejemplar'
    _description = 'Ejemplar'
    
    comic_id = fields.Many2one('biblioteca.comic', string="Cómic", required=True)
    codigo = fields.Char(string="Código ejemplar", required=True)
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
    ], string="Estado", default='disponible')
  
    socio_id = fields.Many2one('biblioteca.socio', string="Prestado a")
    fecha_prestamo = fields.Date(string="Fecha préstamo")
    fecha_devolucion = fields.Date(string="Fecha devolución")
    
    @api.constrains('fecha_prestamo')
    def _check_fecha_prestamo(self):
        hoy = date.today()
        for ejemplar in self:
            if ejemplar.fecha_prestamo and ejemplar.fecha_prestamo > hoy:
                raise ValidationError(_("Error!! Fecha no puede ser posterior a entrega."))
    
    @api.constrains('fecha_devolucion')
    def _check_fecha_devolucion(self):
        hoy = date.today()
        for ejemplar in self:
            if ejemplar.fecha_devolucion and ejemplar.fecha_devolucion < hoy:
                raise ValidationError(_("Error! No se puede devolver en una fecha anterior a hoy"))