
from Harness_api.jobs_app import serializers
from jobs_app.models import Job
from jobs_app.serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

class JobListApiView(APIView):
    """
    This class handles the request for jobs list
    """
    def get(self, request):
        """
        This method returns the jobs list
        """
        jobs = Job.objects.all()
        if jobs:
            serializerd_jobs = JobSerializer(jobs, many=True)
            return JsonResponse({"Students List": serializerd_jobs.data}, status=status.HTTP_200_OK)
        return JsonResponse({"messsage": "No Students exist yet"})
