from rest_framework import generics, viewsets

from src.audio_library import models, serializers
from src.base.permissions import IsAuthor


class GenreListView(generics.ListAPIView):
    """Список жанров"""
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class LicenseView(viewsets.ModelViewSet):
    """CRUD лицензий автора"""
    serializer_class = serializers.LicenseSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return models.License.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
