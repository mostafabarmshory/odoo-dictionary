
from odoo import models, fields


class Dictionary(models.Model):
    _name = "vw_odic.dictionary"
    _description = "This is a table contains list of dictionaries"
    
    name = fields.Char(required = true)
    description = fields.Text(required = false)

