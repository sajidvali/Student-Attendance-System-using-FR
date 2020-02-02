# Generated by Django 3.0.2 on 2020-02-02 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFR1', '0032_delete_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('Semester', models.CharField(max_length=5, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='allocate_classes',
            old_name='Faculty_Name',
            new_name='Faculty_ID',
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Attendance', jsonfield.fields.JSONField(default='')),
                ('Branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFR1.Branche')),
                ('Faculty_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFR1.Period')),
                ('Section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFR1.Section')),
                ('Semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFR1.Semester')),
                ('Studying_Year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFR1.StudyingYear')),
            ],
        ),
    ]
