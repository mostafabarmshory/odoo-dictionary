from odoo import models, fields


class Dictionary(models.Model):
    _name = "vw_odic.dictionary"
    _description = "List of different dictionaries"
    _rec_name = 'text'

    text = fields.Char(size=128, trim=True, translate=False, required=True)
