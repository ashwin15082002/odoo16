# -*- coding: utf-8 -*-

from odoo import api, fields, models


class LandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    landed_cost_ids = fields.One2many('average.landed.cost',
                                      'landed_cost_id',
                                      string='Average Landed')
