# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = """
    The course model defines attributes about individual courses.
"""

    name = fields.Char(string='Name', required=True)
    level = fields.Selection(string='Difficulty', selection=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])
    instructor = fields.Char(string='Instructor Name')
    description = fields.Text(string='Description')

