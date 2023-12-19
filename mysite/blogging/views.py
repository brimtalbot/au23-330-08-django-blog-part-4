from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class CustomListView:
    model = None
    template_name = None

    def as_view(self):
        return self.get

    def get(self, request):
        model_list_name = self.model.__name__.lower() + '_list'
        context = {model_list_name: self.model.objects.all()}


class BlogListView(ListView):
    model = Post
    template_name = 'list.html'

    def get_queryset(self):
        queryset = Post.objects.\
            exclude(published_date=None).\
            order_by('-published_date')
        return queryset


    # def post(self, request, *args, **kwargs):
    #     posts = self.get_object()
    #     queryset = Post.objects.filter(published_date=None)
    #     context_object_name = 'post_list'
    #     template_name = 'list.html'
    #     context = {'posts': posts}
        # post = self.get_object()
        #
        # published = Post.objects.exclude(published_date=None)
        # posts = published.order_by('-published_date')
        # context = {'posts': posts}
        # return render(request, 'list.html', context)


class BlogDetailView(DetailView):

    model = Post
    template_name = 'detail.html'

    def post_detail_view(self, request, ):
        try:
            post = self.get_object()
            published = Post.objects.exclude(published_date=None)
        except Post.DoesNotExist:
            print(f'Everybody PANIC (reason: post DNE)')
            raise Http404
        context = {'post': post}
        return render(request, 'detail.html', context)
