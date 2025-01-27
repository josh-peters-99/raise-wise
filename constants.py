# Federal Tax Brackets: [(lower_limit, upper_limit, tax_rate)]
FEDERAL_TAX_BRACKETS = [
    {'min': 0, 'max': 11600, 'rate': 0.10},
    {'min': 11601, 'max': 47150, 'rate': 0.12},
    {'min': 47151, 'max': 100525, 'rate': 0.22},
    {'min': 100526, 'max': 191950, 'rate': 0.24},
    {'min': 191951, 'max': 243725, 'rate': 0.32},
    {'min': 243726, 'max': 609350, 'rate': 0.35},
    {'min': 609351, 'max': float('inf'), 'rate': 0.37}
]

#State Income Taxes
STATE_TAXES = [
    {'UT': 0.0455},
    {'AZ': 0.025},
    {'NV': 0.0}
]