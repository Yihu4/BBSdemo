"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# 模板
from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext
from django.shortcuts import render



#def index(request):
#    print(request)
#    print(type(request))
    # 本质
    # tpl = loader.get_template('index.html')
    # context = RequestContext(request, {'content': 'www.torch.com'})
    # return HttpResponse(tpl.render(context))
#    d = dict(zip('abced', range(1, 6)))
#    return render(request, 'index.html', {'dct': d})
    # return JsonResponse({'user': 'hello'}) # json str


urlpatterns = [
    path('torch/', include('torch.urls')),
    path('admin/', admin.site.urls),
]
