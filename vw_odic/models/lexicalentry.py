from odoo import models, fields

class LexicalEntry(models.Model):
    #TODO: 2022, maso: Missed field
    # - compounds           (ArrayOfRelatedEntries, optional): 
    # - grammaticalFeatures (GrammaticalFeaturesList, optional),
    # - notes               (CategorizedTextList, optional),
    # - phrasalVerbs        (ArrayOfRelatedEntries, optional): Other words from which their Sense derives ,
    # - phrases             (ArrayOfRelatedEntries, optional): Other words from which their Sense derives ,
    # - pronunciations      (PronunciationsList, optional),
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
    text = fields.Text(trim=True, translate=False, required=True)
    
    headwordentry_id = fields.Many2one(ondelete='cascade', comodel_name='vw_odic.headwordentry')
    lexicalCategory_id = fields.Many2one(ondelete='set null', comodel_name='vw_odic.lexicalcategory')
    # (ArrayOfRelatedEntries, optional): Other words from which this one derives ,
    derivativeOf_ids = fields.One2many(comodel_name='vw_odic.derivativeof', inverse_name='lexicalEntry_id')
    # (ArrayOfRelatedEntries, optional): Other words from which their Sense derives ,
    derivatives_ids = fields.One2many(comodel_name='vw_odic.derivative', inverse_name='lexicalEntry_id')
