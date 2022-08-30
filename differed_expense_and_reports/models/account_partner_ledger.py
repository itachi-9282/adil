from odoo import api, fields, models, _, _lt


class ReportPartnerLedger(models.AbstractModel):
    _inherit = "account.partner.ledger"

    filter_account_type = [
        {'id': 'receivable', 'name': _lt('Receivable'), 'selected': False},
        {'id': 'payable', 'name': _lt('Payable'), 'selected': False},
        {'id': 'other', 'name': _lt('Miscellaneous'), 'selected': False}
    ]
    print('')

    @api.model
    def _get_options_domain(self, options):
        domain = super(ReportPartnerLedger, self)._get_options_domain(options)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>', options)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!', domain)
        return domain
