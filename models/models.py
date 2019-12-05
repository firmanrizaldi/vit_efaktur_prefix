
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class invoiceprevix(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    
    prefix_berikat_id = fields.Many2one(
        string='Prefix NSFP',
        comodel_name='prefix.nsfp',
    )
    

class invoice(models.Model):
    _name = 'prefix.nsfp'
    _rec_name = 'prefix_berikat'

    prefix_berikat = fields.Char(
        string='Prefix NSFP',
    )
    

    # prefix_berikat_ids = fields.One2many(
    #     string='Prefix NSFP',
    #     comodel_name='account.invoice',
    #     inverse_name='prefix_berikat_id',
    # )
    


    



