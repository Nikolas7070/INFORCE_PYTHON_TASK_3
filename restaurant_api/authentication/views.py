from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from restaurant_api.authentication.serializers import UserSerializer, UserProfileSerializer


class TokenObtainPairView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        profile_serializer = UserProfileSerializer(data={'user': user.id})
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
