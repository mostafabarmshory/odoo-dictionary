from odoo import models, fields

class Tag(models.Model):
    _name = "vw_odic.tag"
    _description = "You can add tag to word, dictionary and example. "
    
    name = fields.Char(required = True)
    description = fields.Text(required = False)

