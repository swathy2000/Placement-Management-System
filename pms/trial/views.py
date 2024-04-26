from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import studymaterial,company,student,job,students_applied_details
from django.contrib.auth import authenticate,login,logout
from .forms import CompanyForm,JobForm,MaterialForm
import os
from django.views.decorators.csrf import csrf_exempt
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from trial.models import job
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from django.conf import settings



def new_register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user_type = request.POST.get('user_type')


        myuser=User.objects.create_user(username,email,password)
        myuser.last_name = user_type
        myuser.save()
        print(user_type)
        if user_type == 'tpc':
            myuser.is_staff = True
            # myuser.save()
            login(request,myuser)
            return redirect('tcpdash')
        else :
            return redirect('login')
    else:
            return render(request, 'newregister.html')


def new_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print("PRINT DATA<<<<<<<<<<",user.username,user.id,)
        request.session['student_id'] = user.id

        if user is not None:
            login(request, user)

            
            if user.last_name == 'tpc':
                return redirect('tcpdash')
            
            else:
                
                return redirect('userdash')
        else:

           return render(request, 'newlogin.html')
    else:
        return render(request,'newlogin.html')


@csrf_exempt
def user_dashboard(request):
     context = {}
     if 'student_id' in request.session:
        student_id = request.session['student_id']
        context['stud_id'] = student_id

        # Retrieve the placed students with their details
        try:
            student_obj = student.objects.get(student_id = student_id)
            shortlisted_students = students_applied_details.objects.filter(shortlisted_status='Y').filter(applied_student_id = student_obj)
            context['shortlisted_students'] = shortlisted_students
            placed_students = students_applied_details.objects.filter(placed_status='Y').filter(applied_student_id = student_obj)
            context['placed_students'] = placed_students
        except Exception as err:
            context['placed_students'] = []
            
            # Get the total number of registered companies
        registered_companies = company.objects.count()
        context['registered_companies'] = registered_companies

        # Get the total number of jobs applied by the student
        total_jobs_applied = students_applied_details.objects.filter(applied_student_id=student_obj).count()
        context['total_jobs_applied'] = total_jobs_applied
     else:
        context['error_message'] = "Session data missing. Please log in again."

     return render(request, 'user_dashboard.html', context=context)
   
@csrf_exempt
def tcp_dashboard(request):
    total_companies = company.objects.count()
    active_jobs = job.objects.filter(status='Active').count()
    total_students = student.objects.count()

    context = {
        'total_companies': total_companies,
        'active_jobs': active_jobs,
        'total_students': total_students,
    }
    return render(request, 'tcp_dashboard.html', context=context)

