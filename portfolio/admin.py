from django.contrib import admin

# Register your models here.
from .models import Portfolio, Stock, PortfolioStock, MutualFund  # your models

admin.site.register(Portfolio)
admin.site.register(Stock)
admin.site.register(PortfolioStock)
admin.site.register(MutualFund)
