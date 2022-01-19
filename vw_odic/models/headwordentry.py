from odoo import models, fields

class HeadwordEntry(models.Model):
    #TODO: 2022, Masood: Missed field
    # - lexicalEntries
    _name = "vw_odic.headwordentry"
    _description = "Group of lexicalEntries related to a specific result for a given word ID."

    word = fields.Char(size=1024, trim=True, translate=False, required=True)
    language = fields.Char(size=8, trim=True, translate=False, required=True)
    type = fields.Selection([
        ('headword', 'Headword'),
        ('inflection', 'Inflection'),
        ('phrase', 'Phrase')
    ])
    pronunciations_ids = fields.One2many(comodel_name='vw_odic.pronunciation', inverse_name='headwordentry_id')
