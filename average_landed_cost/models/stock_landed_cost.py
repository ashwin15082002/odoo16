# -*- coding: utf-8 -*-

from odoo import fields, models


class LandedCost(models.Model):
    """ Inherits the model stock landed cost add a tree view in the form and
        while clicking the validate button changes the product cost"""
    _inherit = 'stock.landed.cost'

    landed_cost_ids = fields.One2many('average.landed.cost',
                                      'landed_cost_id',
                                      string='Average Landed')

    def compute_landed_cost(self):
        self.landed_cost_ids.unlink()
        super().compute_landed_cost()
        values = []
        for lines in self.valuation_adjustment_lines:
            values.append({'product_id': lines.product_id.id,
                           'average_landed_cost': lines.additional_landed_cost / lines.quantity})
        res = {}
        for i in values:
            product_id = i['product_id']
            average_landed_cost = i['average_landed_cost']

            if product_id in res:
                res[product_id] += average_landed_cost
            else:
                res[product_id] = average_landed_cost

        result = [{'product_id': key, 'average_landed_cost': value,
                   'landed_cost_id': self.cost_lines.cost_id.id}
                  for key, value in res.items()]

        self.env['average.landed.cost'].create(result)
