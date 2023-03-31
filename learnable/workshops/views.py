from rest_framework import status, permissions
from django.http import Http404, JsonResponse
from users import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workshop
from .serializers import WorkshopSerializer, WorkshopDetailSerializer

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
            return Response(
                {"data": {"result":"workshop has been deleted"}},
                status=status.HTTP_200_OK
            )
        return Response(
        {"result":"Unsuccessful - Workshop can only be deleted by the owner."},
        status=status.HTTP_400_BAD_REQUEST,
        )
