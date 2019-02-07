# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models
from odoo.exceptions import ValidationError

class AddAttendees(models.TransientModel):
    _name = 'open_academy.wizard_add_attendees'
    _description = 'Wizard to add attendees to a session'

    session_id = fields.Many2one('open_academy.session', string="Sessions", default=lambda self: self._context.get('active_id'))
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.constrains('attendee_ids')
    def _check_attendees(self):
        self.ensure_one()
        if not self.attendee_ids:
            raise ValidationError("Please add at least one attendee to subscribe them to the session.")

    @api.constrains('session_id')
    def _check_session(self):
        self.ensure_one()
        if not self.session_id:
            raise ValidationError("Please select a session to add attendees.")

    @api.multi
    def subscribe(self):
        self.ensure_one()
        for session in self.session_id:
            session.attendee_ids |= self.attendee_ids
        return {}
