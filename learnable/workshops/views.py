from rest_framework import status, permissions
from django.http import Http404, JsonResponse
from users import permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Workshop
from .serializers import WorkshopSerializer, WorkshopDetailSerializer
# from .models import Workshop, WorkshopSignups
# from .serializers import WorkshopSerializer, WorkshopDetailSerializer, WorkshopSignupsDetailSerializer, WorkshopSignupsSerializer


# Create your views here.
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
            serializer.save(owner=request.user)
            # if workshop.is_open and workshop.current_mentor_num < workshop.max_mentor_num:
            #     workshop.current_mentor_num += 1
            #     workshop.save()
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
        # attempting current_mentor_num
        # mentor_count = workshop.current_mentor_num.aggregate(count=Count('id'))['count']
        # data = serializer.data
        # data['mentor_count'] = mentor_count
        return Response(serializer.data)

    def put(self, request, workshop_pk):
        workshop = self.get_object(workshop_pk)
        data = request.data
        if workshop.owner == request.user:
            serializer = WorkshopDetailSerializer(
                instance=workshop,
                data=data,
                partial=True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data # can also replace with a personalised message for a successful update
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, workshop_pk):
        workshop = self.get_object(workshop_pk)
        if workshop.owner == request.user:
            workshop.delete()
            # if workshop.is_open:
            #     workshop.current_mentor_num -= 1
            #     workshop.save()
            return Response(
                {"data": {"result":"workshop has been deleted"}},
                status=status.HTTP_200_OK
            )
        return Response(
        {"result":"Unsuccessful - Workshop can only be deleted by the owner."},
        status=status.HTTP_400_BAD_REQUEST,
        )

## attempting to make current_mentor_count work
# class WorkshopSignupsList(APIView):
#     def get(self, request):
#         workshopsSignup = WorkshopSignups.objects.all()
#         serializer = WorkshopSignupsSerializer(workshopsSignup, many=True)
#         return Response(
#             serializer.data,
#         )
       
#     def post(self, request):
#         serializer = WorkshopSignupsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             # if workshop.is_open and workshop.current_mentor_num < workshop.max_mentor_num:
#             #     workshop.current_mentor_num += 1
#             #     workshop.save()
#             return Response(
#                 serializer.data,
#                 status = status.HTTP_201_CREATED,
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST,
#         )


# class WorkshopSignupsDetail(APIView):

#     def get_object(self,workshop_pk):
#         try:
#             workshopsSignup = WorkshopSignups.objects.get(pk=workshop_pk)
#             # self.check_object_permissions(self.request, workshop)
#             return workshopsSignup
#         except Workshop.DoesNotExist:
#             raise Http404

#     def get(self, request, workshop_pk):
#         workshopsSignup = self.get_object(workshop_pk)
#         serializer = WorkshopSignupsDetailSerializer(workshopsSignup)
#         # attempting current_mentor_num
#         # mentor_count = workshop.current_mentor_num.aggregate(count=Count('id'))['count']
#         # data = serializer.data
#         # data['mentor_count'] = mentor_count
#         return Response(serializer.data)

#     def put(self, request, workshop_pk):
#         workshopsSignup = self.get_object(workshop_pk)
#         data = request.data
#         if workshopsSignup.owner == request.user:
#             serializer = WorkshopSignupsDetailSerializer(
#                 instance=workshopsSignup,
#                 data=data,
#                 partial=True
#             )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data # can also replace with a personalised message for a successful update
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     def delete(self, request, workshop_pk):
#         workshopsSignup = self.get_object(workshop_pk)
#         if workshopsSignup.owner == request.user:
#             workshopsSignup.delete()
#             return Response(
#                 {"data": {"result":"workshop has been deleted"}},
#                 status=status.HTTP_200_OK
#             )
#         return Response(
#         {"result":"Unsuccessful - Workshop can only be deleted by the owner."},
#         status=status.HTTP_400_BAD_REQUEST,
#         )