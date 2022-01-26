from odoo import models, fields


class Register(models.Model):
    _name = "vw_odic.register"
    _description = "A level of language usage, typically with respect to formality. e.g. 'offensive', 'informal'"
    _rec_name = 'text'

    text = fields.Char(size=256, trim=True, translate=False, required=True)

