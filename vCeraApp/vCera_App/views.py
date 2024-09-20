from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .forms import MangerOpenPosition, HRQueryForm, PillarQueryForm, PillarSearchForm, JobIDForm
from .models import Employee, manager_form
from django.contrib import messages
from django.shortcuts import render
from .chatbot_logic import get_bot_response


def login(request):
    
    return render(request , template_name='vCera/login.html')

def first_page(request):
    return render(request , template_name='vCera/first_page.html')

def employee(request):
    return render(request , template_name='vCera/employee.html')

def HR(request):
    return render(request , template_name='vCera/HR.html')

def HR_Final(request):
    return render(request , template_name='vCera/HR_Final.html')
#def manager(request):
#    return render(request , template_name='vCera/managers.html')

def manager_open_position(request):
    if request.method == 'POST':
        form = ManagerOpenPosition(request.POST)
        if form.is_valid():
            saved_data =form.save()  # Save the data to the database
            return redirect('success')  # Redirect to a success page or elsewhere
            #return render(request, 'vCera/manager_submit.html', {'job_id': saved_data.JobID})
        else:
            # If the form is not valid, re-render the form with errors
            print(form.errors)
            #return render(request, 'Vcera/managers.html', {'form': form})
            return render(request, 'Vcera/manager_form.html', {'form': form})

            
    else:
        form = MangerOpenPosition()
        #return render(request, 'vCera/managers.html', {'form': form})
        return render(request, 'vCera/manager_form.html', {'form': form})

def manager_submit(request):

    if request.method == 'POST':
        # Process the form
        job_id = request.POST.get('JobID')  # Assuming 'JobID' is the name of the input field
        # Save the form or perform some action with the data
        # For example:
        # manager_form = ManagerForm(JobID=job_id, ...) # Add other fields as necessary
        # manager_form.save()

        # Pass the JobID to the next page (template)
        #return render(request, 'vCera/manager_submit.html', {'job_id': job_id})
        return render(request, 'vCera/success.html', {'job_id': job_id})


    #return render(request, 'vCera/manager_submit.html')
    return render(request, 'vCera/success.html')

# HR search in manager record
def HR_query(request):
    form = HRQueryForm(request.GET or None)
    results = []

    if form.is_valid():
        # Get the cleaned data from the form
        cleaned_data = form.cleaned_data

        # Build the query
        query = Employee.objects.all()
        if cleaned_data.get('pillar'):
            query = query.filter(pillar__icontains=cleaned_data['pillar'])
        if cleaned_data.get('primary_skills'):
            query = query.filter(primary_skills__icontains=cleaned_data['primary_skills'])
        if cleaned_data.get('secondary_skills'):
            query = query.filter(primary_skills__icontains=cleaned_data['primary_skills'])
        if cleaned_data.get('location'):
            query = query.filter(location__icontains=cleaned_data['location'])
        if cleaned_data.get('experience'):
            query = query.filter(location__icontains=cleaned_data['location'])
        

        results = query
        
    #return render(request, 'vCera/HR_query.html', {'form': form, 'results': results})
    return render(request, 'vCera/HR_query.html', {'form': form, 'results': results})

#HR search in manager record
def pillar_query_view(request):
    jobs = None
    form = PillarQueryForm()

    if request.method == 'POST':
        form = PillarQueryForm(request.POST)
        if form.is_valid():
            selected_pillar = form.cleaned_data['pillar']
            jobs = manager_form.objects.filter(Pillar=selected_pillar)

    return render(request, 'vCera/pillar_query.html', {'form': form, 'jobs': jobs})
    #return render(request, 'vCera/hr_demo.html', {'form': form, 'jobs': jobs})
    
