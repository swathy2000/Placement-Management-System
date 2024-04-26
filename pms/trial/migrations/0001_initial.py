# Generated by Django 3.2 on 2024-03-27 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=100)),
                ('ph_no', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('caste', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('reg_no_10', models.CharField(max_length=100)),
                ('school_name_10', models.CharField(max_length=100)),
                ('passout_yr_10', models.CharField(max_length=4)),
                ('mark_10', models.CharField(max_length=10)),
                ('reg_no_12', models.CharField(max_length=100)),
                ('school_name_12', models.CharField(max_length=100)),
                ('passout_yr_12', models.CharField(max_length=4)),
                ('stream', models.CharField(max_length=100)),
                ('percentage_12', models.CharField(max_length=10)),
                ('graduation_university_Reg_no', models.CharField(max_length=100)),
                ('graduated_college_name', models.CharField(max_length=100)),
                ('graduated_branch', models.CharField(max_length=100)),
                ('graduated_passout_yr', models.CharField(max_length=4)),
                ('graduated_cgpa', models.CharField(max_length=5)),
                ('existing_backlogs', models.CharField(max_length=10)),
                ('masters_university_reg_no', models.CharField(max_length=100)),
                ('masters_college_name', models.CharField(max_length=100)),
                ('masters_branch', models.CharField(max_length=100)),
                ('masters_passout_yr', models.CharField(max_length=4)),
                ('masters_cgpa', models.CharField(max_length=5)),
                ('masters_existing_backlogs', models.CharField(max_length=10)),
                ('resume', models.FileField(default=None, max_length=250, null=True, upload_to='news/')),
                ('student_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='studymaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('material', models.FileField(upload_to='study_materials/')),
                ('links', models.URLField()),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'studymaterial',
            },
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('backlogs', models.IntegerField()),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('posted_date', models.DateField()),
                ('last_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trial.company')),
            ],
            options={
                'db_table': 'job',
            },
        ),
    ]
