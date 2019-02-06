from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect

def indexx(request):
	return render(request,"indexx.html")