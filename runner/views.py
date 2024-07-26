from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient

from runner.models import Students
from runner.serializers import StudentSerializer


# Create your views here.
def index(request):
    data = Students.objects.all()
    context = {'data': data}
    return render(request,'index.html',context)



def save(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        form = Students(name=name, email=email, age=age, gender=gender)
        form.save()
        return redirect("/")
    return render(request,'index.html')
def editStudent(request,id):
    if request.method == 'post':
        name = request.post['name']
        email = request.post['email']
        age = request.post['age']
        gender = request.post['gender']


        editForm = Students.object.get(id=id)
        editForm.name = name
        editForm.email = email
        editForm.age = age
        editForm.gender = gender
        editForm.save()
        return redirect("/")
    student = Students.objects.get(id=id)
    context = {'student': student}
    return render(request, "edit.html",context)

def deleteStudents(request,id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect("/")

def student_list(request):
    student = Students.objects.all()
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)
def mpesaapi(request):
    cl = MpesaClient()
    phone_number ='0795542312'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
    return HttpResponse(response)


def stk_push_callback(request):
    data = request.body
    return HttpResponse('STK PUSH has been sent successfully')





