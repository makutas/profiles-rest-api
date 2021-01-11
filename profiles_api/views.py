from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEST API VIEW"""
    '''This creates a new class based on APIView class and it allows us to define an application
    logic for out endpoint. You define a URL which is the endpoint and assign it to this view then 
    django REST framework handles it by calling the appropriate functions in a view for 
    http request you make'''

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post. put, patch, delete)',
            'Is similar to a traditional Django view',
            'Give you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        # Every HTTP function must return a response object - dictionary or a list!!!
        # It converts response object to JSON
