from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from Accounting.forms import TagForm
from Accounting.models import Tag


@method_decorator(login_required(), name="dispatch")
class TagListView(ListView):
    model = Tag
    template_name = "Accounting/dashboard/sections/tags.html"

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


@method_decorator(login_required(), name="dispatch")
class TagNewView(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'Accounting/dashboard/sections/tag_new.html', {'form': form})

    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            tag = Tag(name=form.cleaned_data['name'], user=self.request.user)
            tag.save()
            return HttpResponseRedirect('/dashboard/tags')
        else:
            return render(request, 'Accounting/dashboard/sections/tag_new.html', {'form': form})


@method_decorator(login_required(), name="dispatch")
class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    template_name = 'Accounting/dashboard/sections/tag_update.html'
    success_url = '/dashboard/tags'