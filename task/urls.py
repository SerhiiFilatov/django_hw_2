



from django.urls import path
from task.views import *

urlpatterns = [
    path('', ex_login, name='login'),
    path('list', ex_list, name='list'),
    path('reg/', ex_reg, name='reg'),
    path('<int:id>/', task_list, name='det_list'),

]

handler404 = pageNotfound