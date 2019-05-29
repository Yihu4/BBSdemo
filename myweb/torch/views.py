from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseBadRequest, Http404
from django.shortcuts import get_object_or_404, render, redirect
import json
import logging
import simplejson
from .models import User
from .models import Wordclass, Word
from django.db.models.query import QuerySet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

FORMAT = "%(asctime)s%(threadName)s%(thread)d%(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def welcome(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def checkemail(request):
    # 判断email
    return HttpResponse()


def reg(request: HttpRequest):
    # print(json.loads(request.body))
    payload = simplejson.loads(request.body)
    try:
        try:
            qs = User.objects.filter(pk=1).get()
            print(qs)
        except Exception as e:
            print(e, '~~~')
        finally:
            print('-' * 30)

        email = payload['email']
        qs = User.objects.filter(email=email)  # queryset
        print(qs)  # 列表[]
        print(type(qs))  # 查询集
        print(qs.query, "~~~~~~~~~~~")
        if qs:  # 该email已经存在了
            return HttpResponseBadRequest()
        else:
            print('-' * 30)

        name = payload['name']
        password = payload['password']
        print(email, name, password)

        user = User()
        user.email = email
        user.name = name
        user.password = password
        try:
            user.save()
            return JsonResponse({'user_id': user.id})  # 200
        except Exception as e:
            logging.info(e)
            return HttpResponseBadRequest()  # 最好和下面处理方式不一样,如果一样的话不如删掉
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()


def index(request):
    print(request)
    print(type(request))
    # 本质
    # tpl = loader.get_template('index.html')
    # context = RequestContext(request, {'content': 'www.torch.com'})
    # return HttpResponse(tpl.render(context))
    d = dict(zip('abced', range(1, 6)))
    return render(request, 'index.html', {'dct': d})
    # return JsonResponse({'user': 'hello'}) # json str


def add_word(request):
    if request.method == 'POST':
        new_word = request.POST.get('name')
        wordclass1_id = request.POST.get('wordclass1_id')
        wordclass2_id = request.POST.get('wordclass2_id')
        wordclass3_id = request.POST.get('wordclass3_id')
        wordclass4_id = request.POST.get('wordclass4_id')
        new_chinese1 = request.POST.get('chinese1')
        new_chinese2 = request.POST.get('chinese2')
        new_chinese3 = request.POST.get('chinese3')
        new_chinese4 = request.POST.get('chinese4')
        new_example = request.POST.get('example')
        Word.objects.create(name=new_word, chinese1=new_chinese1, chinese2=new_chinese2, chinese3=new_chinese3,
                            chinese4=new_chinese4, wordclass1_id=wordclass1_id, wordclass2_id=wordclass2_id,
                            wordclass3_id=wordclass3_id, wordclass4_id=wordclass4_id, example=new_example)
        return redirect('/torch/word_list/')

    res = Wordclass.objects.all()
    return render(request, 'add_word.html',
                  {'wordclass1_list': res, 'wordclass2_list': res, 'wordclass3_list': res, 'wordclass4_list': res})


# 删除单词
def drop_word(request):
    drop_id = request.GET.get('id')
    drop_obj = Word.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/torch/word_list/')


# 书籍的列表
def word_list(request):
    current_page = request.GET.get('page', 1)  # 获取页码参数
    words = Word.objects.all()
    pages = Paginator(words, 3)  # 每3个分页
    words = pages.page(current_page)  # 获取当前页的数据

    context = {}
    context['words'] = words
    context['pages'] = pages
    return render(request, 'word_list.html', context)


# 出版社列表
#def wordclass_list(request):
#    wordclass = Wordclass.objects.all()
#    return render(request, 'wordclass_list.html', {'': wordclass})
