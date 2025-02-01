from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def home(request):
    EUFO = UserForm()
    d = {'EUFO': EUFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        if UFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            email = UFDO.cleaned_data.get('email')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            send_mail(
                'Registration Successfull',
                'Thanks for registrating into our application',
                'debajyotin56@gmail.com',
                [email],
                fail_silently=False,
            )
            return HttpResponse('DONE...')
        return HttpResponse('INVALID DATA')
    return render(request,'home.html', d)