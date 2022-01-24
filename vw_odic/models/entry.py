from odoo import models, fields


class Entry(models.Model):
    # Note: maso, 2022: uncoverd attributes.
    #
    # A grouping of crossreference notes.
    # crossReferenceMarkers:
    #    
    # crossReferences:
    #
    # grammaticalFeatures:
    #
    # A list of inflected forms for an Entry.
    # inflections:
    #
    # senses
    #  Complete list of senses
    #
    # Various words that are used interchangeably depending on the context, e.g 'a' and 'an'
    # variantForms:
    _name = "vw_odic.entry"
    _description = "Group of domain related to words."
    _rec_name = 'homographNumber'
    
    homographNumber = fields.Char(
        size=512,
        trim=True,
        translate=False,
        required=False,
        help="Identifies the homograph grouping. The last two digits identify different entries of the same homograph. The first one/two digits identify the homograph number.")
    lexicalEntry_id = fields.Many2one(
        ondelete='cascade', 
        required=True,
        comodel_name='vw_odic.lexicalentry',
        help="Related lexical entry")
    pronunciations_ids = fields.Many2many(
        comodel_name='vw_odic.pronunciation',
        string='Pronunciations',
        help="Other words from which their Sense derives")
    notes_ids = fields.One2many(
        comodel_name='vw_odic.entrynote',
        inverse_name='entry_id',
        string='Notes',
        help="Notes related to the entry")
    etymologies_ids = fields.One2many(
        comodel_name="vw_odic.etymology",
        inverse_name='entry_id',
        string='Etymologies',
        help="The origin of the word and the way in which its meaning has changed throughout history")
    inflections_ids = fields.Many2many(
        string='Inflections',
        comodel_name='vw_odic.headwordentry',
        help="A list of inflected forms for an Entry.")
    senses_ids = fields.One2many(
        comodel_name='vw_odic.sense',
        inverse_name='entry_id',
        string='Senses',
        help="Complete list of senses for bilingual entries")
