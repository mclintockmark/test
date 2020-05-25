from rest_framework import viewsets, permissions
from .serializer import LeadSerializer
from .models import Lead

class LeadApiViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [permissions.AllowAny]

    serializer_class = LeadSerializer
