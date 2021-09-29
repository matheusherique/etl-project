from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .transform import Transform
from .extract import Extract
import logging
import time
import json

LOGGER = logging.getLogger(__name__)


class LoadView(APIView):
    def get(self, request):
        start_time = time.time()
        numbers_list = Extract(times=10001).get_number_list()
        sorted_numbers_list = Transform().sort_numbers_list(numbers_list)
        LOGGER.info(f'--- {time.time() - start_time} seconds ---')

        return Response(json.dumps(
            {"sorted_numbers": sorted_numbers_list}),
            status=status.HTTP_200_OK)

    @classmethod
    def get_extra_actions(cls):
        return []
