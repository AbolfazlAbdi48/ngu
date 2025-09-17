from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactUs
from.forms import DurabilityTestForm
from django.http import JsonResponse
from decouple import config
import logging

logger = logging.getLogger(__name__)


def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        industry = request.POST.get('industry')

        try:
            ContactUs.objects.create(
                name=name,
                phone_number=phone_number,
                industry=industry,
                type='counseling'
            )
                                                                         
            send_mail(
                subject='درخواست جدید مشاوره',
                message=f'نام: {name}\nشماره تماس: {phone_number}\nصنعت: {industry}',
                from_email=config('EMAIL_HOST_USER'),
                recipient_list=config('AAA').split(','),
                fail_silently=False,
            )

            messages.success(
                request,
                'درخواست شما با موفقیت ثبت و ایمیل شد. کارشناسان تاک به زودی با شما تماس میگیرند.'
                '\nبه امید ایرانی آباد، مقتدر و شاد...'
            )
            return redirect('core:home')

        except Exception as e:
            messages.error(request, f'خطا در ثبت پیام یا ارسال ایمیل: {str(e)}')
            return redirect('core:home')

    return render(request, 'core/home.html')


QUESTIONS = [
    {"id":1, "text":"اگر برق قطع شود، ما سریعاً راه‌حل جایگزین (مثل ژنراتور یا UPS) داریم. قطعی برق نمی‌تواند کسب‌وکار ما را فلج کند.", "emoji":"🔌", "field_name":"q1"},
    {"id":2, "text":"اگر برخی از کارگران (مثل کارگران افغانستانی) در دسترس نباشند، ما جایگزین داریم. آموزش نیروی جدید برای ما راحت و سریع است.", "emoji":"👷", "field_name":"q2"},
    {"id":3, "text":"ما برای تأمین مواد اولیه به یک نفر/شرکت خاص وابسته نیستیم. اگر تأمین‌کننده اصلی دچار مشکل شود، می‌توانیم از جای دیگر تهیه کنیم.", "emoji":"🚚", "field_name":"q3"},
    {"id":4, "text":"اگر مسیرهای توزیع (حمل‌ونقل، جاده یا پیک) دچار مشکل شوند، باز هم می‌توانیم محصولات یا خدمات را به مشتری برسانیم. ما چندین کانال توزیع داریم.", "emoji":"📦", "field_name":"q4"},
    {"id":5, "text":"اگر مشتریان یا دولت به‌طور ناگهانی سبد خرید خود را تغییر دهند، کسب‌وکار ما آسیب نمی‌بیند. ما محصولات یا خدمات متنوعی برای جایگزینی داریم.", "emoji":"🛒", "field_name":"q5"},
    {"id":6, "text":"حتی اگر فروش ما کم شود، می‌توانیم برای چند ماه کسب‌وکار را ادامه دهیم. در مواقع بحران، دسترسی به وام یا سرمایه برای ما آسان است.", "emoji":"💰", "field_name":"q6"},
    {"id":7, "text":"اگر اینترنت قطع شود، کسب‌وکار ما کاملاً متوقف نمی‌شود. بدون اینترنت هم می‌توانیم بخش زیادی از کارمان را ادامه دهیم.", "emoji":"🌐", "field_name":"q7"},
    {"id":8, "text":"ما برای خرابی تجهیزات برنامه‌های پشتیبان داریم. زمان توقف کار حداقل است.", "emoji":"🔧", "field_name":"q8"},
    {"id":9, "text":"قراردادهای ما با شرکا انعطاف‌پذیر است. می‌توانیم به‌سرعت با تغییرات سازگار شویم.", "emoji":"🤝", "field_name":"q9"},
    {"id":10, "text":"ما روندهای بازار را رصد می‌کنیم و می‌توانیم استراتژی‌ها را سریع تغییر دهیم.", "emoji":"📈", "field_name":"q10"},
    {"id":11, "text":"نرخ حفظ کارکنان ما بالا است و برنامه‌های جانشینی داریم.", "emoji":"👥", "field_name":"q11"},
    {"id":12, "text":"سوابق مالی ما دیجیتالی و به‌صورت امن پشتیبانی می‌شوند.", "emoji":"💻", "field_name":"q12"},
    {"id":13, "text":"ما با مقررات مطابقت داریم و برای تغییرات قانونی برنامه‌ریزی داریم.", "emoji":"⚖️", "field_name":"q13"},
    {"id":14, "text":"بازخورد مشتریان به ما کمک می‌کند تا تاب‌آوری خود را بهبود دهیم.", "emoji":"📝", "field_name":"q14"}
]

def test_form(request):
    if request.method == 'POST':
        form = DurabilityTestForm(request.POST)
        logger.info(f"Received POST data: {request.POST}")
        if form.is_valid():
            test = form.save()
            logger.info(f"Form saved successfully for phone: {test.user_phone}")
            return JsonResponse({
                'success': True,
                'message': 'فرم با موفقیت ثبت شد!',
                'percentile': test.percentile(),
                'status': test.status(),
                'raw': test.raw_score(),
                'percentile_electricity_challenge': test.percentile_electricity_challenge,
                'status_electricity_challenge': test.status_electricity_challenge,
                'percentile_manual_labor_challenge': test.percentile_manual_labor_challenge,
                'status_manual_labor_challenge': test.status_manual_labor_challenge,
                'percentile_supply_chain_challenge': test.percentile_supply_chain_challenge,
                'status_supply_chain_challenge': test.status_supply_chain_challenge,
                'percentile_distribution_challenge': test.percentile_distribution_challenge,
                'status_distribution_challenge': test.status_distribution_challenge,
                'percentile_customer_demand_challenge': test.percentile_customer_demand_challenge,
                'status_customer_demand_challenge': test.status_customer_demand_challenge,
                'percentile_liquidity_challenge': test.percentile_liquidity_challenge,
                'status_liquidity_challenge': test.status_liquidity_challenge,
                'percentile_internet_challenge': test.percentile_internet_challenge,
                'status_internet_challenge': test.status_internet_challenge
            })
        else:
            logger.error(f"Form validation failed: {form.errors}")
            return JsonResponse({
                'success': False,
                'message': 'خطا در فرم. لطفاً تمام فیلدها را بررسی کنید.',
                'errors': form.errors.as_json()
            }, status=400)
    else:
        form = DurabilityTestForm()
    return render(request, 'core/test.html', {'form': form, 'question_fields': QUESTIONS})