# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import api, fields, models
from odoo.fields import Date


class WorkReport(models.Model):
    _name = 'work.report'
    _description = 'Work Report Tracker'

    name = fields.Char(string='Employee', help='Employee Name')
    employee_email = fields.Char(string='Email', help='Employee Email')
    email_subject = fields.Char(string='Subject', help='Email Subject')
    date = fields.Date(string='Date', help='Work Report Date')
    work_report = fields.Html(string='Email Content', help='Work Report Body')

    @api.model
    def get_datas(self, date_count):
        if date_count == '30':
            start_date = Date.today() - timedelta(days=30)
        else:
            start_date = Date.today() - timedelta(days=7)

        work_reports = self.search([('date', '>', start_date)])
        data_x = list(set(work_reports.mapped('name')))
        data_y = []
        for i in data_x:
            count = len(work_reports.filtered(lambda x: x.name == i))
            data_y.append(count)

        return {
            'data_x': data_x,
            'data_y': data_y,
        }
