from odoo import models, fields


class Sense(models.Model):

    # TODO: 2022, Masood: Missed field
    # - shortDefinitions
    # - thesaurusLinks
    # - notes
    # - constructions

    _name = "vw_odic.sense"
    _description = "Complete list of senses for bilingual entries"

    entry_id = fields.Many2one(
        ondelete='cascade',
        required=True,
        comodel_name='vw_odic.entry',
        help="Related entry")
    definitions_ids = fields.One2many(
        inverse_name='sense_id',
        required=True,
        comodel_name='vw_odic.sensedefinition',
        help="Related definition")
    examples_ids = fields.Many2many(
        comodel_name='vw_odic.example',
        help="Related examples")
    synonyms_ids = fields.Many2many(
        comodel_name="vw_odic.headwordentry",
        relation="vw_odic_headwordsense_synonyms",
        string="Synonyms",
        help="Synonyms of word")

    


