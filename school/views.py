from django.http import JsonResponse

def students (req):
    if req.method == 'GET':
        student = { "id": 1, "name": "Rafael"}
        return JsonResponse(student)
