
from odoo import models, fields


class Example(models.Model):
    _name = "vw_odic.example"
    _description = "This is a table contains all examples of all dictionaries"

    value = fields.Text()
    translation = fields.Text()
    
    word_id = fields.Many2one("vw_odic.word", string="Word")
    tag_ids = fields.Many2many("vw_odic.tag", string="Tag")
    