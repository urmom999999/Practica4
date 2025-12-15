# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente del hospital'
    _rec_name = 'nombre_completo'
    
    # Campos del paciente
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    nombre_completo = fields.Char(
        'Nombre completo',
        compute='_compute_nombre_completo',
        store=True
    )
    sintomas = fields.Text('Síntomas')
    edad = fields.Integer('Edad')
    telefono = fields.Char('Teléfono')
    email = fields.Char('Email')
    historial_consultas = fields.Text('Historial médico', readonly=True)
    
    # Relaciones
    consulta_ids = fields.One2many(
        'hospital.consulta',
        'paciente_id',
        string='Consultas'
    )
    
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
    
    _sql_constraints = [
        ('email_uniq', 'UNIQUE(email)', 'El email debe ser único'),
    ]

class Medico(models.Model):
    _name = 'hospital.medico'
    _description = 'Médico del hospital'
    _rec_name = 'nombre_completo'
    
    # Campos del médico
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    nombre_completo = fields.Char(
        'Nombre completo',
        compute='_compute_nombre_completo',
        store=True
    )
    numero_colegiado = fields.Char(
        'Número de colegiado',
        required=True,
        index=True
    )
    especialidad = fields.Selection([
        ('general', 'Medicina General'),
        ('pediatria', 'Pediatría'),
        ('cardiologia', 'Cardiología'),
        ('traumatologia', 'Traumatología'),
        ('neurologia', 'Neurología'),
        ('dermatologia', 'Dermatología'),
        ('otros', 'Otros'),
    ], string='Especialidad', default='general')
    telefono = fields.Char('Teléfono')
    email = fields.Char('Email')
    activo = fields.Boolean('Activo', default=True)
    
    # Relaciones
    consulta_ids = fields.One2many(
        'hospital.consulta',
        'medico_id',
        string='Consultas realizadas'
    )
    
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
    
    _sql_constraints = [
        ('numero_colegiado_uniq', 'UNIQUE(numero_colegiado)', 
         'El número de colegiado debe ser único'),
    ]

class Consulta(models.Model):
    _name = 'hospital.consulta'
    _description = 'Consulta médica'
    _order = 'fecha_consulta desc'
    
    # Campos de la consulta
    paciente_id = fields.Many2one(
        'hospital.paciente',
        string='Paciente',
        required=True,
        ondelete='cascade'
    )
    medico_id = fields.Many2one(
        'hospital.medico',
        string='Médico',
        required=True,
        domain="[('activo', '=', True)]"
    )
    fecha_consulta = fields.Datetime(
        'Fecha y hora de consulta',
        default=lambda self: fields.Datetime.now(),
        required=True
    )
    diagnostico = fields.Html('Diagnóstico', sanitize=True)
    tratamiento = fields.Text('Tratamiento prescrito')
    observaciones = fields.Text('Observaciones adicionales')
    urgente = fields.Boolean('Consulta urgente', default=False)
    estado = fields.Selection([
        ('programada', 'Programada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='programada')
    
    # Campos calculados
    paciente_nombre = fields.Char(
        'Nombre paciente',
        related='paciente_id.nombre_completo',
        store=True
    )
    medico_nombre = fields.Char(
        'Nombre médico',
        related='medico_id.nombre_completo',
        store=True
    )
    
    @api.constrains('fecha_consulta')
    def _check_fecha_consulta(self):
        for record in self:
            if record.fecha_consulta and record.fecha_consulta < fields.Datetime.now():
                raise ValidationError('La fecha de consulta no puede ser en el pasado')