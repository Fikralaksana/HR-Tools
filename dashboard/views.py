from django.http.response import FileResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Contract, Department,Employee
from django.shortcuts import get_object_or_404
from datetime import date
from strgen import StringGenerator as SG

# Create your views here.
def dashboard(request):
    employee_count=Employee.objects.all().count()
    department_count=Department.objects.all().count()

    contract_type=Contract.objects.all()
    full_time=contract_type[0].id
    part_time=contract_type[1].id
    freelance=contract_type[2].id
    full_count=Employee.objects.filter(contract_type=full_time).count()
    part_count=Employee.objects.filter(contract_type=part_time).count()
    freelance_count=Employee.objects.filter(contract_type=freelance).count()
    
    year=date.today().year
    contract_end_count=Employee.objects.filter(contract_end__year=year).count()
    

    context={"employee_count":employee_count,
    "department_count":department_count,
    "full_count":full_count,
    "part_count":part_count,
    "freelance_count":freelance_count,
    "contract_end_count":contract_end_count,}
    return render(request,"dashboard/counter.html",context)

def input_data(request):
    departments=Department.objects.all()
    contract_types=Contract.objects.all()
    if request.method == 'POST':
        photo=request.FILES.get('photo')
        ekstention=photo.name.split('.')
        ekstention=ekstention[-1]
        photo.name=SG("[\w]{40}").render()+'.'+ekstention

        department_id=int(request.POST.get('department'))
        contract_id=int(request.POST.get('contract_type'))
        department=Department.objects.get(id=department_id)
        contract=Contract.objects.get(id=contract_id)

        print(photo.name)
        new_employee=Employee(name=request.POST.get('name'),
        date_of_birth=request.POST.get('date_of_birth'),
        email=request.POST.get('email'),
        phone_number=request.POST.get('phone_number'),
        address=request.POST.get('address'),
        department=department,
        contract_type=contract,
        contract_start=request.POST.get('contract_start'),
        contract_end=request.POST.get('contract_end'),
        photo=photo,
        description=request.POST.get('description'),
        )
        new_employee.save()


    context={'departments':departments,
    'contract_types':contract_types,
    }
    return render(request, 'dashboard/input.html',context)

def employeelist(request):
    employees=Employee.objects.all()
    context={'employees':employees}
    return render(request,'dashboard/employees.html',context)

def detail_employee(request, _id):
    employee=Employee.objects.get(id=_id)
    context={'employee':employee}
    
    return render(request,'dashboard/employee.html',context)
