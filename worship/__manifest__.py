# Copyright 2019 Denis Roussel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Worship",
    "summary": """
        Adds base application for Worship management""",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "Denis Roussel,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/vertical-worship",
    "application": True,
    "depends": [
        "base",
    ],
    "data": [
        "views/menu.xml",
        "security/security.xml",
    ],
}
