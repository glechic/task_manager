from datetime import datetime, timedelta
import celery

from django.core.mail import send_mail

from .models import Task, User


@celery.decorators.periodic_task(run_every=timedelta(days=1))
def send_email():
    for user in User.objects.all().prefetch_related('task_set'):
        tasks = user.task_set.filter(assigned_date__gt=(datetime.now() - timedelta(days=1)))
        if tasks.exists():
            task_list = '<br>'.join([f"<li>{ task.title }</li>" for task in user.task_set.all()])
            send_mail(
                'Newly assigned tasks',
                f'<h2>Task list:</h2><br>{task_list}',
                'my@email.com',
                [user.email],
                fail_silently=False,
            )
