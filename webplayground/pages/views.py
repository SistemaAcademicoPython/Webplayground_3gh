from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from pages.Forms import PageForms
from django.shortcuts import redirect
from .models import Page

# Create your views here.
#def pages(request):
#    pages = get_list_or_404(Page)
#    return render(request, 'pages/pages.html', {'pages': pages})

class StaffRequiredMixin(object):
    """
    este mixin sirve para validar si el usuario que realiza petición
    es parte del staff
    """
    def dispatch(self, request, *args, **kwargs):
        #print(request.user)
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))
        return super(PageCreate, self).dispatch(request, *args, **kwargs)

class PageListView(ListView):
    model = Page

#def page(request, page_id, page_slug):
#    page = get_object_or_404(Page, id=page_id)
#    return render(request, 'pages/page.html', {'page':page})

class PageDetailView(DetailView):
    model = Page

class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForms
    success_url = reverse_lazy('pages')



class PageUpdate(UpdateView):
    model = Page
    #fields = ['title', 'content', 'order']
    form_class = PageForms
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id]) +'?ok'

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages')

