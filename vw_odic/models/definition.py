from odoo import models, fields


class SenseDefinition(models.Model):
    _name = "vw_odic.sensedefinition"
    _description = "A list of written or spoken words"
    _rec_name = 'text'

    text = fields.Char(size=1024, trim=True, translate=False, required=True)

    sense_id = fields.Many2one(
        ondelete='cascade',
        required=True,
        comodel_name='vw_odic.sense',
        help="Related sense")

