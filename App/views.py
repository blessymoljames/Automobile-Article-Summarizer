# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from App import trialsample

# Create your views here.

data=""
out=""

def home(request):
	return render(request,'firstpage.html',{})

def parse(requests):
	data=requests.POST.getlist('name[]')
	out = trialsample.main(data)
	return render(requests,"firstpage1.html",{"data":out})


