from django.utils import timezone
from .models import Course
from django.shortcuts import render, get_object_or_404
from .forms import CourseForm
from django.shortcuts import redirect
from .forms import SearchForm
from datetime import datetime


def course_list(request):
    courses = Course.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'catalog/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'catalog/course_detail.html', {'course': course})


def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.published_date = timezone.now()
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'catalog/course_edit.html', {'form': form})


def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.published_date = timezone.now()
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'catalog/course_edit.html', {'form': form})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return render(request, 'catalog/course_deleted.html')


def course_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_title = form.clean()['title']
            search_description = form.clean()['description']
            search_start_date = form.clean()['start_date']
            search_start_date_is_greater_or_equal_to = form.clean()['start_date_is_greater_or_equal_to']
            search_start_date_is_less_or_equal_to = form.clean()['start_date_is_less_or_equal_to']
            filter_parameters = {}
            if search_title:
                filter_parameters['title__icontains'] = search_title
            if search_description:
                filter_parameters['text__icontains'] = search_description
            if search_start_date:
                filter_parameters['start_date'] = search_start_date
            if search_start_date_is_greater_or_equal_to:
                filter_parameters['start_date__gte'] = search_start_date_is_greater_or_equal_to
            if search_start_date_is_less_or_equal_to:
                filter_parameters['start_date__lte'] = search_start_date_is_less_or_equal_to
            courses = Course.objects.filter(**filter_parameters).order_by('published_date')
            return render(request, 'catalog/course_list.html', {'courses': courses})
    else:
        form = SearchForm()
    return render(request, 'catalog/course_search.html', {'form': form})
