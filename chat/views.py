from django.shortcuts import render

def index(request, user_id):
    '''
    프로그램 시작 / 로깅 html을 응답으로 주는 뷰
    '''
    return render(request, 'chat/logs.html', {
        'user_id': user_id
    })