from odoo import models, fields


class Example(models.Model):
    _name = "vw_odic.example"
    _description = "A list of written or spoken words"
    _rec_name = 'text'

    text = fields.Char(size=1024, trim=True, translate=False, required=True)


