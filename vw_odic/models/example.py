from odoo import models, fields


class Example(models.Model):
    # TODO: Masood, 2022: Missed fields
    # - notes
    # - registers
    # - senseIds

    _name = "vw_odic.example"
    _description = "A list of written or spoken rendering of examples of use of a word or text"
    _rec_name = 'text'
    _inherit = [
        'portal.mixin',
        'mail.thread.cc',
        'mail.activity.mixin',
        'rating.mixin'
    ]

    text = fields.Char(size=1024, trim=True, translate=False, required=True)
    notes_ids = fields.One2many(
        comodel_name='vw_odic.examplenote',
        inverse_name='example_id',
        string='Notes',
        help="Notes related to the example")
    definitions_ids = fields.One2many(
        comodel_name='vw_odic.exampledefinition',
        help="Related definitions",
        inverse_name='example_id')
    domains_ids = fields.Many2many(
        comodel_name='vw_odic.domain',
        help="Related domains")
    regions_ids = fields.Many2many(
        comodel_name='vw_odic.region',
        help="Related regions")
    registers_ids = fields.Many2many(
        comodel_name='vw_odic.register',
        help="Related registers")
    senses_ids = fields.Many2many(
        comodel_name='vw_odic.sense',
        relation="vw_odic_example_sense",
        column1="example_id",
        column2="sense_id",
        string='Senses',
        help="Related senses")

