from rest_framework import status, permissions
from django.http import Http404, JsonResponse
from users import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workshop
from .serializers import WorkshopSerializer
from django.contrib.auth import get_user_model

User = get_user_model() 

class WorkshopList(APIView):
    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(
            serializer.data,
        )
       
    def post(self, request):
        serializer = WorkshopSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class WorkshopDetail(APIView):
    permission_classes = [
        permissions.IsOwner,        
    ]

    def get_object(self,workshop_pk):
        try:
            workshop = Workshop.objects.get(pk=workshop_pk)
            return workshop
        except Workshop.DoesNotExist:
            raise Http404

    def get(self, request, workshop_pk):
        workshop = self.get_object(workshop_pk)
        serializer = WorkshopSerializer(workshop)
        return Response(serializer.data)

    def post(self, request, workshop_pk):
        user = request.user
        workshop = Workshop.objects.get(pk=workshop_pk)
        
        def skills_workshop_match(workshop,user):  
            if workshop.is_python_mentor and user.is_python_mentor:
                return True
            elif workshop.is_django_mentor and user.is_django_mentor:
                return True
            elif workshop.is_react_mentor and user.is_react_mentor:
                return True
            elif workshop.is_javascript_mentor and user.is_javascript_mentor:
                return True
            elif workshop.is_htmlcss_mentor and user.is_htmlcss_mentor:
                return True
            else:
                return False

        if skills_workshop_match(workshop, user):
            workshop.mentors.add(user)
            return Response(
                {"result":"You have successfully signed up as a mentor"},
                status=status.HTTP_200_OK
            )
        return Response(
            {"result":"You must have a matching skill to the workshop to sign up!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, workshop_pk):
        user = request.user
        workshop = Workshop.objects.get(pk=workshop_pk)
        try:
            workshop.mentors.remove(user)
            return Response(
                {"result":"You have been removed as a mentor"},
                status=status.HTTP_200_OK
            )
        except:
            raise Response(
                {"result":"Unsuccessful - Please try again."},
                status=status.HTTP_400_BAD_REQUEST,
            )

      

