from django.shortcuts import render
from .models import Employee,Device,AssetsReturn,Company
from .serailizer import EmployeeSerializers,DeviceSerializer,AssetsReturnSerailizer,compnaySerailizer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# send the email user email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

class EmployeeviewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class  = EmployeeSerializers

    @receiver(post_save, sender=Employee)
    def send_email_on_return_date(sender, instance, **kwargs):
        if instance.employee_return_data > timezone.now():
            email_subject = 'Reminder: Asset Return Date Exceeded'
            email_body =  render_to_string('reminder.html',{'employee_name' : instance.employee_name})

            email = EmailMultiAlternatives(email_subject,'',to=[instance.employee_email])
            email.attach_alternative(email_body,'text/html')
            email.send()


""" this is work now Deviece view """
class DeviceViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    
    serializer_class = DeviceSerializer


""" this is work now Deviece view """
class AssetsReturnViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AssetsReturn.objects.all()
    
    serializer_class = AssetsReturnSerailizer


""" this is work now Deviece view """
class companyViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    
    serializer_class = compnaySerailizer


