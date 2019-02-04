from django.http import JsonResponse
from django.views import View
import json
from .models import Task


class Tasks(View):
    def get(self, request):
        resultList = list(Task.objects.values().all())
        return JsonResponse ({'status':'ok', 'tasks':resultList})
    def post(self,request):
        body = json.loads(request.body.decode())
        print(body)
        Task.objects.create(name=body['task'], isComplete=body['isComplete'])
        resultList = list(Task.objects.values().all())
        return JsonResponse ({'status':'ok', 'tasks':resultList})
class TaskByID(View):
    def get(self, request, taskID):
        return JsonResponse({'status':'ok'})
    def put(self, request, taskID):
        body = json.loads(request.body.decode())
        print(body['isComplete'])
        Task.objects.filter(id=taskID).update(isComplete = body['isComplete'])
        print(Task.objects.filter(id=taskID))
        resultList = list(Task.objects.values().all())
        return JsonResponse ({'status':'ok', 'tasks':resultList})
    def delete(self, request, taskID):
        Task.objects.filter(id=taskID).delete()
        resultList = list(Task.objects.values().all())
        return JsonResponse ({'status':'ok', 'tasks':resultList})


