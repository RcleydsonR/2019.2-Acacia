import os
from django.urls import path
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


def list_all_endpoints(urlpatterns, app_name=None):

    class ListAllEndpoints(APIView):
        permission_classes = (AllowAny,)

        def get(self, request, format=None):
            link = os.environ.get('HOST')
            endpoints = {}

            for url in urlpatterns:
                url = url.pattern._route[:-1]

                if url:

                    if app_name:
                        endpoints[url] = f"{link}{app_name}/{url}/"

                    else:
                        endpoints[url] = f"{link}{url}/"

            return Response(endpoints, status=status.HTTP_200_OK)

    urlpatterns += [
        path('', ListAllEndpoints.as_view()),
    ]

    return urlpatterns
