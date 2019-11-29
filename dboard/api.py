from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class LawyerAuth(APIView):
    def post(self, request):
        pass
    

class LawyerList(APIView):

    def get(self, request):

        model = Lawyers.objects.all()
        serializer = LawyersSerializers(model, many= True)
        return Response(serializer.data)

    def post(self, request):
        # model = Lawyers.objects.all()
        serializer = LawyersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class LawyerDetail(APIView):
    def get_lawyer(self, lawyer_id):
        try:
            model = Lawyers.objects.get( id = lawyer_id)
            return model
        except Lawyers.DoesNotExist:
            return 

    def get(self, request, lawyer_id):
        if not self.get_lawyer(lawyer_id):
            return Response(f"User with ID number {lawyer_id} does not exist in DataBase", status= status.HTTP_404_NOT_FOUND)
        serializer = LawyersSerializers(self.get_lawyer(lawyer_id))
        return Response(serializer.data)

    def put(self, request, lawyer_id):
        serializer = LawyersSerializers(self.get_lawyer(lawyer_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, lawyer_id):
        model = self.get_lawyer(lawyer_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)