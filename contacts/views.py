from django.shortcuts import render
from .models import QA

# Create your views here.

def chat(request):
    questions = QA.objects.all()
    if request.method == "POST":
        if 'submit-reply' in request.POST:
            a = request.POST.get('answer')
            q_id = request.POST.get('ques-id')
            question = QA.objects.get(pk=q_id)
            question.ans = a
            question.save()

            print("Replied")
        elif 'submit-question' in request.POST:
            q = request.POST.get('question')
            qa = QA(user=request.user, ques=q)
            qa.save()
    return render(request, "contacts/chat.html", {"questions": questions})