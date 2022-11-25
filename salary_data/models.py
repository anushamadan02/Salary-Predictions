from django.db import models

# Create your models here.
class salary_data(models.Model):
    Id = models.AutoField(primary_key=True)
    job_title=models.CharField(max_length=2555)
    salary_estimate	=models.CharField(max_length=2555)
    job_description	=models.CharField(max_length=2555)
    rating	=models.CharField(max_length=2555)
    company_name =models.CharField(max_length=2555)
    location =models.CharField(max_length=2555)
    headquarters =models.CharField(max_length=2555)	
    size	=models.CharField(max_length=2555)
    founded	=models.CharField(max_length=2555)
    ownership_type	=models.CharField(max_length=2555)
    industry=models.CharField(max_length=2555)
    sector	=models.CharField(max_length=2555)
    revenue	=models.CharField(max_length=2555)
    competitors	=models.CharField(max_length=2555)
    hourly	=models.CharField(max_length=2555)
    employer_provided	=models.CharField(max_length=2555)
    min_salary = models.CharField(max_length=2555)
    max_salary	= models.CharField(max_length=2555)
    avg_salary	=models.CharField(max_length=2555)
    company_txt	 =models.CharField(max_length=2555)
    job_state	=models.CharField(max_length=2555)
    same_state =models.CharField(max_length=2555)
    age	=models.CharField(max_length=2555)
    python_yn =models.CharField(max_length=2555)
    R_yn =models.CharField(max_length=2555)
    spark=models.CharField(max_length=2555)
    aws	=models.CharField(max_length=2555)
    excel =models.CharField(max_length=2555)
        

        
