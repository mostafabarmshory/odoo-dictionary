from odoo import models, fields


class Domain(models.Model):
    _name = "vw_odic.domain"
    _description = "A subject, discipline, or branch of knowledge particular to the Sense"
    _rec_name = 'text'

    text = fields.Char(size=256, trim=True, translate=False, required=True)