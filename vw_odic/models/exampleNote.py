from odoo import models, fields


class ExampleNote(models.Model):
    _name = "vw_odic.examplenote"
    _description = "Notes related to examples."
    _inherit =["vw_odic.abstractnote"]

    example_id = fields.Many2one(
        ondelete='cascade', 
        required=True,
        comodel_name='vw_odic.example',
        help="Related example")

