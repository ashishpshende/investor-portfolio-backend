from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="portfolios")
    name = models.CharField(max_length=100, blank=True,
                            null=True, default='My Portfolio')
    invested_amount = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    current_value = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    profit_loss = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    profit_loss_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, default=0.00)
    created_at = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)
    total_stocks = models.PositiveIntegerField(default=0)
    total_mutual_funds = models.PositiveIntegerField(default=0)
    total_exchange_traded_funds = models.PositiveIntegerField(default=0)
    free_cash = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)


class Stock(models.Model):
    code = models.PositiveIntegerField(default=0, unique=True)
    symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    # e.g., 'PSU', 'Pharma', 'IT', 'Banking'
    type = models.CharField(max_length=50, blank=True, null=True)

    # Pricing data
    current_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    open_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    previous_close = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    day_high = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    day_low = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    week_52_high = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    week_52_low = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    all_time_high = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    all_time_low = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    last_traded_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True)

    # Volatility & volume
    volume = models.BigIntegerField(null=True, blank=True)
    average_volume = models.BigIntegerField(null=True, blank=True)

    # Market cap and other analytics
    market_cap = models.BigIntegerField(null=True, blank=True)
    pe_ratio = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    dividend_yield = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    stock_exchange = models.CharField(
        max_length=50, default='NSE')  # e.g., 'NSE', 'BSE'
    market_cap = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    # e.g., 'Technology', 'Finance'
    sector = models.CharField(max_length=50, blank=True)
    # e.g., 'Software', 'Banking'
    industry = models.CharField(max_length=50, blank=True)
    ipo_date = models.DateField(null=True, blank=True)  # Date of IPO
    # International Securities Identification Number
    isin = models.CharField(max_length=12, unique=True, blank=True)
    # Additional information about the stock
    description = models.TextField(null=True, blank=True)
    # To mark if the stock is currently active
    active = models.BooleanField(default=True)


class PortfolioStock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    amount_invested = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    current_value = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    profit_loss = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    profit_loss_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, default=0.00)
    average_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    added_on = models.DateTimeField(auto_now=True, blank=True)
    last_added_on = models.DateTimeField(auto_now=True, blank=True)


class MutualFund(models.Model):
    name = models.CharField(max_length=100)
    current_nav = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    nfo_date = models.DateField(null=True, blank=True)  # New Fund Offer date
    isin = models.CharField(max_length=12, unique=True, blank=True)
    scheme_type = models.CharField(
        max_length=50, blank=True)  # e.g., 'Equity', 'Debt'
    # e.g., 'Large Cap', 'Mid Cap'
    category = models.CharField(max_length=50, blank=True)
    fund_house = models.CharField(
        max_length=50, blank=True)  # e.g., 'HDFC', 'ICICI'
    # e.g., 'Open-ended', 'Close-ended'
    type = models.CharField(max_length=50, blank=True)
    # AUM - Assets Under Management
    # e.g., 'Large', 'Medium', 'Small'
    size = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    # Assets Under Management
    aum = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    # International Securities Identification Number
    # Compound Annual Growth Rate
    cagr = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    # e.g., 'Low', 'Medium', 'High'
    fund_size = models.BigIntegerField(
        null=True, blank=True)  # Assets Under Management
    expense_ratio = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)  # % of AUM
    # e.g., 'Low', 'Moderate', 'High'
    risk_level = models.CharField(max_length=50, null=True, blank=True)
    benchmark_index = models.CharField(
        max_length=100, null=True, blank=True)  # e.g., 'Nifty 50'

    returns_1yr = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)  # in %
    returns_3yr = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    returns_5yr = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)


class PortfolioMutualFund(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    mutual_fund = models.ForeignKey(MutualFund, on_delete=models.CASCADE)
    amount_invested = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, blank=True)
    average_nav = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    current_value = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    profit_loss = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00)
    profit_loss_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, default=0.00)
    invested_start_date = models.DateField(null=True, blank=True)
    last_invested_date = models.DateField(null=True, blank=True)
    units = models.PositiveIntegerField()
    investment_type = models.CharField(
        max_length=50, default='SIP', choices=[('SIP', 'SIP'), ('Lump Sum', 'Lump Sum')])
    active = models.BooleanField(default=True)
