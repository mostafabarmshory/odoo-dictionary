{
    "name": "Dictionary",
    "summary": "An Odoo dictionary app to build a dictionary and manage it",
    "author": "ViraWeb123",
    "website": "https://viraweb123.ir",
    "license": "AGPL-3",
    "category": "Dictionary",
    "version": "14.0.1.0.0",
    "depends": [
        "base",
        "web"
    ],
    "data": [
        "data/ir.model.access.csv",
        
        "views/dashboard.xml",
        "views/dictionary.xml",
        "views/word.xml",
        "views/tag.xml"
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
    'images': [
        'static/description/assets/img/main_screenshot.jpg'
    ]
}
