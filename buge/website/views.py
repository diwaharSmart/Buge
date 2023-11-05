from django.shortcuts import render
from website.models import Page
from rest_framework.views import APIView
from rest_framework.response import Response
from website.models import Api

# Create your views here.
def get_page(key):
    return Page.objects.get(key=key)


def PageView(request,key):

    data         = dict()
    print(key)
    try:
        if key == "favicon.ico":
            data["page"] = get_page("index")

        else:
            data["page"] = get_page(key)

    except:
        data["page"] = Page.objects.create(
            key="index",
            title="Home"
        )
    return render(
        request,
        template_name="website/page.html",
        context=data
    )

class ApiRequest(APIView):
    def get(self,request,format=None):
        response = dict()
        api_key = self.request.query_params.get("api_key",None)
        api = Api.objects.get(key=api_key)
        exec(api.content)
        return Response(response)


