from django.db import models


class student(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    course = models.CharField(max_length=256)
    ph_no = models.CharField(max_length=256)
    dob = models.DateField(auto_now=True, null=True, blank=True)
    gender = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    religion = models.CharField(max_length=256)
    caste = models.CharField(max_length=256)
    blood_group = models.CharField(max_length=256)
    address = models.TextField()
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    skills = models.TextField()
    reg_no_10 = models.CharField(max_length=256)
    school_name_10 = models.CharField(max_length=256)
    passout_yr_10 = models.CharField(max_length=256)
    mark_10 = models.CharField(max_length=256)
    reg_no_12 = models.CharField(max_length=256)
    school_name_12 = models.CharField(max_length=256)
    passout_yr_12 = models.CharField(max_length=256)
    stream = models.CharField(max_length=256)
    percentage_12 = models.CharField(max_length=256)
    graduation_university_Reg_no = models.CharField(max_length=256)
    graduated_college_name = models.CharField(max_length=256)
    graduated_branch = models.CharField(max_length=256)
    graduated_passout_yr = models.CharField(max_length=256)
    graduated_cgpa = models.CharField(max_length=256)
    existing_backlogs = models.CharField(max_length=256)
    masters_university_reg_no = models.CharField(max_length=256)
    masters_college_name = models.CharField(max_length=256)
    masters_branch = models.CharField(max_length=256)
    masters_passout_yr = models.CharField(max_length=256)
    masters_cgpa = models.CharField(max_length=256)
    masters_existing_backlogs = models.CharField(max_length=256)
    resume = models.FileField(upload_to="news/",max_length=1000,null=True, default=None)
    student_id = models.CharField(max_length=256,null=True,blank=True)
    
   
    class Meta:
        db_table = 'student'


class company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'     


class job(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    job_role = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    backlogs = models.IntegerField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    posted_date = models.DateField()
    last_date = models.DateField()
    status = models.CharField(max_length=50)



    class Meta:
        db_table = 'job' 


class studymaterial(models.Model):
    title = models.CharField(max_length=100)
    material = models.FileField(upload_to='study_materials/')
    links = models.URLField()
    date = models.DateField(auto_now_add=True) 
    description = models.CharField(max_length=200) 

    class Meta:
        db_table = 'studymaterial'


class students_applied_details(models.Model):
    applied_student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    applied_job = models.ForeignKey(job, on_delete=models.CASCADE)
    placed_date = models.DateField(blank=True, null=True)
    attendance = models.CharField(max_length=100,blank=True, null=True)
    placed_status = models.CharField(max_length=100,blank=True, null=True)
    shortlisted_status = models.CharField(max_length=100,blank=True, null=True)
    status = models.CharField(max_length=100)
    field1 = models.CharField(max_length=100, blank=True, null=True)
    field2 = models.CharField(max_length=100, blank=True, null=True)
    field3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'students_applied_details'




















