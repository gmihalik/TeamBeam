from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import League, Event
from django.contrib.auth.models import User
import uuid
from django.db.models import F

