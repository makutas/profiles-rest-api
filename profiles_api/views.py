from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    """TEST API VIEW"""
    serializer_class = serializers.HelloSerializer
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

        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview
        })
        # Every HTTP function must return a response object - dictionary or a list!!!
        # It converts response object to JSON

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        # Since serializer can validate data, we can in this case check if name is no
        # more then 10 characters in length by using isvalid class.
        if serializer.is_valid():
            name = serializer.validated_data.get('name') # we get our name if it is valid in length
            message = f'Hello {name}'
            return Response({'message': message})
        # if input is however not valid we return 400
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        # Used to update and object. It will update an entire object based on put request
        # However this is different from HTTP PATCH
        '''The http PUT is usually do it to a specific URL primary key 
        (object with an ID to update for example .../object.id=1)'''
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        # This is used to update the fields provided in a request
        '''For example to update last name but not the first name. If you would use PUT
        to update a last name, it would remove the first name because it is basically replacing
        and object with the new object provided'''
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial update, destroy)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Removing an object"""
        return Response({'http_method': 'DELETE'})