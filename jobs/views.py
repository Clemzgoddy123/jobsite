from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from .models import Job, JobApplication
from .forms import JobApplicationForm, UserRegistrationForm


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        location = self.request.GET.get('location', '').strip()
        remote = self.request.GET.get('remote', '').lower()

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(company__icontains=q) | Q(description__icontains=q)
            )

        if location:
            queryset = queryset.filter(location__icontains=location)

        if remote in ('1', 'true', 'yes', 'on'):
            queryset = queryset.filter(is_remote=True)

        return queryset


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['application_submitted'] = self.request.GET.get('applied') == '1'
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('jobs:register') + '?next=' + request.path)
        
        self.object = self.get_object()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')

        if name and email:
            JobApplication.objects.create(
                job=self.object,
                name=name,
                email=email,
                phone=phone or '',
                cover_letter=cover_letter or '',
                resume=resume,
            )
            return redirect(reverse('jobs:job_detail', kwargs={'pk': self.object.pk}) + '?applied=1')

        return self.render_to_response(self.get_context_data())


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_url = request.GET.get('next', reverse('jobs:job_list'))
            return redirect(next_url)
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', reverse('jobs:job_list'))
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def landing(request):
    return render(request, 'landing.html')
