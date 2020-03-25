from .models import Profile,User_Attendance
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user_name', 'name', 'email', 'phone']


class UserAttendanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many = False,queryset = Profile.objects.all())
    class Meta:
        model = User_Attendance
        fields = ['user','is_present', 'present_time', 'exit_time']

