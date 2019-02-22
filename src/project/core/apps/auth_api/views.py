from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, get_user_model
from project.core.apps.auth_api.serializers import LoginSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class Login(APIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    @staticmethod
    def post(request):
        try:
            if request.data['username'] and request.data['password']:
                try:
                    user = authenticate(username=request.data['username'], password=request.data['password'])

                    if user:
                        payload = jwt_payload_handler(user)
                        token = jwt_encode_handler(payload)
                        return Response({'token': token}, status=HTTP_200_OK)
                    else:
                        return Response({'type': 'error', 'content': 'Invalid username or password.'},
                                        status=HTTP_400_BAD_REQUEST)
                except get_user_model().DoesNotExist:
                    return Response({'type': 'error', 'content': 'Invalid username or password.'},
                                    status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'type': 'error', 'content': 'Please provide username and password'},
                                status=HTTP_400_BAD_REQUEST)

        except MultiValueDictKeyError:
            return Response({'type': 'error', 'content': 'Please provide username and password'},
                            status=HTTP_400_BAD_REQUEST)
