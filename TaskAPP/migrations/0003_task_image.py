# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskAPP', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default=b'Images/None/No-img.jpg', upload_to=b'Images/'),
        ),
    ]
