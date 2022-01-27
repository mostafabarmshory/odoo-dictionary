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
        "web",
        "mail",
        "portal",
        "rating"
    ],
    "data": [
        "data/ir.model.access.csv",
        
        # Basic views 
        "views/dashboard.xml",
        "views/region.xml",
        "views/domain.xml",
        "views/notetypes.xml",
        "views/lexicalcategory.xml",
        
        "views/headwordentry.xml",
        "views/lexicalentery.xml",
        "views/lexicalentryNote.xml",
        "views/pronunciation.xml",
        "views/derivative.xml",
        "views/entry.xml",
        "views/etymology.xml",
        "views/sense.xml",
        "views/definition.xml",
        "views/example.xml",
        "views/dictionary.xml",

    ],
    'auto_install': False,
    'installable': True,
    'application': True,
    'images': [
        'static/description/assets/img/main_screenshot.jpg'
    ]
}
