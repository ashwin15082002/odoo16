# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.fields import Date


class WorkReport(models.Model):
    """ This model is used for tracking daily work report of employees """
    _name = 'work.report'
    _description = 'Work Report Tracker'

    name = fields.Char(string='Employee', help='Employee Name')
    employee_email = fields.Char(string='Email', help='Employee Email')
    email_subject = fields.Char(string='Subject', help='Email Subject')
    date = fields.Date(string='Date', help='Work Report Date')
    work_report = fields.Html(string='Email Content', help='Work Report Body')

    @api.model
    def get_datas(self, filter):
        """ This function is called from work_report.js file for getting data for reporting."""
        if filter == 'Date':
            res = self.get_date_data()
            return res
        else:
            res = self.get_employee_data()
            return res

    def get_date_data(self):
        """ if the filter is date then this function works and return data"""
        work_reports = self.search([('date', '=', Date.today())])
        data_x = list(set(work_reports.mapped('name')))
        data_y = []
        for i in data_x:
            count = len(work_reports.filtered(lambda x: x.name == i))
            data_y.append(count)

        return {
            'data_x': data_x,
            'data_y': data_y,
        }

    def get_employee_data(self):
        """ if the filter is employee then this function works and return data """
        work_reports = self.search([])
        data_x = list(set(work_reports.mapped('name')))
        data_y = []
        for i in data_x:
            count = len(work_reports.filtered(lambda x: x.name == i))
            data_y.append(count)
        return {
            'data_x': data_x,
            'data_y': data_y,
        }
