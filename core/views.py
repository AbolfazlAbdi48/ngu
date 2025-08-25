from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactUs
from decouple import config


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
