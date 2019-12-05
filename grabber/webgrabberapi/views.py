from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .resources.myrequest import CtxRequest
import requests


class UrlGrabberView(APIView):
    def get(self, request):
        url = self.request.query_params.get('url', None)
        print("Parsing Started!")
        myRequest = CtxRequest(url)
        result = myRequest.getEmails()
        # req = requests.get(url)
        # queryset = Ulset.objects.all().update(statusi=False)
        return Response({"Emails": result["emails"], "Page_status": result["status"], "url_validity": result["urlValidity"]})
