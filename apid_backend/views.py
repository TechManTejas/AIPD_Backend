import subprocess
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


@csrf_exempt
def git_push_view(request):
    if request.method == 'POST':

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"utility ({timestamp})"
        
        subprocess.call(['git', 'add', '.'])
        subprocess.call(['git', 'commit', '-m', commit_message])
        subprocess.call(['git', 'push'])
        return HttpResponse('Git add, commit, and push commands executed successfully.')
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def git_pull_view(request):
    if request.method == 'POST':

        subprocess.call(['git', 'pull'])

        return HttpResponse('Git pull command executed successfully.')
    else:
        return HttpResponseNotAllowed(['POST'])
