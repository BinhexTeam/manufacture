# Copyright 2024 r.perez@binhex.cloud
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Mrp Production Stock Secondary Unit",
    "summary": """Adds support for the stock secondary units of measure feature on raw stock moves associated with manufacturing orders""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "r.perez@binhex.cloud,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/manufacture",
    "depends": ["mrp", "stock_secondary_unit"],
    "data": [
        "views/mrp_production_views.xml",
    ],
    "demo": [],
}
