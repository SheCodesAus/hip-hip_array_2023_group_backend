from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workshop
from .serializers import WorkshopSerializer

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
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class WorkshopDetail(APIView):
    def get_object(self,workshop_pk):
        try:
            return Workshop.objects.get(pk=workshop_pk)
        except Workshop.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, workshop_pk):
        workshop = self.get_object(workshop_pk)
        serializer = WorkshopSerializer(workshop)
        return Response(serializer.data)