from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.db.models import Subquery
from . forms import HelperForm,CustomerForm

# Create your views here.

def home(request):
    return render(request,'home.html')


def all_helper(request):
    helper = Helper.objects.all()
    context ={'helpers':helper}
    return render(request,'all_helper.html',context)

def add_helper(request):
    if request.method == 'POST':
        form = HelperForm(request.POST)
        if form.is_valid():
            print("form valid")
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']

            skills = form.cleaned_data.get('skills', [])
            # skills = form.cleaned_data['skills']
            print(skills)
            # skill_list = request.POST.getlist('skills')
            # Create helper object
            helper = Helper.objects.create(name=name, gender=gender, age=age)            
            # Set skills for the helper
            # skills = [Skill.objects.get_or_create(name=skill)[0] for skill in skill_list]
            helper.skills.set(skills)
            helper.save()
            # Display success message
            messages.success(request, 'Helper added successfully!')            
            return redirect('add_helper')
        else:
            print("form Invalid")
            skills = Skill.objects.all()
            context = {
                'skills': skills,
                'form': form
            }
            return render(request, 'add_helper.html', context)

    else:
        form = HelperForm()
        skills=Skill.objects.all()
        context ={
            'skills':skills,
            'form': form
        }
        return render(request, 'add_helper.html',context)

def all_customers(request):
    customer = Customer.objects.all()
    context ={'customers':customer}
    return render(request,'all_customers.html',context)


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Helper added successfully!') 
            return redirect('add_customer')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def assign_helper(request):

    if request.method == 'POST':
        helper_id = request.POST.get('helper')
        print(helper_id)
        customer_id = request.POST.get('customer')
        print(customer_id)
        # Retrieve helper and customer objects
        helper = Helper.objects.get(pk=helper_id)
        
        customer = Customer.objects.get(pk=customer_id)
        print("customer_deta",customer)

        helper.assigned_customer = customer
        customer.assigned_helper = helper

        helper.save()
        customer.save()

        assignment = Assignment.objects.create(helper=helper, customer=customer)

        return redirect('home')

    helpers = Helper.objects.filter(assigned_customer__isnull = True)
    customers = Customer.objects.filter(assigned_helper__isnull = True)
    print(helpers)
    customer  = Customer.objects.all()
    context={
        'helpers':helpers,
        'customers':customers
    }   
    return render(request,'assign_helper.html',context)

def free_helper(request):

    free_helpers = Helper.objects.filter(assigned_customer__isnull = True)
    context ={'free_helpers':free_helpers}
    return render(request,'all_free_helper.html',context)
