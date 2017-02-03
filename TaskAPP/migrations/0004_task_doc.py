# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskAPP', '0003_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='doc',
            field=models.FileField(default=b'Doc/None/No-doc.pdf', upload_to=b'Doc/'),
        ),
    ]
