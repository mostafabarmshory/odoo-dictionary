from odoo import models, fields


class Rigion(models.Model):
    _name = "vw_odic.region"
    _description = "Group of lexicalEntries related to a specific result for a given word ID."

    text = fields.Char(size=1024, trim=True, translate=False, required=True)

