from django.db import models
from django.urls import reverse


class Job(models.Model):
    """A job listing that users can search and apply to."""

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    is_remote = models.BooleanField(default=False)
    salary_min = models.PositiveIntegerField(blank=True, null=True)
    salary_max = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    apply_url = models.URLField(blank=True)

    class Meta:
        ordering = ['-posted_at']
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return f"{self.title} @ {self.company}"

    def get_absolute_url(self):
        return reverse('jobs:job_detail', kwargs={'pk': self.pk})


class JobApplication(models.Model):
    """An application submitted by a user for a job."""

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-applied_at']
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'

    def __str__(self):
        return f"{self.name} applied for {self.job.title}"
