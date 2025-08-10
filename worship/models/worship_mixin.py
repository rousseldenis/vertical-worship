# Copyright 2019 Denis Roussel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorshipMixin(models.AbstractModel):
    _name = "worship.mixin"
    _description = "Worship Mixin"

    worship_related = fields.Boolean(
        help="This is a technical field to represent models that were created"
        "in a worship context",
    )
