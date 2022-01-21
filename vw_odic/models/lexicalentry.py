from odoo import models, fields

class LexicalEntry(models.Model):
    #TODO: 2022, maso: Missed field
    # - compounds           (ArrayOfRelatedEntries, optional): 
    # - grammaticalFeatures (GrammaticalFeaturesList, optional),
    # - variantForms        (VariantFormsList, optional): Various words that are used interchangeably depending on the context, e.g 'a' and 'an'
    _name = "vw_odic.lexicalentry"
    _description = "Group of lexicalEntries related to a specific result for a given word ID."
    # TOOD: 2022, maso: check the field _date_name 
    _inherit = [
        'portal.mixin', 
        'mail.thread.cc', 
        'mail.activity.mixin', 
        'rating.mixin'
    ]
    _mail_post_access = 'read'
    _order = "language desc, id desc"
    _check_company_auto = True
    _rec_name = 'text'
    
    # IANA language code
    language = fields.Char(size=8, trim=True, translate=False, required=True)
    
    # Abstract root form from which this lexicalEntry is derived
    root = fields.Char(size=1024, trim=True, translate=False, required=False)
    
    # A given written or spoken realisation of an entry
    text = fields.Text(
        translate=False,
        required=True)
    
    headwordentry_id = fields.Many2one(ondelete='cascade', comodel_name='vw_odic.headwordentry')
    lexicalCategory_id = fields.Many2one(ondelete='set null', comodel_name='vw_odic.lexicalcategory')
    derivativeOf_ids = fields.One2many(
        comodel_name='vw_odic.derivativeof', 
        inverse_name='lexicalEntry_id',
        help="Other words from which this one derives")
    derivatives_ids = fields.One2many(
        comodel_name='vw_odic.derivative', 
        inverse_name='lexicalEntry_id',
        help="Other words from which their Sense derives")
    phrases_ids = fields.Many2many(
        comodel_name="vw_odic.headwordentry", 
        relation="vw_odic_lexicalentry_phrases",
        string="Phrases",
        help="Other words from which their Sense derives")
    phrasalVerbs_ids = fields.Many2many(
        comodel_name="vw_odic.headwordentry",
        relation="vw_odic_lexicalentry_phrasalverbs",
        string="Phrasal Verbs",
        help="Other words from which their Sense derives")
    pronunciations_ids = fields.Many2many(
        comodel_name='vw_odic.pronunciation',
        string='Pronunciations',
        help="Other words from which their Sense derives")
    notes_ids = fields.One2many(
        comodel_name='vw_odic.lexicalentrynote',
        inverse_name='lexicalEntry_id',
        string='Notes',
        help="Notes related to the lexical entry")
    entries_ids = fields.One2many(
        comodel_name="vw_odic.entry",
        inverse_name='lexicalEntry_id',
        string='Entries',
        help="")
