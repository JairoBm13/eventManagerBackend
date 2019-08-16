from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods(['POST'])
def create_event(request):
    return HttpResponse("Hello, world. You're at the polls post.")

@require_http_methods(['GET'])
def event_details(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods(['PUT'])
def edit_event(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods(['DELETE'])
def delete_event(request):
    return HttpResponse("Hello, world. You're at the polls index.")