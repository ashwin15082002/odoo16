# -*- coding: utf-8 -*-

from odoo import fields, models


class AverageLandedCost(models.Model):
    """ This models gives the fields to stock landed cost """
    _name = 'average.landed.cost'
    _description = 'Average Landed Cost'

    product_id = fields.Many2one('product.product', string='Product',
                                 help='Select Product')
    average_landed_cost = fields.Float(string='Average Landed Cost',
                                       help='Automatically calculate Average landed cost')
    landed_cost_id = fields.Many2one('stock.landed.cost', string='landed_cost',
                                     help='Landed Cost ID')
