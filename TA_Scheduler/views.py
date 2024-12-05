from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.views.generic import TemplateView

from TA_Scheduler.models import Course


class LoginPageView(TemplateView):
    template_name = 'LoginPage.html'


class HomePageView(TemplateView):
    template_name = 'homePage.html'

class CreateAccountPageView(TemplateView):
    template_name = 'create-account.html'

class EditAccountPageView(TemplateView):
    template_name = 'edit-account.html'

class coursesPageView(TemplateView):
    template_name = 'courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all courses from the database
        context['courses'] = Course.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        # Handle course deletion
        delete_course_id = request.POST.get("delete_course_id")
        if delete_course_id:
            course = Course.objects.get(course_id=delete_course_id)
            course.delete()

        return redirect("courses")  # Redirect back to the same page
class CreateCoursePageView(TemplateView):
    template_name = 'create-course.html'

    def post(self, request, *args, **kwargs):
        # Get course details from the POST request
        course_name = request.POST.get('course_name')
        course_code= request.POST.get('course_code')
        course_sem = request.POST.get('course_sem')
        # course_instructor = request.POST.get('course_instructor')
        if course_name and course_code and course_sem :
            # Create and save a new course
            Course.objects.create(course_name=course_name, course_code=course_code, course_sem= course_sem)
        # Redirect back to the courses page
        return HttpResponseRedirect(reverse('courses'))

class AssignPageView(TemplateView):
    template_name = 'assign-people.html'

class NotificationsView(TemplateView):
    template_name = 'Notifications.html'


# Create your views here.