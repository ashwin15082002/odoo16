# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AverageLandedCost(models.Model):
    _name = 'average.landed.cost'

    product_id = fields.Many2one('product.product', string='Product')
    average_landed_cost = fields.Float(string='Average Landed Cost')
    landed_cost_id = fields.Many2one('stock.landed.cost', string='landed_cost')