def add_details(request):
    print('mmmmmmmmmmmmmmmmmmmmmmmmm',request.session)
    print("student_id>><<",request.session['student_id'])
    stud_id = request.session['student_id']

    if request.method == 'POST':
        if request.FILES:
            uploaded_file = request.FILES.get('resume')
        print(request.POST)
        if  request.POST.get('actionItem') == 'E':
            student_obj = student.objects.get(student_id = stud_id)
        elif request.POST.get('actionItem') == 'N':
            student_obj = student()
            student_obj.student_id = stud_id
        student_obj.name = request.POST.get('name') if request.POST.get('name') != None else '' 
        student_obj.email = request.POST.get('email') if request.POST.get('email') != None else '' 
        student_obj.course = request.POST.get('course') if request.POST.get('course') != None else '' 
        student_obj.ph_no = request.POST.get('ph_no') if request.POST.get('ph_no') != None else '' 
        student_obj.dob = request.POST.get('dob') if request.POST.get('dob') != None else '1993-01-01'
        student_obj.gender = request.POST.get('gender') if request.POST.get('gender') != None else '' 
        student_obj.nationality = request.POST.get('nationality') if request.POST.get('nationality') != None else '' 
        student_obj.religion = request.POST.get('religion') if request.POST.get('religion') != None else '' 
        student_obj.caste = request.POST.get('caste') if request.POST.get('caste') != None else '' 
        student_obj.blood_group = request.POST.get('blood_group') if request.POST.get('blood_group') != None else '' 
        student_obj.address = request.POST.get('address') if request.POST.get('address') != None else '' 
        student_obj.city = request.POST.get('city') if request.POST.get('city') != None else '' 
        student_obj.state = request.POST.get('state') if request.POST.get('state') != None else '' 
        student_obj.skills = str(",".join( request.POST.getlist('skills') ))
        student_obj.reg_no_10 = request.POST.get('reg_no_10')
        student_obj.school_name_10 = request.POST.get('school_name_10')
        student_obj.passout_yr_10 = request.POST.get('passout_yr_10')
        student_obj.mark_10 = request.POST.get('mark_10')
        student_obj.reg_no_12 = request.POST.get('reg_no_12')
        student_obj.school_name_12 = request.POST.get('school_name_12')
        student_obj.passout_yr_12 = request.POST.get('passout_yr_12')
        student_obj.stream = request.POST.get('stream')
        student_obj.percentage_12 = request.POST.get('percentage_12')
        student_obj.graduation_university_Reg_no = request.POST.get('graduation_university_Reg_no')
        student_obj.graduated_college_name = request.POST.get('graduated_college_name')
        student_obj.graduated_branch = request.POST.get('graduated_branch')
        student_obj.graduated_passout_yr = request.POST.get('graduated_passout_yr')
        student_obj.graduated_cgpa = request.POST.get('graduated_cgpa')
        student_obj.existing_backlogs = request.POST.get('existing_backlogs')
        student_obj.masters_university_reg_no = request.POST.get('masters_university_reg_no')
        student_obj.masters_college_name = request.POST.get('masters_college_name')
        student_obj.masters_branch = request.POST.get('masters_branch')
        student_obj.masters_passout_yr = request.POST.get('masters_passout_yr')
        student_obj.masters_cgpa = request.POST.get('masters_cgpa')
        student_obj.masters_existing_backlogs = request.POST.get('masters_existing_backlogs')
        student_obj.resume = request.FILES.get('resume')

        student_obj.save()
        print("new func")
        updated_stud_skills = newlogin_matchingjobs(stud_id)
        print("students skills updated status",updated_stud_skills)

        return JsonResponse({
            'status':200,
            'message': 'Records has been added.'
        } , safe=False)
    else:
        student_data = student.objects.filter(student_id=stud_id)
        if len(student_data)>0:
            form = student_data.values()[0]
            action='E'
        else:
            form = student()
            action='N'
    

    return render(request, 'add_details.html'  , {'form': form,'action':action})



def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tcpdash')
    else:
        form = CompanyForm()
    return render(request, 'company_details.html' , {'form' : form})
    
    
