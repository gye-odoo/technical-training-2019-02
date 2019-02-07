# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'open_academy.session'

    instructor = fields.Many2one(string='Instructor', comodel_name='res.partner')
    start_date = fields.Datetime(string='Start Date')

    duration = fields.Float(string='Duration', default=1.0, digits=(3, 2), help='Duration (hours)')
    course_id = fields.Many2one(comodel_name='open_academy.course')
    course_name = fields.Char(string='Course Name', related='course_id.name')
    state = fields.Selection(string='Session Ready', selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ])
    active = fields.Boolean(string='Is Active', default=True)
    attendee_ids = fields.Many2many(string='Attendees', comodel_name='res.partner')

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration > 2:
                raise ValidationError("Session cannot be longer than 2 hours (current value: {})".format(record.duration))
