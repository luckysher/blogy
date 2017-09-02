# -*- coding: utf-8 -*-
from openerp import models, fields, api

class blogs(models.Model):
     _name = 'blogy.blogs'

     title = fields.Char('Title')
     description = fields.Char('Description')