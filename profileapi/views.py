from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
from django.core.validators import validate_email
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
import json


class ProfileDetail(APIView):

    def get(self, request):
        profile = Profile.objects.all().first()
        if profile:
            profile_serializer = ProfileSerializer(profile)
            return HttpResponse(json.dumps(profile_serializer.data), content_type="application/json")
        return HttpResponseNotFound("No profile exist")

    def post(self, request):
        try:
            name = request.data["name"]
            email = request.data["email"]
            dob = request.data["dob"]
            location = request.data["location"]
        except:
            return HttpResponseBadRequest('Required fields missing.')
        try:
            validate_email(email)
        except:
            return HttpResponseBadRequest('Invalid fields.')
        if name == '' or email == '' or dob == '' or location == '':
            return HttpResponseBadRequest('Invalid fields.')
        profile = Profile.objects.all().first()
        if profile:
            try:
                profile.name = name
                profile.email = email
                profile.dob = dob
                profile.location = location
                profile.save()
            except:
                return HttpResponseBadRequest('Invalid fields.')
        else:
            try:
                profile = Profile(name=name, email=email,
                                  dob=dob, location=location)
                profile.save()
            except:
                return HttpResponseBadRequest('Invalid fields.')
        profile_serializer = ProfileSerializer(profile)
        return HttpResponse(json.dumps(profile_serializer.data), content_type="application/json")
