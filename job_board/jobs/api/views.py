from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from jobs.api.serializers import JobOfferSerializer
from jobs.models import JobOffer


class JobListCreateAPIView(APIView):

    def get(self, request):
        joboffers = JobOffer.objects.all()
        serializer = JobOfferSerializer(joboffers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailAPIView(APIView):
    
    def get_object(self, pk):
        joboffer = get_object_or_404(JobOffer, pk=pk)
        return joboffer

    def get(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(joboffer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(data=request.data, instance=joboffer, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(data=request.data, instance=joboffer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        joboffer = self.get_object(pk)
        joboffer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

