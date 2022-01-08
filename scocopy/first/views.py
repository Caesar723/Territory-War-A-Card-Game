from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import mysql.connector
import re
import csv

def home(request):
    return render(request,'homeP.html')