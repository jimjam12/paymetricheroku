from urllib import request
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import ContactForm, RequestForm
from accounts.models import RequestLeave, Attendance
from django.db.models.query_utils import Q
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


def startup(request):
    return render(request, "startup.html")


def home_page(request):
    if request.user.is_authenticated:
        print(request.session.get('first_name'))
        return render(request, "home/home_page.html")
    else:
        return redirect('login')


def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form

    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/contact.html", context)


def list_user(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(email__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(
            middle_name__icontains=q))
        data = User.objects.filter(multiple_q)
        model = data.values()

    else:
        model = User.objects.all().values()
        q = ""
    context = {
        'model': model,
        'q': q
    }
    return render(request, 'admin/list_user.html', context)


def update(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'auth/update.html', context)


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('list_user')

def profile(request):

    employee = User.objects.filter(id=id)

def updaterecord(request, id):
    newEmail = request.POST['email']
    newFirstName = request.POST['first_name']
    newMiddleName = request.POST['middle_name']
    newLastName = request.POST['last_name']
    newGender = request.POST['gender']
    newNationality = request.POST['nationality']
    newBirthDate = request.POST['birth_date']
    newAddress = request.POST['address']
    newPayPerDay1 = request.POST['pay_per_day1']
    newSickLeave = request.POST['sick_leave']
    newVacationLeave = request.POST['vacation_leave']
    newTaxRate = request.POST['tax_rate']

    user = User.objects.get
    user.email = newEmail
    user.first_name = newFirstName
    user.middle_name = newMiddleName
    user.last_name = newLastName
    user.gender = newGender
    user.nationality = newNationality
    user.birth_date = newBirthDate
    user.address = newAddress
    user.pay_per_day1 = newPayPerDay1
    user.sick_leave = newSickLeave
    user.vacation_leave = newVacationLeave
    user.tax_rate = newTaxRate
    user.save()

    return redirect('list_user')

# def attendance(request):
#     return render(request, "attendance/attendance.html")

def detailed(request):

    #My Information / User Profile
    reqEmail = request.user.email
    qs = User.objects.get(email=reqEmail)
    qs2 = Attendance.objects.filter(user=request.user).count()
    print(qs2)
    if not qs.pay_per_day1:
        total = 0
    else:

        total = float((qs.pay_per_day1 * qs2) - (qs.pay_per_day1 * (1 - qs.tax_rate)))
    context = {
        'qs': qs,
        'total': total,
        'qs2': qs2

    }
    return render(request, "my_info/my_info.html", context)


def testFunction(request, id):
    #Detailed View User List
    qs = User.objects.get(id=id)
    qs2 = Attendance.objects.filter(user=qs).count()
    print(qs2)
    if not qs.pay_per_day1:
        total = 0
    else:

        total = float((qs.pay_per_day1 * qs2) - (qs.pay_per_day1 * (1 - qs.tax_rate)))
    # print(total)
    context = {
        'qs': qs,
        'total': total,
        'qs2': qs2

    }
    return render(request, 'details/detailed_view.html', context)


def request_leave(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            requests = RequestLeave(
                emp_email=request.POST['emp_email'],
                emp_name=request.POST['emp_name'],
                emp_leaveDateStart=request.POST['emp_leaveDateStart'],
                emp_leaveDateEnd=request.POST['emp_leaveDateEnd'],
                typeOf_leave=request.POST['typeOf_leave'],
                reasonFor_leave=request.POST['reasonFor_leave']
            )
            requests.save()

    # context = { 'form': form }
    return render(request, "emp_requests/request_leave.html")


def leaveApprove(request, id):
    if request.user.is_staff:
        qs = RequestLeave.objects.filter(id=id)
        qs.update(IsApproved=True)
        return redirect('list_requests')
    elif request.user.is_admin:
        qs = RequestLeave.objects.filter(id=id)
        qs.update(AdminApproved=True)
        return redirect('list_requests')
    # print(qs)
    # return redirect('list_requests')

def leaveDecline(request, id):
    if request.user.is_staff:
        qs = RequestLeave.objects.filter(id=id)
        qs.update(IsDeclined=True)
        return redirect('list_requests')
    elif request.user.is_admin:
        qs = RequestLeave.objects.filter(id=id)
        qs.update(AdminDeclined=True)
        return redirect('list_requests')

def AdminleaveApprove(request, id):

    qs2 = RequestLeave.objects.filter(id=id)
    qs.update(AdminApproved=True)
    print(qs2)
    return redirect('requests')

def AdminleaveDecline(request, id):

    qs2 = RequestLeave.objects.filter(id=id)
    qs.update(AdminDeclined=True)
    print(qs2)
    return redirect('requests')



#Arnaz Code

def list_requests(request):
    qs = RequestLeave.objects.filter(IsApproved=False, IsDeclined=False)
    qs2 = RequestLeave.objects.filter(IsApproved=True, AdminApproved=False, AdminDeclined=False)
    print(request.user.is_staff)
    context = {
        'qs': qs,
        'qs2': qs2
    }
    return render(request, "emp_requests/requests.html", context)