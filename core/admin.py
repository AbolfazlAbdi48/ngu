from django.contrib import admin
from core.models import DurabilityTest

@admin.register(DurabilityTest)
class DurabilityTestAdmin(admin.ModelAdmin):
    list_display = ('user_phone', 'user_name', 'user_industry', 'created_at', 'raw_score', 'percentile', 'status',
                    'percentile_electricity_challenge', 'status_electricity_challenge',
                    'percentile_manual_labor_challenge', 'status_manual_labor_challenge',
                    'percentile_supply_chain_challenge', 'status_supply_chain_challenge',
                    'percentile_distribution_challenge', 'status_distribution_challenge',
                    'percentile_customer_demand_challenge', 'status_customer_demand_challenge',
                    'percentile_liquidity_challenge', 'status_liquidity_challenge',
                    'percentile_internet_challenge', 'status_internet_challenge')
    readonly_fields = ('raw_score', 'percentile', 'status',
                       'percentile_electricity_challenge', 'status_electricity_challenge',
                       'percentile_manual_labor_challenge', 'status_manual_labor_challenge',
                       'percentile_supply_chain_challenge', 'status_supply_chain_challenge',
                       'percentile_distribution_challenge', 'status_distribution_challenge',
                       'percentile_customer_demand_challenge', 'status_customer_demand_challenge',
                       'percentile_liquidity_challenge', 'status_liquidity_challenge',
                       'percentile_internet_challenge', 'status_internet_challenge')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return []