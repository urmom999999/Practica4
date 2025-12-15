# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente'
    
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    sintomas = fields.Text(string="Síntomas")
    
    # Relación con consultas
    consulta_ids = fields.One2many('hospital.consulta', 'paciente_id', string="Consultas")

class HospitalMedico(models.Model):
    _name = 'hospital.medico'
    _description = 'Médico'
    
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    numero_colegiado = fields.Char(string="Número de colegiado", required=True)
    
    # Relación con consultas
    consulta_ids = fields.One2many('hospital.consulta', 'medico_id', string="Consultas")

class HospitalConsulta(models.Model):
    _name = 'hospital.consulta'
    _description = 'Consulta'
    
    paciente_id = fields.Many2one('hospital.paciente', string="Paciente", required=True)
    medico_id = fields.Many2one('hospital.medico', string="Médico", required=True)
    diagnostico = fields.Text(string="Diagnóstico", required=True)
    fecha_consulta = fields.Datetime(string="Fecha de consulta", default=fields.Datetime.now)
    
    # Campos relacionados (opcionales para mostrar en vistas)
    paciente_nombre = fields.Char(related='paciente_id.nombre', store=True, string="Nombre Paciente")
    medico_nombre = fields.Char(related='medico_id.nombre', store=True, string="Nombre Médico")