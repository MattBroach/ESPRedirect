import requests

from rest_framework.views import APIView 
from rest_framework.response import Response

from fetch.models import Token

from redirect.secret_keys import AX_USERNAME, AX_PASSWORD 

class GetProductView(APIView):
    def get(self,request,*args,**kwargs):

        token = self.get_token()

        return Response({'token': token.key})

    def get_token(self):
        try:
            token = Token.objects.all()[0]
        except IndexError:
            r = requests.post("https://api.axiologue.org/rest-auth/login/", data={
                    'username': AX_USERNAME,
                    'password': AX_PASSWORD
                })
            data = r.json()

            token = Token(key=data['key'])
            token.save()

        return token
