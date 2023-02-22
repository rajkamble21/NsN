from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Work, Artist, Client
from .serializers import WorkSerializer, UserSerializer, ArtistSerializer, ClientSerializer



class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        
class WorkList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['link_type']
    search_fields = ['artist__name']
    ordering_fields = ['id']


class ClientList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
               
        
class ArtistWorksList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['link_type']

    def get(self, request, format=None):
        artist_name = request.query_params.get('artist')
        artist = Artist.objects.filter(name=artist_name).first()
        if not artist:
            return Response({'message': f'Artist with name "{artist_name}" does not exist'}, status=status.HTTP_404_NOT_FOUND)
        works = artist.works.all()
        serializer = self.serializer_class(artist)
        response_data = serializer.data
        return Response(response_data, status.HTTP_200_OK)
    

class WorkTypeList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['link_type']
    ordering_fields = ['id']

    def get(self, request, format=None):
        work_type = request.query_params.get('work_type')
        queryset = Work.objects.filter(link_type=work_type)
        if not queryset.exists():
            Response({'message': 'Work with link_type {} does not exist'.format(work_type)}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)