def job_offer(request): 
    if request.method == 'POST':
        print("data>>>>>>>>>>>>>>>>",request.POST)
        if request.POST.get('actionItem') == 'E':
            job_id = request.POST.get('job_id')
            job_obj = job.objects.get(id=job_id)
            print("....",job_obj)
        elif request.POST.get('actionItem') == 'N':
            job_obj = job()
        job_obj.company =  company.objects.get( id = int(request.POST.get('company')) )
        
        job_obj.job_role = request.POST.get('job_role')

        print(",".join( request.POST.getlist('skills') ))
        job_obj.skills = str(",".join( request.POST.getlist('skills') ))
        job_obj.eligibility = request.POST.get('eligibility')
        job_obj.eligibility = str(",".join( request.POST.getlist('eligibility') ))

        job_obj.backlogs = request.POST.get('backlogs')
        job_obj.cgpa = request.POST.get('cgpa')
        job_obj.posted_date= request.POST.get('posted_date')

        job_obj.last_date = request.POST.get('last_date')
        job_obj.status = request.POST.get('status')
        job_obj.save()
        job_id = job_obj.id
        job_objs = job.objects.get(id=job_id)
        job_skills = job_objs.skills.split(',')
        matching_students = student.objects.none()  # Initialize an empty queryset
        for skill in job_skills:
            matching_students |= student.objects.filter(skills__contains=skill)
                        
        student_ids = [item for item in matching_students]
        if student_ids:
            for stud in student_ids:
                app_stud_obj=students_applied_details()
                app_stud_obj.applied_student_id = stud
                app_stud_obj.applied_job = job_objs
                app_stud_obj.status = 'N'
                app_stud_obj.save()             

        return redirect('tcpdash')
    else:
        job_id = request.GET.get('job_id')
        print("???????????????????????",request.GET)
        context={}
        job_action='N'
        if request.GET.get('action'):
            job_action='E'
            print(".......",job_action)
            job_data = job.objects.filter(id = int(job_id))
            print(job_data,len(job_data))
            data= job_data.values()[0]
            context['form'] = data
            context['action'] = 'E'
        else:
            context['form'] =  job()
            context['action'] = 'N'
        companyname = company.objects.all()  # Fetch all companies from the database
        context['companyname'] =companyname
        print("'''''''''''''''''''''''''''",context)
        return render(request, 'jobform.html', context)
    

def create_logout(request):
    logout(request)
    return redirect('login')


def test_yourself(request):
    if request.method == 'POST':
        
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('userdash')
    else:
        form = MaterialForm()
    return render(request, 'test_yourself.html', {'form': form,} )




def display_material(request):
    content = studymaterial.objects.all()
    print('jhh,,,,,,,,,,,,,,,,',request.user.username,request.user.last_name)

    return render(request, 'material.html',{'content':content})



def job_list(request):
    jobs = job.objects.all()
    return render(request, 'joblist.html', {'jobs':jobs})



