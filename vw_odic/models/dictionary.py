from odoo import models, fields


class Dictionary(models.Model):
    _name = "vw_odic.dictionary"
    _description = "List of different dictionaries"
    _rec_name = 'code'

    code = fields.Char(size=128, trim=True, translate=False, required=True)
    title = fields.Char(size=128, trim=True, translate=False, required=True)
    description = fields.Char(size=256, trim=True, translate=False, required=True)

    headwordentries_ids = fields.One2many(
        inverse_name='dictionary_id',
        required=True,
        comodel_name='vw_odic.headwordentry',
        help="Related headwords")
