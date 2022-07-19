# pylint: disable=too-few-public-methods
from rest_framework import serializers
from jobs_app.models import Skill

class SkillSerializer(serializers.ModelSerializer):
    """
    This class serializes Post model.
    """
    class Meta:
        model = Skill
        fields = "__all__"
