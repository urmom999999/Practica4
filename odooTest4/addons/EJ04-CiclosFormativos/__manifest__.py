{
    'name': 'Gestión de Ciclos Formativos',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestión de ciclos formativos, módulos, alumnos y profesores',
    'description': 'Módulo para gestionar ciclos formativos en un instituto',
    'author': 'Tu Nombre',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}