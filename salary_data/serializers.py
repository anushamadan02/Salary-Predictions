from rest_framework import serializers
from salary_data.models import salary_data 

class SalaryDataSerializer(serializers.ModelSerializer):
    class Meta:
        managed = False
        model= salary_data 
        fields=(
                'Id', 'job_title', 'salary_estimate', 'job_description', 'rating',
                'company_name', 'location',	'headquarters',	'size', 'founded',
                'ownership_type', 'industry', 'sector', 'revenue',
                'competitors', 'hourly', 'employer_provided', 'min_salary', 
                'max_salary', 'avg_salary', 'company_txt','job_state'	,
                'same_state', 'age', 'python_yn', 'R_yn', 'spark','aws','excel'
            )


