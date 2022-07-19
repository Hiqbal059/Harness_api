from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from jobs_app.models import Job, Skill
from jobs_app.serializers import JobSerializer, SkillSerializer
from django.http import JsonResponse

class JobApiView(APIView):
    """
    This class handles the actions about jobs
    """
    def post(self, request):
        """
        This method create a object for job
        """
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, **kwargs):
        """
        this method returns the student data with given id
        """
        student_id = kwargs["id"]
        if student_id:
            try:
                student = Skill.objects.get(id=student_id)
                serialzed_student = SkillSerializer(instance=student)
                return JsonResponse({"data": serialzed_student.data}, status=status.HTTP_200_OK)
            except Skill.DoesNotExist:
                return Response({"message": "No student exist againt given id"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Please enter an ID to proceed"}, status=status.HTTP_400_BAD_REQUEST)
