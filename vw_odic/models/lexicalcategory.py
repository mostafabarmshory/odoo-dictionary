from odoo import models, fields


class LexicalCategory(models.Model):
    _name = "vw_odic.lexicalcategory"
    _description = "The category of a lexical entry."

    text = fields.Char(size=256, trim=True, translate=False, required=True)

