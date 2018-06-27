from django.shortcuts import render
from emaillist.models import Emaillist
from django.http import HttpResponseRedirect
# Create your views here.
# 파라미터가 request로 들어온다. - handler함수

def index(request):
    # randering
    emaillist_list = Emaillist.objects.all().order_by('-id') # id의 있는 객체들을 리턴해서 list에 넣어준다.
    # emaillist 객체들이 들어있다.
    data = {'emaillist_list': emaillist_list} # emaillist_list가 emaillist_list로 html
    return render(request, 'index.html' , data)
    #return render(request,'index.html')
# 응답할 때 django application을 거치고, 해당 index함수가 있는 application을 찾는다.
def form(request):
    return render(request, 'form.html')

def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn'] # 이름은 포스트[dict] 방식으로
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save() # 쿼리를 안하고, save를 쓰면 db에 들어간다.
    return HttpResponseRedirect('/emaillist') # 다시 리스트로 돌아가게하는 redirect 함수
    # 주로 웹은 등록하고나서 메인으로 돌아가기 때문
    # 등록 후의 화면이동은 redirect로 해준다.
    #return render(request, 'success.html') # 요청에 대한 응답을 직접해준다. success 파일안에 html함수
