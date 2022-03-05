#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _ 


class evento(models.Model):
    _name = 'evento.evento'
    _description = 'evento.evento'

    name = fields.Char("Event Name :", required=True)
    organizador = fields.Char("Organizator Name :", required=True)
    date = fields.Date("Event Date : ", required=True)
    description = fields.Text("Informacion of the Event :", required=True)
    image = fields.Binary("Up imagens : ", required=True)
    estado = fields.Selection([('sonnn', 'Soonn'),('available', 'Available'),('finish', 'Finish'),('cancelled', 'Cancelled'),], default="soon")

