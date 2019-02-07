# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'This model contains relevant information about each course.'

    name = fields.Char(string='Name', required=True)
    level = fields.Selection(string='Difficulty', selection=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])
    instructor = fields.Many2one(string='Instructor', comodel_name='res.partner')
    description = fields.Text(string='Description')

    session_ids = fields.One2many(comodel_name='open_academy.session', inverse_name='course_id')
    session_count = fields.Integer(string='No. of Sessions', compute='_compute_session_count', store=True)

    @api.depends('session_ids')
    def _compute_session_count(self):
        for record in self:
            record.session_count = len(record.session_ids)

    @api.onchange('level')
    def change_description(self):
        for record in self:
            if record.level == 'hard':
                record.description = '[Hard] ' + str(record.description)
