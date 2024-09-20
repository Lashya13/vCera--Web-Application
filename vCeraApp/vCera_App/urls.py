from django.urls import path
from . import views
from .views import manager_open_position,manager_submit, HR_query

urlpatterns = [
    path('', views.login, name='login'),
    path('first_page/', views.first_page, name='first_page'),
    #path('manager_form/', views.manager_open_position, name='managerForm'),
    #path('manager_submit/', views.manager_submit, name='manager_submit'),
    path('query/', views.HR_query, name='HR_query'),
    path('employee/', views.employee, name='employee'),
    path('HR/', views.HR, name='HR'),
    #path('managers/', views.manager, name='managers'),
    path('pillar_query/', views.pillar_query_view, name='pillar_query'),
    path('HR_final/', views.HR_Final, name='HR_final'),
    #path('search/', views.search_page, name='search_page'),  # The main search page
    #path('ajax/load-job-ids/', views.load_job_ids, name='load_job_ids'),  # AJAX call to load Job IDs
    #path('ajax/load-job-details/', views.load_job_details, name='load_job_details'),  # AJAX call to load Job details
    #path('ajax/search-employees/', views.search_employees, name='search_employees'),  # AJAX call to search employees
    path('search/', views.hr_query, name='hr_query'),
    path('get-job-ids/', views.get_job_ids, name='get_job_ids'),
    path('get-job-details/', views.get_job_details, name='get_job_details'),
    path('manager/form/', views.manager_query, name='manager_query'),
    path('success/<str:job_id>/', views.manager_submit_view, name='success'), # Add a success page or another template
    path('chat/', views.chat, name='chat'),
] 
