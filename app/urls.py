from app import views
from django.urls import path

urlpatterns = [
    path('',views.indexview,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('search',views.search,name='search'),
    
    path('jobs',views.jobs,name='jobs'),
    path('companies',views.companies,name='companies'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    
    # RESUME
    path('resume',views.resume,name='resume'), 
    path('show',views.show,name='show'),  
    path('edit/<int:id>',views.edit,name='edit'),  
    path('update/<int:id>',views.update,name='update'),  
    path('delete/<int:id>',views.destroy,name='destroy'), 
    
    # PROFILE
    path('profile',views.profile,name='profile'),
    path('profile_edit/<int:id>',views.profile_edit,name='profile_edit'),  
    path('profile_update/<int:id>',views.profile_update,name='profile_update'), 
    
    # EMPLOYEE
    path('employee',views.employee,name='employee'),
    path('post_a_job',views.post_a_job,name='post_a_job'),
    path('show_job',views.show_job,name='show_job'),  
    path('edit_job/<int:id>',views.edit_job,name='edit_job'),  
    path('update_job/<int:id>',views.update_job,name='update_job'),  
    path('delete_job/<int:id>',views.delete_job,name='destroy_job'), 
    
    path('register',views.registerview,name='register'),
    path('login',views.loginview,name='login'),
    path('logout',views.logoutview,name='logout'),
]