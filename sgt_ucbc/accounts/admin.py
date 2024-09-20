from django.contrib import admin
from .models import User
from .models import *
admin.site.register(FacultyProfile)
admin.site.register(StudentProfile)
admin.site.register(DirectorProfile)
admin.site.register(SupervisorProfile)
admin.site.register(AdminProfile)



