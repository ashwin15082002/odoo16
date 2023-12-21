# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import api, models


class MailThread(models.AbstractModel):
    """ Inheriting mail.thread for getting datas from incoming mail """
    _inherit = 'mail.thread'

    @api.model
    def message_parse(self, message, save_original=False):
        res = super().message_parse(message, save_original)

        # ---------------------email------------------------
        email_from = res['from'].split('<')[1]
        email = email_from.split('>')[0]
        employee = self.env['hr.employee'].search([('work_email', '=', email)])

        # ---------------------date------------------------

        email_date = res['subject'].split('_')[1]
        date = email_date.split('_')[0]
        date_time = datetime.strptime(date, '%d %b %Y')
        formatted_date = date_time.strftime('%Y-%m-%d')
        if employee:
            data = {'name': employee.name,
                    'employee_email': email,
                    'email_subject': res['subject'],
                    'work_report': res['body'],
                    'date': formatted_date,
                    }
            self.env['work.report'].create(data)

        return res
