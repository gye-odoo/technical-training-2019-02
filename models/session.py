# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'open_academy.session'

    instructor = fields.Char(string='Instructor')
    start_time = fields.Char(string='Start Time')

    duration = fields.Float(string='Duration', default=1.0, digits=(3, 2), help='Duration of session in hours')
    course_id = fields.Many2one(comodel_name='open_academy.course')
    course_name = fields.Char(string='Course Name', related='course_id.name')
    prepared = fields.Boolean(string='Session Ready', default=False)
    active = fields.Boolean(string='Is Active', default=True)

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration > 2:
                raise ValidationError("Session cannot be longer than 2 hours (current value: {})".format(record.duration))
