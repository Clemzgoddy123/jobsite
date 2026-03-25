from django.core.management.base import BaseCommand

from jobs.models import Job


class Command(BaseCommand):
    help = "Seed the database with example job listings."

    def handle(self, *args, **options):
        sample_jobs = [
            {
                'title': 'Senior Django Backend Engineer',
                'company': 'Nimbus Labs',
                'location': 'Remote',
                'is_remote': True,
                'salary_min': 90000,
                'salary_max': 130000,
                'description': (
                    'Build and maintain APIs and services for a fast-growing SaaS product. '
                    'You will own features end-to-end and collaborate with design and product teams.'
                ),
                'apply_url': 'https://example.com/jobs/django-backend-engineer',
            },
            {
                'title': 'Product Designer',
                'company': 'BrightWave',
                'location': 'San Francisco, CA',
                'is_remote': False,
                'salary_min': 85000,
                'salary_max': 110000,
                'description': (
                    'Design intuitive experiences for an enterprise collaboration platform. '
                    'Bring your craft to a tight-knit product team shipping weekly.'
                ),
                'apply_url': 'https://example.com/jobs/product-designer',
            },
            {
                'title': 'Data Analyst',
                'company': 'Atlas Insights',
                'location': 'New York, NY',
                'is_remote': False,
                'salary_min': 70000,
                'salary_max': 95000,
                'description': (
                    'Interpret data, build dashboards, and work with stakeholders to drive product decisions.'
                    ' Familiarity with SQL and modern BI tools is a plus.'
                ),
                'apply_url': 'https://example.com/jobs/data-analyst',
            },
        ]

        created = 0
        for job_data in sample_jobs:
            job, _ = Job.objects.get_or_create(
                title=job_data['title'],
                company=job_data['company'],
                defaults=job_data,
            )
            if _:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Seeded {created} job(s)."))
