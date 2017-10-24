from django.contrib import auth  # 別忘了import auth
from django.shortcuts import render_to_response
from .pushTracker import printUserGitStatus
def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')

def index(request):
    return render_to_response('index.html',locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def gitCommitYet(request):
    result = printUserGitStatus()
    return render_to_response('whyIndexIsNotInTheRootDirButInIndexDir.html',{
        'gitStatus' : result
    })
