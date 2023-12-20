# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.fields import Date


class WorkReport(models.Model):
    _name = 'work.report'
    _description = 'Work Report Tracker'

    name = fields.Char(string='Name')
    email_header = fields.Char(string='Email Header')
    date = fields.Date(string='Date', default=Date.today())
    email_body = fields.Html(string='Email Content')

