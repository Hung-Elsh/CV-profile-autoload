# -*- coding: utf-8 -*-
# from odoo import http


# class ViinToCvAutoload(http.Controller):
#     @http.route('/viin_to_cv_profile_autoload/viin_to_cv_profile_autoload/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viin_to_cv_profile_autoload/viin_to_cv_profile_autoload/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viin_to_cv_profile_autoload.listing', {
#             'root': '/viin_to_cv_profile_autoload/viin_to_cv_profile_autoload',
#             'objects': http.request.env['viin_to_cv_profile_autoload.viin_to_cv_profile_autoload'].search([]),
#         })

#     @http.route('/viin_to_cv_profile_autoload/viin_to_cv_profile_autoload/objects/<model("viin_to_cv_profile_autoload.viin_to_cv_profile_autoload"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viin_to_cv_profile_autoload.object', {
#             'object': obj
#         })
