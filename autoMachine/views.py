from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .auto_scraper import *

from django.http import JsonResponse


# Create your views here.

def mainview(request) :
    return render(request, "autoMachine/index.html")


def scrap(request) :
    run_main()
    return JsonResponse({'msg': '작업이 종료되었습니다'})


def submitScrap(request) :
    getDate = request.POST.get('postDate','')
    getActResult = run_main( getDate )

    if getActResult == 'dateError' :
        return JsonResponse({'msg': '날짜 입력오류'})
    else :
        return JsonResponse({'msg': '작업이 종료되었습니다'})
    
    

    # return HttpResponseRedirect( reverse('board:gotolist'))
    # return HttpResponse(getDate)
