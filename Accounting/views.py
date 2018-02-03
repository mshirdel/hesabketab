from django.http import HttpResponse

def index(request):
    return HttpResponse('accounting view test.')