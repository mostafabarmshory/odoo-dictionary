from odoo import models, fields


class Pronunciation(models.Model):

    # TODO: 2022, Masood: Missed fields
    # - dialects
    # - regions
    # - registers

    _name = "vw_odic.pronunciation"
    _description = "A grouping of pronunciation information."

    # The audio file of pronunciation
    audioFile = fields.Binary(required=False)

    # The alphabetic system used to display the phonetic spelling
    phoneticNotation = fields.Char(string='Phonetic Notation', size=256, trim=True, translate=False, required=False)

    # Phonetic spelling is the representation of vocal sounds which express pronunciations of words.
    # It is a system of spelling in which each letter represents invariably the same spoken sound
    phoneticSpelling = fields.Char(string='Phonetic Spelling', size=256, trim=True, translate=False, required=False)

    headwordentry_id = fields.Many2one(ondelete='cascade', comodel_name='vw_odic.headwordentry')
    regions_ids = fields.Many2many(string='Regions', comodel_name='vw_odic.region', _req_name='text')



