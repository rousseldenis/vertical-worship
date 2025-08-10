# Copyright 2019 Denis Roussel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class EventEvent(models.Model):
    _name = "event.event"
    _inherit = ["event.event", "worship.mixin"]
