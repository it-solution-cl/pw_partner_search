# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if name and not self.env.context.get('import_file'):
            args = args if args else []
            args.extend(['|', ['vat', 'ilike', name],
                         '|', ['name', 'ilike', name],
                        ['function', 'ilike', name]])
            name = ''
        return super(ResPartner, self).name_search(
            name=name, args=args, operator=operator, limit=limit)
