{
    'name': "Differed Expense and JE Reports",
    'author': "Sid",
    'version': '14.0.1.0',

    'depends': ['account_accountant', 'account_asset', 'account'],

    'data': [
        'reports/journal_report_card.xml',
        'reports/journal_report_template.xml',
        'views/account_asset_views.xml',
    ],

    'application': True,
    'installable': True,
}
