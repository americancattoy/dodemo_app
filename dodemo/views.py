from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from.models import DodemoModel
# from django.core.paginator import Paginator
# from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


@login_required
def indexfunc(request):
    object_index = DodemoModel.objects.all()
    return render(request, 'dodemo/index.html', {'object_index':object_index})

def detailfunc(request, pk):
    object = DodemoModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})
    
def goodfunc(request, pk):
    post = DodemoModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('index')


class DodemoCreate(CreateView):
    template_name = 'dodemo/create.html'
    model = DodemoModel
    fields = ('content', 'author', 'image')
    success_url = reverse_lazy('index')

