from rest_framework import serializers
from django.conf import settings
from rest_framework.exceptions import ValidationError

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")
        
    def validate_students(self, value):
        if len(value) > settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError(
                f'На курсе не может быть больше чем {settings.MAX_STUDENTS_PER_COURSE} студентов'
            )
        return value