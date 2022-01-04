
from odoo import models, fields


class Word(models.Model):
    _name = "vw_odic.word"
    _description = "This is a table contains all words of all dictionaries"
    
    name = fields.Char(required = True)
    
    dictionary_id = fields.Many2one("vw_odic.dictionary", string="Dictionary")