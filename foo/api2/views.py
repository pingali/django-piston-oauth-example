from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

def request_token_ready(request, token):
    error = request.GET.get('error', '')
    ctx = RequestContext(request, {
        'error' : error,
        'token' : token
    })
    return render_to_response(
        'piston/request_token_ready.html',
        context_instance = ctx
    )
