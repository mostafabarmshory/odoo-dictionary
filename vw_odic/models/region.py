from odoo import models, fields


class Region(models.Model):
    _name = "vw_odic.region"
    _description = "Group of regions related to words."

    text = fields.Char(size=256, trim=True, translate=False, required=True)

