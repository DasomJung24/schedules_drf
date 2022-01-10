from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSignUpSerializer, UserLoginSerializer


class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
