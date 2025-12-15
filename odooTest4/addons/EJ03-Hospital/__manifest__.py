# -*- coding: utf-8 -*-
{
    'name': "Gestión Hospital",
    'summary': "Gestion pacientes, médicos y consultas",
    'description': "Modulo gestion hospital",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_views.xml',
    ],
    'installable': True,
    'application': True,
}