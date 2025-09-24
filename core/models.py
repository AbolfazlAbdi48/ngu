from django.db import models

class DurabilityTest(models.Model):
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=15)
    user_industry = models.CharField(max_length=50)
    q1 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q2 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q3 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q4 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q5 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q6 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q7 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q8 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q9 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q10 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q11 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q12 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q13 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    q14 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def raw_score(self):
        return sum([self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12, self.q13, self.q14])

    def percentile(self):
        min_score = 14
        max_score = 70
        return round(((self.raw_score() - min_score) / (max_score - min_score)) * 100)

    def status(self):
        perc = self.percentile()
        if perc >= 64:
            return "آماده برای بحران"
        elif perc >= 25:
            return "نیاز به تقویت"
        else:
            return "خطر جدی در شرایط بحران"

    @property
    def percentile_electricity_challenge(self):  # q1-q2: چالش قطعی برق
        min_score = 2
        max_score = 10
        return round(((self.q1 + self.q2 - min_score) / (max_score - min_score)) * 100)

    @property
    def status_electricity_challenge(self):
        perc = self.percentile_electricity_challenge
        if perc >= 64:
            return "آماده برای بحران"
        elif perc >= 25:
            return "نیاز به تقویت"
        else:
            return "خطر جدی در شرایط بحران"

    @property
    def percentile_manual_labor_challenge(self):  # q3-q4: چالش منابع انسانی کار یدی
        min_score = 2
        max_score = 10
        return round(((self.q3 + self.q4 - min_score) / (max_score - min_score)) * 100)

    @property
    def status_manual_labor_challenge(self):
        perc = self.percentile_manual_labor_challenge
        if perc >= 64:
            return "آماده برای بحران"
        elif perc >= 25:
            return "نیاز به تقویت"
        else:
            return "خطر جدی در شرایط بحران"

    @property
    def percentile_supply_chain_challenge(self):  # q5-q6: چالش به هم ریختن زنجیره تامین
        min_score = 2
        max_score = 10
        return round(((self.q5 + self.q6 - min_score) / (max_score - min_score)) * 100)

    @property
    def status_supply_chain_challenge(self):
        perc = self.percentile_supply_chain_challenge
        if perc >= 64:
            return "آماده برای بحران"
        elif perc >= 25:
            return "نیاز به تقویت"
        else:
            return "خطر جدی در شرایط بحران"

    @property
    def percentile_distribution_challenge(self):  # q7-q8: چالش به هم ریختن زنجیره ی توزیع
        min_score = 2
        max_score = 10
        return round(((self.q7 + self.q8 - min_score) / (max_score - min_score)) * 100)

    @property
    def status_distribution_challenge(self):
        perc = self.percentile_distribution_challenge
        if perc >= 64:
            return "آماده برای بحران"
        elif perc >= 25:
            return "نیاز به تقویت"
        else:
            return "خطر جدی در شرایط بحران"

    @property
    def percentile_customer_demand_challenge(self):  # q9-q10: چالش تغییر ناگهانی در سبد خرید دولت و خانوار
        min_score = 2
        max_score = 10
        return round(((self.q9 + self.q10 - min_score) / (max_score - min_score)) * 100)

    @property
    def status_customer_demand_challenge(self):
        perc = self.percentile_customer_demand_challenge
        if perc >= 64:
            return "آماده برای بحران"
        elif perc >= 25:
            return "نیاز به تقویت"
        else:
            return "خطر جدی در شرایط بحران"

    @property
    def percentile_liquidity_challenge(self):  # q11-q12: چالش تامین نقدینگی و سرمایه در گردش
        min_score = 2
        max_score = 10
        return round(((self.q11 + self.q12 - min_score) / (max_score - min_score)) * 100)

    @property
    def status_liquidity_challenge(self):
        perc = self.percentile_liquidity_challenge
        if perc >= 64:
            return "آماده برای بحران"
        elif perc >= 25:
            return "نیاز به تقویت"
        else:
            return "خطر جدی در شرایط بحران"

    @property
    def percentile_internet_challenge(self):  # q13-q14: چالش قطعی اینترنت
        min_score = 2
        max_score = 10
        return round(((self.q13 + self.q14 - min_score) / (max_score - min_score)) * 100)

    @property
    def status_internet_challenge(self):
        perc = self.percentile_internet_challenge
        if perc >= 64:
            return "آماده برای بحران"
        elif perc >= 25:
            return "نیاز به تقویت"
        else:
            return "خطر جدی در شرایط بحران"