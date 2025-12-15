# -*- coding: utf-8 -*-
{
    'name': "Gestion Hospital",
    'summary': "Gestión de pacientes, médicos y consultas hospitalarias",
    'description': """
        Módulo para gestionar pacientes, médicos y consultas de un hospital.
        Funcionalidades:
        - Registro de pacientes y sus síntomas
        - Registro de médicos con número de colegiado
        - Control de consultas médicas con diagnóstico
    """,
    'application': True,
    'author': "Tu Nombre",
    'website': "http://tu-sitio.com",
    'category': 'Salud',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menu.xml',
        'views/paciente_views.xml',
        'views/medico_views.xml',
        'views/consulta_views.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}