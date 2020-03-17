from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Reader, Reading
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime, timedelta
from .forms import UserRegisterForm, ReadingSchedule
from django.contrib import messages
from django.core.mail import send_mail

month = date.today().month
year = date.today().year
day = date.today().day
today = date(year, month, day)

try:
    read = Reading.objects.get(date_reading=today)
    if read:
        send_mail(
            'Reading', 'you are reaing today',
             'kuhneykwame@gmail.com', ['woden42076@mailernam.com'],
             fail_silently=False
            )
except Reading.DoesNotExist:
    pass

# Create your views here.
def home(request):
    month = date.today().month
    year = date.today().year
    day = date.today().day
    today = date(year, month, day)
    return render(request,'readers/home.html',{'lists':Reading.objects.all().order_by('date_reading'),'today':today,'month':month})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'readers/register.html',{'form':form})

class ReaderDetailView(DetailView):
    model = Reader
    template_name = 'readers/readers-detail.html'


class ReadingDetailView(DetailView):
    model = Reading
    template_name = 'readers/reading-detail.html'


class ReadingCreateView(CreateView,LoginRequiredMixin):
    model = Reading
    template_name = 'readers/reading_create.html'
    fields = ['reader','date_reading']

class ReaderCreateView(CreateView, LoginRequiredMixin):
    model = Reader
    template_name = 'readers/reader_create.html'
    fields = ['name','profile_image','date_joined']

#class AdminCreateView(CreateView):
 #   model = Admin
  #  template_name = 'readers/admin-create.html'
   # fields = ['name','profile_image']


def reading(request):
    if request.method == 'POST':
        form = ReadingSchedule(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('reader')
            date = form.cleaned_data.get('date_reading')
            publication = form.cleaned_data.get('publication')
            title = form.cleaned_data.get('title')
            try:
                obj = Reading.objects.get(date_reading=date)
                messages.success(request, f'This schedule has already been created')
                '''send_mail(
                     'Subject here', 'Here is the message.',
                     'kuhneykwame@gmail.com', ['vonaf26544@upcmaill.com'],
                     fail_silently=False
                )'''
            except Reading.DoesNotExist:
                obj = Reading(reader=username, date_reading=date, publication=publication, title=title)
                obj.save()
                return redirect('home')
    else:
        form = ReadingSchedule()
    return render(request,'readers/reading_create.html',{'form':form})

class ReaderListView(ListView):
    model = Reader
    template_name = 'readers/readers-list.html'
    context_object_name = 'readers'
    ordering = ['date_joined']

class ReadingUpdateView(UpdateView, LoginRequiredMixin):
    model = Reading
    template_name = 'readers/reading-update.html'
    fields = ['reader','date_reading','publication','title']

class ReadingDeleteView(DeleteView):
    model = Reading
    template_name = 'readers/reading_delete.html'
    success_url = '/'

def listview(request):
    month = date.today().month
    year = date.today().year
    day = date.today().day
    today = date(year, month, day)
    return render(request,'readers/table-list.html',{'lists':Reading.objects.all().order_by('date_reading'),'today':today})


    
