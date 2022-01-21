from odoo import models, fields


class AbstractDerivative(models.AbstractModel):
    """ Abstract implementation of Derivative
    
    Derivative is used as two roles. They are the same in implementation but
    with different usage.
    """
    _name = "vw_odic.abstractderivative"
    _description = "Related entry to words."
    _rec_name = 'text'
    
    text = fields.Char(size=512, trim=True, translate=False, required=True)
    language = fields.Char(size=8, trim=True, translate=False, required=True)
    regions_ids = fields.Many2many(string='Regions', comodel_name='vw_odic.region')
    lexicalEntry_id = fields.Many2one(ondelete='cascade', comodel_name='vw_odic.lexicalentry')
    domains_ids = fields.Many2many(string='Domains', comodel_name='vw_odic.domain')


class DerivativeOf(models.Model):
    _name = "vw_odic.derivativeof"
    _inherit = ["vw_odic.abstractderivative"]


class Derivative(models.Model):
    _name = "vw_odic.derivative"
    _inherit = ["vw_odic.abstractderivative"]
