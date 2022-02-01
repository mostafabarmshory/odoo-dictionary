from odoo import models, fields


class Picture(models.Model):
    
    # TODO: 2022, Maso: see pronunciation for more attrs
    
    _name = "vw_odic.headwordpicture"
    _description = "A grouping of picture information."
    _rec_name = 'text'
    _inherit = 'image.mixin'
    
    
    # picture = fields.Image(
    #     required=False,
    #     help="The picture file")
    
    text = fields.Char(
        string='Text', 
        size=1024, 
        trim=True, 
        translate=False, 
        required=False,
        help="A text to describe the image")
    
    regions_ids = fields.Many2many(
        string='Regions', 
        comodel_name='vw_odic.region')


