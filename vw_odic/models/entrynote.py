from odoo import models, fields


class EntryNote(models.Model):
    _name = "vw_odic.entrynote"
    _description = "Notes related to entry."
    _inherit =["vw_odic.abstractnote"]
    
    entry_id = fields.Many2one(
        ondelete='cascade', 
        required=True,
        comodel_name='vw_odic.entry',
        help="Related entry")

