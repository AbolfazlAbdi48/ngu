from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactUs


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
            messages.success(request,
                             'درخواست شما با موفقیت ثبت شد. کارشناسان تاک به زودی با شما تماس میگیرند.'
                             ' \n به امید ایرانی آباد، مقتدر و شاد...'
                             )
            return redirect('core:home')
        except Exception as e:
            messages.error(request, f'خطا در ثبت پیام: {str(e)}')
            return redirect('core:home')

    return render(request, 'core/home.html')
