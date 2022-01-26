from odoo import models, fields


class Sense(models.Model):

    # TODO: 2022, Masood: Missed field
    # - shortDefinitions
    # - thesaurusLinks
    # - notes
    # - constructions
    # - crossReferenceMarkers
    # - crossReferences
    # - domainClasses
    # - domains
    # - etymologies
    # - pronunciations
    # - regions
    # - registers
    # - semanticClasses
    # - variantForms

    # - subsenses

    _name = "vw_odic.sense"
    _description = "Complete list of senses for bilingual entries"
    _inherit = [
        'portal.mixin',
        'mail.thread.cc',
        'mail.activity.mixin',
        'rating.mixin'
    ]

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
        relation="vw_odic_example_sense",
        column1="sense_id",
        column2="example_id",
        string='Examples',
        help="Related examples")
    synonyms_ids = fields.Many2many(
        comodel_name="vw_odic.headwordentry",
        relation="vw_odic_headwordsense_synonyms",
        string="Synonyms",
        help="Synonyms of word")
    antonyms_ids = fields.Many2many(
        comodel_name="vw_odic.headwordentry",
        relation="vw_odic_headwordsense_antonyms",
        string="Antonyms",
        help="Antonyms of word")
    inflections_ids = fields.Many2many(
        string='Inflections',
        comodel_name='vw_odic.headwordentry',
        help="A list of inflected forms for a word.")

    


