from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import BookingForm
from .models import BookingModel, VisitModel
import random


def booking(request):
    Name = 0
    Mobile_No = 0
    Address = 0
    Age = 0
    Gender = 0
    Account_status = 0
    submit = 0
    rand = random.randint(0, 10000)

    if request.GET:
        Name = request.GET["Name"]
        Mobile_No = int(request.GET["Mobile_No"])
        Address = request.GET["Address"]
        Age = int(request.GET["Age"])
        Gender = request.GET["Gender"]
        Account_status = "unverified"
        rand = random.randint(0, 10000)
        print(rand)

        opt = request.GET["option"]
        booking = BookingModel()
        booking.Name = Name
        booking.Mobile_No = Mobile_No
        booking.Address = Address
        booking.Age = Age
        booking.Gender = Gender
        booking.Account_status = Account_status
        rand = random.randint(0, 10000)
        print(rand)

        booking.save()
        print(opt)
        if opt == 'submit':
            submit = Name
    return render(request, "booking.html",
                  {"Name": Name, "Mobile_No": Mobile_No, "Address": Address, "Age": Age, "Gender": Gender,
                   "Account_status": Account_status, "rand": rand})


def form(request):
    if request.POST:
        newbook = BookingForm(request.POST)
        if newbook.is_valid():
            newbook.save(commit=False)
            newbook.save()
            return HttpResponse("Book Saved")
    initial = {"Name": "Name", "Mobile_No": 200, "Address": "x", "Age": "33", 'Gender': "male",
               "Account_status": "unverified"}
    return render(request, "bookingf.html", {"form": BookingForm(initial=initial)})


def entryform(request):
    Mobile_No = 0
    rand=""

    if request.GET:
        Mobile_No = int(request.GET["Mobile_No"])
        print("mobile no ",Mobile_No)
        rand = random.randint(1000, 9999)
        print(rand)
        opt = request.GET["option"]
        entryform = VisitModel()
        entryform.Mobile_No=Mobile_No
        entryform.Random_No=rand
        entryform.save()
        print(opt)

    return render(request, 'entryform.html', {"Mobile_No": Mobile_No, "rand": rand})
