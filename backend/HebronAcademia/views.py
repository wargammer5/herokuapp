from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HebronOneHundredSerializer
from .models import FormDonaite


class HebronAcademyView(APIView):
    def get(self, request, **args,**kwargs):
        data = [{'id': '1', 'name':'John'},{'id': '2', 'name':'Jane'}]
        return Response(data)