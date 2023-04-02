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
        user = get_user_model()
        workshop = Workshop.objects.get(pk=workshop_pk)
        
        def skills_workshop_match(workshop,user):    
            if workshop.is_python_mentor == user.is_python_mentor:
                return True
            elif workshop.is_django_mentor == user.is_django_mentor:
                return True
            elif workshop.is_react_mentor == user.is_react_mentor:
                return True
            elif workshop.is_javascript_mentor == user.is_javascript_mentor:
                return True
            elif workshop.is_htmlcss_mentor == user.is_htmlcss_mentor:
                return True
            else:
                return False

        if skills_workshop_match(workshop, user) == True:
            serializer = WorkshopSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    {"result":"You have successfully signed up as a mentor"},
                    status=status.HTTP_200_OK
                )
        return Response(
            {"result":"You must have a matching skill to the workshop to sign up!"},
            status=status.HTTP_400_BAD_REQUEST
        )

  ## function workshop skills == user skills 
        ## views serialise the mentors field > return success
        ##  else error message



    # def put(self, request, workshop_pk):
    #     workshop = self.get_object(workshop_pk)
    #     data = request.data
    #     if workshop.owner == request.user:
    #         serializer = WorkshopDetailSerializer(
    #             instance=workshop,
    #             data=data,
    #             partial=True
    #         )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             serializer.data # can also replace with a personalised message for a successful update
    #         )
    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )

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

      



#attempting workshop_mentor view so FE can return a response telling the user they have signed up. 
# user can only sign up if they have a matching skillset
## pseudo code for WorkshopMentors model

# class WorkshopMentorsDetail(APIView):
#     permission_classes = [
#         permissions.IsOwner,        
#     ]

#     # def get(self):
#     #     WorkshopMentors = WorkshopMentors.objects.all() #do we have to filter for a particular workshop?
#     #     serializer = WorkshopMentorsSerializer(WorkshopMentors)
#     #     return Response(serializer.data)

#     def get_object(self,mentor_pk):
#         try:
#             WorkshopMentors = WorkshopMentors.objects.get(pk=mentor_pk)
#             self.check_object_permissions(self.request, WorkshopMentors)
#             return WorkshopMentors
#         except WorkshopMentors.DoesNotExist:
#             raise Http404

#     def post(self, request, mentor_pk):
#         mentor = self.get_object(mentor_pk)
#         serializer = WorkshopMentorsSerializer(mentor)
#         # if mentor.mentor == request.user & mentor.skills == workshops.skills: ## how do i make it so that python mentor can only sign up for python workshops?
#         if mentor.mentor == request.user & mentor.skills:
#             mentor.save()
#             return Response(
#                 serializer.data,
#                 {"You are signed up as a mentor"},
#                 status = status.HTTP_201_CREATED,
#             )
#         return Response(
#             serializer.errors,
#             {"Oh no, we could not register you as a mentor. Please make sure you are logged in and have a matching skillset to the skill the workshop is for"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )