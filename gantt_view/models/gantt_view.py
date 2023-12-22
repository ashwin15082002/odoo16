# -*- coding: utf-8 -*-

from odoo import api, fields, models


class TipsTricks(models.Model):
    _name = 'tips.tricks'
    _rec_name = 'name'
    _inherit = ['mail.thread']

    name = fields.Char("Name")
    check = fields.Boolean("Active", default=False)
    partner_id = fields.Many2one('res.partner', 'Partner')
    number = fields.Integer(string="Value", default=0)
    date_deadline = fields.Date(string='Deadline', index=True, copy=False)
    date_start = fields.Date(string='Start date', index=True, copy=False)
