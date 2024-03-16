from .models import Employee,AssetsReturn,Device,Company
from django.utils import timezone
from rest_framework import serializers



""" this Employee serializer here """


class EmployeeSerializers(serializers.ModelSerializer):

    employee_name = serializers.CharField(max_length=100,required=True)

    employee_email = serializers.EmailField(required=True)

    employee_current_address = serializers.CharField(max_length=100,required=True)

    employee_parmanent_address = serializers.CharField(max_length=100,required=True)

    employee_phone_number = serializers.CharField(max_length=18,required=True)

    employee_national_id_number =  serializers.CharField(max_length=18,required=True)

    employee_department_name = serializers.CharField(max_length=100,required=True)

    employee_parchased_data = serializers.DateTimeField(default=timezone.now)

    employee_return_data = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = Employee
        fields = '__all__'



""" this is Device serializer here """

class DeviceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Device
        fields = '__all__'




""" This is Assets Return serializer """


class AssetsReturnSerailizer(serializers.ModelSerializer):

    class Meta:
        model = AssetsReturn
        fields = "__all__"

""" This is company serializer """


class compnaySerailizer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"