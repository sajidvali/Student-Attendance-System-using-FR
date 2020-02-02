# Generated by Django 3.0.2 on 2020-02-02 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFR1', '0027_delete_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faculty_ID', models.CharField(max_length=20)),
                ('Faculty_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Faculty', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
