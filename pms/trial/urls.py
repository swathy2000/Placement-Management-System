# urls.py
from django.urls import path,re_path
from trial.views import new_login , new_register ,user_dashboard , add_details , create_company ,  job_offer , create_logout , test_yourself , tcp_dashboard , display_material , matching_skills, job_list ,update_stud_attendence , stud_job_details ,update_application_status 
import trial.views as Tviews
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', new_login, name='login'),

    path('registration/', new_register, name='registration'),

    path('userdashboard/' , user_dashboard , name='userdash'),

    path('tcpdashboard/' , tcp_dashboard , name='tcpdash'),

    path('adddetails/' , add_details , name='details'),

    path('companydetails/' , create_company , name='company'),

    path('joboffer/' , job_offer , name='jobof'),

    path('logout/' , create_logout , name='logout'),

    path('test/' , test_yourself , name='testyourself'),

    path('studsmaterial/' , display_material , name='studmaterial'),

    path('matchingskills/' , matching_skills, name='match'),

    path('job_list/', job_list , name='job_list') ,

    path('update_stud_attendence/', update_stud_attendence , name='update_stud_attendence') ,

    path('studjobdetails/' , stud_job_details , name='studjoblist') ,

    path('update_application_status/', Tviews.update_application_status, name='update_application_status'),
    
    path('newlogin_matchingjobs/', Tviews.newlogin_matchingjobs, name='newlogin_matchingjobs'),



  


    





   



    


    

    
    
    

    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]