@csrf_exempt
def matching_skills(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        try:
            
            app_stud_obj = students_applied_details.objects.filter(applied_job = job.objects.get(id = int(job_id)))
                            
            student_ids = [item.applied_student_id for item in app_stud_obj]
            stund_data  = [model_to_dict(stud) for stud in student_ids]
            for stud in stund_data:
                stud['resume'] = None
                attendence = students_applied_details.objects.filter(applied_job = job.objects.get(id = int(job_id))).filter(applied_student_id = student.objects.get(id = int(stud['id'])))
                stud['placement'] = {}
                stud['placement']['id'] = attendence[0].id
                stud['placement']['attendence_status'] = attendence[0].attendance or 'N'
                stud['placement']['attendence_status'] = stud['placement']['attendence_status'].upper()
                stud['placement']['placement_status'] = attendence[0].placed_status or 'N'
                stud['placement']['placement_status'] = stud['placement']['placement_status'].upper()
                stud['placement']['shortlisted_status'] = attendence[0].shortlisted_status or 'N'
                stud['placement']['shortlisted_status'] = stud['placement']['shortlisted_status'].upper()
                stud['placement']['status'] = attendence[0].status
                stud['placement']['status'] = stud['placement']['status'].upper()
            return JsonResponse(stund_data,safe=False)
        
        except job.DoesNotExist:
            return render(request, 'skill.html', {'error_message': 'Job does not exist'})
        
        except student.DoesNotExist:
            return render(request, 'skill.html', {'error_message': 'No students found with matching skills'})
    
    else:
        return render(request, 'skill.html', {'error_message': 'No found'})
    
        
@csrf_exempt
def update_stud_attendence(request):
    try:
        print("dddd")
        from trial.util import send_email
        response={}
        response['status'] = 400
        stud_id = request.POST.get('stud_att_id')
        stud_action_col = request.POST.get('stud_att_action')
        stud_action_value = request.POST.get('stud_att_value')
        stud_app_obj= students_applied_details.objects.get(id = int(stud_id))
        if stud_action_col =='psc':     
            print("..............")       
            stud_app_obj.placed_status = 'Y' if stud_action_value == 'true' else 'N'
            if stud_app_obj.placed_status == 'Y' and settings.SENT_EMAIL_ON_PLACEMENT:
                messageBody = """
                    Congratulations %s,
                    You have been placed on the company %s as %s,
                    You will receive further notification and response from the company.
                    Once again Congratulations.
                """ % (stud_app_obj.applied_student_id.name,stud_app_obj.applied_job.company.name , stud_app_obj.applied_job.job_role )
                send_email(stud_app_obj.applied_student_id.email,messageBody)
                
        elif stud_action_col =='ssc':
            print(">>>>>>>>>>>>>>")
            stud_app_obj.shortlisted_status = 'Y' if stud_action_value == 'true' else 'N' 
            if stud_app_obj.shortlisted_status == 'Y' and settings.SENT_EMAIL_ON_PLACEMENT:
                messageBody = """
                    Congratulations %s,
                    You have been shortlisted on the company %s as %s,
                    You will receive further notification and response from the company.
                    Once again Congratulations.
                """% (stud_app_obj.applied_student_id.name,stud_app_obj.applied_job.company.name , stud_app_obj.applied_job.job_role )
                send_email(stud_app_obj.applied_student_id.email,messageBody)

        elif stud_action_col =='asc':
            stud_app_obj.attendance = 'Y' if stud_action_value == 'true' else 'N' 
        stud_app_obj.save()
        
        
    except Exception as err:
        print(err)
        
    
    return JsonResponse(response)


def stud_job_details(request):

    print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",settings.SENT_EMAIL_ON_PLACEMENT)
    matching_jobs = []
    stud_id = student.objects.get(student_id=request.session['student_id'])
    
    student_ids = students_applied_details.objects.filter(applied_student_id =stud_id.id)
    print("stud data>>>>>>>>>>>>",student_ids)
    for std_app_id in student_ids:
        if std_app_id.applied_job.status == 'Active':
            matching_jobs.append(std_app_id)
           
    if matching_jobs:
        print("????????????????????",matching_jobs)
        
        return render(request, 'studjob.html', {'matching_jobs': matching_jobs})
    else:
        print("????????????????????",matching_jobs)
        return render(request, 'studjob.html', {'message': 'No active job details found for any student'})
    
@csrf_exempt
def update_application_status(request):
    if request.method == 'POST':
        student_id = request.POST.get("student_id")
        job_id = request.POST.get('job_id')
        try:
            _sad_filter = {
                'applied_student_id' : student.objects.get(id=int(student_id)),
                'applied_job_id' : job.objects.get(id = int(job_id))
            }
            print(_sad_filter)
            applied_student = students_applied_details.objects.get(**_sad_filter)
            if applied_student:
                applied_student.status = 'Y'
                applied_student.save()
                return JsonResponse({ 'status' : 'success' }) 
            else:
                return JsonResponse({'status': 'error', 'message': 'Student application not found'})
        except Exception as err:
            print(err)
            return JsonResponse({'status': 'error', 'message': str(err)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
    
def newlogin_matchingjobs(student_id):
    try:
        student_objs = student.objects.get(student_id=student_id)
        
        student_skills = student_objs.skills.split(',')

        existing_stud_dtls = students_applied_details.objects.filter(applied_student_id_id = student_objs).delete()
        print(student_skills)
        for skill in student_skills:
            matching_jobs = job.objects.filter(skills__contains = skill)
            for job_obj in matching_jobs:
                try:
                    app_stud_obj_filter = {
                        'applied_student_id' : student_objs,
                        'applied_job' : job_obj
                    }
                    app_stud_obj = students_applied_details.objects.get(**app_stud_obj_filter)
                except Exception as err:    
                    app_stud_obj = students_applied_details()
                app_stud_obj.applied_student_id = student_objs
                app_stud_obj.applied_job = job_obj
                app_stud_obj.status = 'N'
                app_stud_obj.save()
        return True  
    except Exception as err:
        return False  # Student with given id does not exist