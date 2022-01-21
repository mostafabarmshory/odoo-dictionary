from odoo import models, fields


class NoteType(models.Model):
    _name = "vw_odic.notetype"
    _description = "A name to categorize notes."
    name = fields.Char(size=256,
        trim=True,
        translate=False,
        required=True)


class AbstractNote(models.AbstractModel):
    """
    A general note to display in web and applications.
    """
    _name = "vw_odic.abstractnote"
    _description = "Related entry to words."
    _rec_name = 'text'
    
    text = fields.Text(
        required=True,
        help="A note text")
    type_id = fields.Many2one(
        comodel_name="vw_odic.notetype",
        required=True,
        help="The descriptive category of the text")
