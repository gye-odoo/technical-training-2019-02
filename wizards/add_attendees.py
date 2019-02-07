# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models

class AddAttendees(models.TransientModel):
    _name = 'open_academy.wizard_add_attendees'
    _description = 'Wizard to add attendees to a session'

    session_id = fields.Many2one('open_academy.session', string="Sessions", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees", )

    @api.multi
    def subscribe(self):
        for session in self.session_id:
            session.attendee_ids |= self.attendee_ids
        return {}
