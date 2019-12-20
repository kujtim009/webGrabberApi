from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .resources.myrequest import CtxRequest
from .resources.linkedinCompany import companyLinkedin
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


class linkedinCompanyGrabber(APIView):
    def get(self, request):
        cpNames = self.request.data["names"]
        linkedin = companyLinkedin(cpNames)
        linkedin.getCompanyData()
        print("Request data: ", cpNames)
        return Response(linkedin.getJson())

