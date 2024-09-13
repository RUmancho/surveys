from django.shortcuts import render, HttpResponse
from . import form
# Create your views here.

userData = {}

def questionnaire(request):
    entry = form.Entry()

    entry.getEmail = request.POST.get("getEmail", "")
    entry.getDate = request.POST.get("getDate", "")
    entry.getNum = request.POST.get("getNum", "")
    entry.getLine = request.POST.get("getLine", "")

    context = {
        "entry" : entry
    }

    if all([entry.getEmail, entry.getDate, entry.getNum, entry.getLine]):
        userData["email"] = entry.getEmail
        userData["date"]  = entry.getDate
        userData["num"]   = entry.getNum
        userData["line"]  = entry.getEmail

    return render(request, "entry.html", context)

def show_surveys(request):
    """Вернёт сохранённые пользовательские данные"""
    saves = ""
    for key in userData:
        saves += f"{key}  {userData[key]}</br>"

    if len(userData) == 0:
        return HttpResponse(f"У вас нет сохранённых данных")
    return HttpResponse(saves)