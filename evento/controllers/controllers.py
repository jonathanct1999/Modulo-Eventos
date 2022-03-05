# -*- coding: utf-8 -*-
# from odoo import http


# class Evento(http.Controller):
#     @http.route('/evento/evento/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/evento/evento/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('evento.listing', {
#             'root': '/evento/evento',
#             'objects': http.request.env['evento.evento'].search([]),
#         })

#     @http.route('/evento/evento/objects/<model("evento.evento"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('evento.object', {
#             'object': obj
#         })
