# Generated by Django 3.2.12 on 2022-07-24 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_student_info_deparment_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff_info',
            fields=[
                ('staff_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=200)),
                ('fathers_name', models.CharField(max_length=200)),
                ('mothers_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=200, null=True)),
                ('pre_addresss', models.CharField(blank=True, max_length=200, null=True)),
                ('per_address', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('BloodGroup', models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=20, null=True)),
                ('deparment_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.deparment_info')),
            ],
        ),
    ]