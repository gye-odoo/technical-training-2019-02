# -*- coding: utf-8 -*-

from odoo import models, fields

class Session(models.Model):
    _name = 'open_academy.session'

    instructor = fields.Char(string='Instructor')
    start_time = fields.Char(string='Start Time')

    duration = fields.Float(string='Duration', default=1.0)
    course_id = fields.Many2one(comodel_name='open_academy.course')
    prepared = fields.Boolean(string='Session Ready', default=False)
    active = fields.Boolean(string='Is Active', default=True)
