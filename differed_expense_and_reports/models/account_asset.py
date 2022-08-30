from odoo import api, fields, models, _


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    partner_id = fields.Many2one('res.partner', string='Customer')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self._origin.depreciation_move_ids:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!', self.asset_type)
            if not rec.partner_id:
                if rec.state == 'draft':
                    if self.asset_type == 'expense':
                        print('dddddddddddddddexpensedddddddddddd',self.asset_type)
                        rec.update({
                            'partner_id': self.partner_id.id,
                            'line_ids': [(1, line.id, {
                                'partner_id': self.partner_id.id if line.credit > 0 else False,
                            })for line in rec.line_ids]
                        })
                    elif self.asset_type == 'sale':
                        print('dddddddddddddddsaledddddddddddd', self.asset_type)
                        rec.update({
                            'partner_id': self.partner_id.id,
                            'line_ids': [(1, line.id, {
                                'partner_id': self.partner_id.id if line.debit > 0 else False,
                            }) for line in rec.line_ids]
                        })

    def compute_depreciation_board(self):
        re = super(AccountAsset, self).compute_depreciation_board()
        if self.partner_id:
            for rec in self.depreciation_move_ids:
                if not rec.partner_id:
                    if rec.state == 'draft':
                        if self.asset_type == 'expense':
                            rec.update({
                                'partner_id': self.partner_id.id,
                                'line_ids': [(1, line.id, {
                                    'partner_id': self.partner_id.id if line.credit > 0 else False,
                                }) for line in rec.line_ids]
                            })
                        elif self.asset_type == 'sale':
                            rec.update({
                                'partner_id': self.partner_id.id,
                                'line_ids': [(1, line.id, {
                                    'partner_id': self.partner_id.id if line.debit > 0 else False,
                                }) for line in rec.line_ids]
                            })
        return re
