# -*- coding: utf-8 -*-

from odoo import fields, models


class WorkReport(models.Model):
    _name = 'work.report'
    _description = 'Work Report Tracker'

    name = fields.Char(string='Employee', help='Employee Name')
    employee_email = fields.Char(string='Email', help='Employee Email')
    email_subject = fields.Char(string='Subject', help='Email Subject')
    date = fields.Date(string='Date', help='Work Report Date')
    work_report = fields.Html(string='Email Content', help='Work Report Body')
