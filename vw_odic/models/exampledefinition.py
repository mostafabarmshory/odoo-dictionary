from odoo import models, fields


class ExampleDefinition(models.Model):
    _name = "vw_odic.exampledefinition"
    _description = "A list of statements of the exact meaning of a word"
    _rec_name = 'text'

    text = fields.Char(size=1024, trim=True, translate=False, required=True)

    example_id = fields.Many2one(
        ondelete='cascade',
        required=True,
        comodel_name='vw_odic.example',
        help="Related examples")

