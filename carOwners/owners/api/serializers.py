from rest_framework import serializers
from owners.models import Owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('first_name','last_name','age','gender','car_model','car_model_year','car_vin','job_title','country' )