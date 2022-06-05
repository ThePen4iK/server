from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from subprocess import Popen
import sys

@api_view(['GET'])
@permission_classes([AllowAny])
def voice_command(request):
    help = True
    try:
        Popen([sys.executable, 'D:\\University\\blank_django-master\\bot\\bot.py'])
        return Response(help)
    except:
        help = False
        return Response(help)