from rest_framework import status, permissions
from django.http import Http404, JsonResponse
from users import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workshop
from .serializers import WorkshopSerializer
from django.contrib.auth import get_user_model

User = get_user_model() 

# Create your views here.
class WorkshopList(APIView):
    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(
            serializer.data,
        )
       
    def post(self, request):
        # request.data['owner'] = request.user.id
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
            # self.check_object_permissions(self.request, workshop)
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
        # print(user.is_python_mentor)
        # print(workshop.is_python_mentor)
        
        def skills_workshop_match(workshop,user):    #use and and not == as flase == false and will return true
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
            # serializer = WorkshopSerializer(data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            workshop.mentors.add(user) #add delete method and call .remove(user)
            return Response(
                    # serializer.data,
                {"result":"You have successfully signed up as a mentor"},
                status=status.HTTP_200_OK
            )
        return Response(
            {"result":"You must have a matching skill to the workshop to sign up!"},
            status=status.HTTP_400_BAD_REQUEST
        )



    # def delete(self, request, workshop_pk):
    #     workshop = self.get_object(workshop_pk)
    #     if workshop.owner == request.user:
    #         workshop.delete()
    #         return Response(
    #             {"data": {"result":"workshop has been deleted"}},
    #             status=status.HTTP_200_OK
    #         )
    #     return Response(
    #     {"result":"Unsuccessful - Workshop can only be deleted by the owner."},
    #     status=status.HTTP_400_BAD_REQUEST,
    #     )

      

