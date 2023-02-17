from django.shortcuts import render
import logging

logger = logging.getLogger("django")


# Create your views here.
def show(request):
    logger.info('Hello, world!')
    logger.error('Critical!')
    return render(request, 'show.html')
