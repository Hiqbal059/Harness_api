# pylint: disable=too-few-public-methods
from rest_framework import serializers
from jobs_app.models import Job
from jobs_app.serializers import SkillSerializer

class JobSerializer(serializers.ModelSerializer):
    """
    This class serializes Post model.
    """
    skills = SkillSerializer(many=True, source="skills")

    class Meta:
        model = Job
        fields = ("title", "description", "skills")
