# Generated by Django 2.2.4 on 2019-09-30 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_teststatus'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='teststatus',
            name='username',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
