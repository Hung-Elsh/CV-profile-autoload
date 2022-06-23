# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class viin_to_cv_profile_autoload(models.Model):
#     _name = 'viin_to_cv_profile_autoload.viin_to_cv_profile_autoload'
#     _description = 'viin_to_cv_profile_autoload.viin_to_cv_profile_autoload'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