'''
# Main view for the form
def search_page(request):
    pillar_form = PillarSearchForm()
    job_form = JobIDForm()

    return render(request, 'vCera/search.html', {
        'pillar_form': pillar_form,
        'job_form': job_form,
    })

# AJAX to load JobIDs based on the selected Pillar
def load_job_ids(request):
    pillar = request.GET.get('Pillar')
    jobs = ManagerForm.objects.filter(Pillar=pillar).values('id', 'JobID')
    return JsonResponse(list(jobs), safe=False)

# AJAX to auto-fill job details when JobID is selected
def load_job_details(request):
    job_id = request.GET.get('JobID')
    job = ManagerForm.objects.get(id=job_id)
    data = {
        'JobTitle': job.JobTitle,
        'PrimarySkills': job.PrimarySkills,
        'SecondarySkills': job.SecondarySkills,
        'Location': job.Location,
        'Experience': job.Experience,
        
    }
    return JsonResponse(data)

# View to search employees based on the selected job details
def search_employees(request):
    job_id = request.GET.get('JobID')
    job = ManagerForm.objects.get(id=job_id)

    # Filter employees based on the selected job criteria
    employees = Employee.objects.filter(
        primary_skills__icontains=job.PrimarySkills,
        secondary_skills__icontains=job.SecondarySkills,
        experience__icontains=job.Experience,
        location__icontains=job.Location,
    )

    return render(request, 'employee_list.html', {'employees': employees})
'''

def hr_query(request):
    if request.method == 'POST':
        # Get the form data
        pillar = request.POST.get('pillar')
        #job_title = request.POST.get('jobTitle')
        primary_skills = request.POST.get('primarySkills')
        secondary_skills = request.POST.get('secondarySkills')
        location = request.POST.get('location')
        experience = request.POST.get('experience')

        # Query the Employee table based on these job details
        employees = Employee.objects.filter(
            pillar=pillar,
            primary_skills__icontains=primary_skills,
            secondary_skills__icontains=secondary_skills,
            location__icontains=location,
            experience__icontains=experience
        )

        # Redirect to the employee list page with the filtered employees
        return render(request, 'vCera/employee_list.html', {'employees': employees})

    if request.method == 'POST':
        # Process form submission and return relevant employee details
        pass

    # Get all unique pillars from the manager_form model
    pillars = manager_form.objects.values_list('Pillar', flat=True).distinct()
    return render(request, 'vCera/HR_Final.html', {'pillars': pillars})

def get_job_ids(request):
    pillar = request.GET.get('pillar')
    job_ids = manager_form.objects.filter(Pillar=pillar).values_list('JobID', flat=True)
    return JsonResponse({'job_ids': list(job_ids)})

def get_job_details(request):
    job_id = request.GET.get('job_id')
    job = manager_form.objects.get(JobID=job_id)
    data = {
        'job_title': job.JobTitle,
        'primary_skills': job.PrimarySkills,
        'secondary_skills': job.SecondarySkills,
        'location': job.Location,
        'experience': job.Experience
    }
    return JsonResponse(data)

def manager_query(request):
    if request.method == 'POST':
        # Get data from the form fields
        pillar = request.POST.get('pillar')
        job_id = request.POST.get('jobID')
        job_title = request.POST.get('jobTitle')
        primary_skills = request.POST.get('primarySkills')
        secondary_skills = request.POST.get('secondarySkills')
        certifications = request.POST.get('certifications')
        location = request.POST.get('location')
        experience = request.POST.get('experience')

        print(f"Received form data: jobID={job_id}, pillar={pillar}")
        if not job_id:
            messages.error(request, "Job ID cannot be empty.")
            return render(request, 'vCera/managers.html')
        #  Save the data to the database
        try:

            new_job=manager_form.objects.create(
                Pillar=pillar,
                JobID=job_id,
                JobTitle=job_title,
                PrimarySkills=primary_skills,
                SecondarySkills=secondary_skills,
                Certifications=certifications,
                Location=location,
                Experience=experience
            )
        
        # Redirect or display a success message
            messages.success(request, "Job position added successfully!")
            return redirect('success',job_id=new_job.JobID)  # Or another view/template to confirm success
        except Exception as e:
            print(f"Error saving job: {e}")
            messages.error(request, "An error occurred while saving the job position.")
            return render(request, 'vCera/managers.html')

    # If GET request, render the form
    return render(request, 'vCera/managers.html')

def manager_submit_view(request, job_id):
    return render(request, 'vCera/manager_submit.html', {'job_id': job_id})


def chat(request):
    if request.method == 'GET':
        user_message = request.GET.get('message', '').strip()
        step = int(request.GET.get('step', 1))  # track the conversation step
        bot_response = get_bot_response(user_message, step)
        return JsonResponse(bot_response)
    return render(request, 'vCera/chatbot.html')