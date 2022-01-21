from odoo import models, fields


class Etymology(models.Model):
    _name = "vw_odic.etymology"
    _description = "Group of regions related to words."
    _rec_name = 'text'
    
    text = fields.Text(
        translate=False, 
        required=True,
        help="The origin of the word and the way in which its meaning has changed throughout history")
    entry_id = fields.Many2one(
        ondelete='cascade', 
        required=True,
        comodel_name='vw_odic.entry',
        help="Related entry")
