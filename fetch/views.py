import requests

from rest_framework.views import APIView 
from rest_framework.response import Response

from fetch.models import Token

from redirect.secret_keys import AX_USERNAME, AX_PASSWORD 

class BaseAxiologueAPIView(APIView):
    axiologue_url = None

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
            data = self.parse_data(response)

            return Response(data)

        else:
            return Response({"Error": "Error fetching product from Axiologue server.  Server returned messange " + response.text + " and status code " + str(response.status_code)})

    # Makes call to server based on url kwarg
    def make_product_call(self, token):
        headers = {'Authorization': 'Token ' + token.key}

        r = requests.get(
            self.get_url(), 
            headers=headers 
        )

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

    # Function for fetching API Url target
    def get_url(self):
        assert self.axiologue_url is not None, (
            "'%s' should either include a `queryList` attribute, "
            "or override the `get_queryList()` method."
            % self.__class__.__name__
        )

        axiologue_url = self.axiologue_url

        return axiologue_url

    # By default returns whole data, but can be overwritten to provide more specific data
    def parse_data(self, resp):
        return resp.json()

# Get Just the score
class GetProductScoreView(BaseAxiologueAPIView):
    def get_url(self):
        return 'https://api.axiologue.org/profile/scores/product/overall-only/' + self.kwargs['pk'] + '/';


# Get Score, Company Name, and Product Name
class GetFullProductInfoView(BaseAxiologueAPIView):
    def get_url(self):
        return 'https://api.axiologue.org/profile/scores/product/fetch/' + self.kwargs['pk'] + '/';

    def parse_data(self, resp):
        raw_data = resp.json()

        data = {
            'product': raw_data['product']['name'],
            'company': raw_data['product']['company'],
            'score': raw_data['score']['overall'] 
        }

        return data 
