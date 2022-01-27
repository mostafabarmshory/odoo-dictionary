from odoo import models, fields


class HeadwordEntry(models.Model):

    # TODO: 2022, Masood: Missed field
    # - lexicalEntries
    _name = "vw_odic.headwordentry"
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
    _rec_name = 'word'

    word = fields.Char(size=1024, trim=True, translate=False, required=True)
    language = fields.Char(size=1024, trim=True, translate=False, required=True)
    type = fields.Selection([
        ('headword', 'Headword'),
        ('inflection', 'Inflection'),
        ('phrase', 'Phrase')
    ])
    pronunciations_ids = fields.Many2many(
        comodel_name='vw_odic.pronunciation',
        relation="vw_odic_headwordpronunciation",
        string='Pronunciations',
        help="Other words from which their Sense derives")
    pictures_ids = fields.Many2many(
        comodel_name='vw_odic.picture',
        relation="vw_odic_hwentry_picture",
        string='Pictures',
        help="Related pictures to the headword")
    lexicalEntries_ids = fields.One2many(
        comodel_name='vw_odic.lexicalentry', 
        inverse_name='headwordentry_id')
