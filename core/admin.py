from django.contrib import admin
from core.models import ContactUs, DurabilityTest


# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'phone_number', 'industry', 'seen')
    list_editable = ('seen',)
    list_filter = ('seen', 'created_at')
    search_fields = ('name', 'phone_number', 'industry')
    readonly_fields = ('created_at',)

@admin.register(DurabilityTest)
class DurabilityTestAdmin(admin.ModelAdmin):
    list_display = ('user_phone', 'created_at', 'raw_score', 'percentile', 'status',
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
        if obj:  # Editing an existing object
            return self.readonly_fields
        return []  # Allow editing for new objects