from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .transform import Transform
from .extract import Extract
import json


class LoadView(APIView):
    def get(self, request):
        numbers_list = Extract(times=10001).get_number_list()
        sorted_numbers_list = Transform().sort_numbers_list(numbers_list)

        return Response(json.dumps(
            {"sorted_numbers": sorted_numbers_list}),
            status=status.HTTP_200_OK)

    @classmethod
    def get_extra_actions(cls):
        return []
