from rest_framework import serializers
from .models import Curriculum, Education, Experience


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class CurriculumSerializer(serializers.ModelSerializer):
    educations=EducationSerializer(many=True, read_only=True)
    experiences=ExperienceSerializer(many=True, read_only=True)
    class Meta:
        model = Curriculum
        fields = '__all__'



