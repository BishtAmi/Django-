from rest_framework.response import Response
from rest_framework import generics
from demoapp.models import UserInfo,Financial
from demoapp.serializers import UserSerializer,FinancialSerializer
from rest_framework import status
from rest_framework.generics import UpdateAPIView

class demo(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserInfo.objects.all()

    def get(self, request):
        # Retrieve all instances from the database
        users = self.get_queryset()

        # Serialize all instances
        serializer = self.serializer_class(users, many=True)

        # Return response with serialized data
        return Response({
            "status": "success",
            "total": len(users),
            "users": serializer.data
        })
        
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Save all data received in the request to the database
            serializer.save()

            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        college_id = kwargs.get('college_id')

        try:
            user = self.get_object()  # Retrieve the user object based on the college_id
        except UserInfo.DoesNotExist:
            return Response({"status": "fail", "message": "User with college_id '{}' does not exist.".format(college_id)}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"user": serializer.data}})
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Financial(generics.GenericAPIView):
    serializer_class = FinancialSerializer
    queryset = Financial.objects.all()

    def get(self, request):
        # Retrieve all instances from the database
        users = self.get_queryset()

        # Serialize all instances
        serializer = self.serializer_class(users, many=True)

        # Return response with serialized data
        return Response({
            "status": "success",
            "total": len(users),
            "users": serializer.data
        })
        
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Save all data received in the request to the database
            serializer.save()

            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)