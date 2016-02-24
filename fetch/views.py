import requests

from rest_framework.views import APIView 
from rest_framework.response import Response

from fetch.models import Token

from redirect.secret_keys import AX_USERNAME, AX_PASSWORD 

class GetProductScoreView(APIView):
    def get(self,request,*args,**kwargs):

        token = self.get_token()

        response = self.make_product_call(token)

        # If response is unauthorized, delete (likely expired) token and try again
        if response.status_code == 401:
            token.delete()
            token = self.get_token()

            response = self.make_product_call(token)

        # If successful response, return server data
        if response.status_code == 200:
            return Response(response.json())

        else:
            return Response({"Error": "Error fetching product from Axiologue server.  Server returned messange " + response.text + " and status code " + str(response.status_code)})

    # Makes call to server based on url kwarg
    def make_product_call(self, token):
        headers = {'Authorization': 'Token ' + token.key}

        r = requests.get('https://api.axiologue.org/profile/scores/product/overall-only/' + self.kwargs['pk'] + '/', 
                headers=headers )

        return r

    # Fetch Axiologue API Auth token from database
    # If none is there, log in to Axiologue to get token
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
