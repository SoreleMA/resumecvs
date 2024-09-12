from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Curriculum, Education, Experience
from .serializers import CurriculumSerializer, EducationSerializer, ExperienceSerializer
from rest_framework.permissions import IsAuthenticated
from api.users.permissions import IsAdminUser, IsClientUser, IsCompanyUser

class AdminCurriculumListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        # Filtrar los currículums para mostrar solo los de los clientes
        curriculums = Curriculum.objects.filter(owner__role='client')
        serializer = CurriculumSerializer(curriculums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Eliminación permitida pero no se permite creación ni actualización
    def delete(self, request, id):
        try:
            curriculum = Curriculum.objects.get(id=id)
        except Curriculum.DoesNotExist:
            return Response({'error': 'Curriculum not found'}, status=status.HTTP_404_NOT_FOUND)

        curriculum.delete()
        return Response({'message': 'Curriculum deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class AdminCurriculumDetailView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, id):
        try:
            curriculum = Curriculum.objects.get(id=id)
        except Curriculum.DoesNotExist:
            return Response({'error': 'Curriculum not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CurriculumSerializer(curriculum)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        try:
            curriculum = Curriculum.objects.get(id=id)
        except Curriculum.DoesNotExist:
            return Response({'error': 'Curriculum not found'}, status=status.HTTP_404_NOT_FOUND)

        curriculum.delete()
        return Response({'message': 'Curriculum deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class ClientCurriculumListView(APIView):
    permission_classes = [IsAuthenticated, IsClientUser]

    def get(self, request):
        curriculums = Curriculum.objects.filter(owner=request.user)
        serializer = CurriculumSerializer(curriculums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CurriculumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Asigna el usuario actual como el propietario
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientCurriculumDetailView(APIView):
    permission_classes = [IsAuthenticated, IsClientUser]

    def get(self, request, id):
        try:
            curriculum = Curriculum.objects.get(id=id, owner=request.user)
        except Curriculum.DoesNotExist:
            return Response({'error': 'Curriculum not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CurriculumSerializer(curriculum)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        try:
            curriculum = Curriculum.objects.get(id=id, owner=request.user)
        except Curriculum.DoesNotExist:
            return Response({'error': 'Curriculum not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CurriculumSerializer(curriculum, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            curriculum = Curriculum.objects.get(id=id, owner=request.user)
        except Curriculum.DoesNotExist:
            return Response({'error': 'Curriculum not found'}, status=status.HTTP_404_NOT_FOUND)

        curriculum.delete()
        return Response({'message': 'Curriculum deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class CompanyCurriculumListView(APIView):
    permission_classes = [IsCompanyUser]

    def get(self, request):
        curriculums = Curriculum.objects.all()  # Las compañías pueden ver todos los CVs
        serializer = CurriculumSerializer(curriculums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class EducationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ExperienceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer