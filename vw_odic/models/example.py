from odoo import models, fields


class Example(models.Model):
    _name = "vw_odic.example"
    _description = "A list of written or spoken rendering of examples of use of a word or text"
    _rec_name = 'text'

    text = fields.Char(size=1024, trim=True, translate=False, required=True)


