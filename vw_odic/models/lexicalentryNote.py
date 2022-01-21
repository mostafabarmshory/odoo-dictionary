from odoo import models, fields


class LexicalEntryNote(models.Model):
    _name = "vw_odic.lexicalentrynote"
    _description = "Notes related to words."
    _inherit =["vw_odic.abstractnote"]
    
    lexicalEntry_id = fields.Many2one(
        ondelete='cascade', 
        required=True,
        comodel_name='vw_odic.lexicalentry',
        help="Related lexical entry")

