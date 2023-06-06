from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
import json
from .serializers import AccountSerializer

# Create your views here.


@api_view(["GET"])
def index(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    accounts_data = serializer.data
    json_data = json.dumps(accounts_data)
    return HttpResponse(json_data, content_type="application/json")


@api_view(["GET"])
def detail(request, account_id):
    account = Account.objects.get(pk=account_id)
    serializer = AccountSerializer(account)
    json_data = json.dumps(serializer.data)
    return HttpResponse(json_data, content_type="application/json")
