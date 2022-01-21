from odoo import models, fields


class Pronunciation(models.Model):
    
    # TODO: 2022, Masood: Missed fields
    # - dialects
    # - registers
    
    _name = "vw_odic.pronunciation"
    _description = "A grouping of pronunciation information."
    _rec_name = 'phoneticNotation'
    
    audioFile = fields.Binary(
        required=False,
        help="The audio file of pronunciation")
    
    phoneticNotation = fields.Char(
        string='Phonetic Notation', 
        size=256, 
        trim=True, 
        translate=False, 
        required=False,
        help="The alphabetic system used to display the phonetic spelling")
    
    # Phonetic spelling is the representation of vocal sounds which express pronunciations of words.
    # It is a system of spelling in which each letter represents invariably the same spoken sound
    phoneticSpelling = fields.Char(
        string='Phonetic Spelling', 
        size=256, trim=True, 
        translate=False, 
        required=False)
    regions_ids = fields.Many2many(
        string='Regions', 
        comodel_name='vw_odic.region')
    


