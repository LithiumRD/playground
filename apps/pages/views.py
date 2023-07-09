
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm

# Create your views here.


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class PageListView(ListView):
    model = Page
    template_name = 'pages/pages.html'


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page.html'


@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    template_name = 'pages/create.html'
    success_url = reverse_lazy('pages:page_list')


class PageUpdateView(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    template_name = 'pages/update.html'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDeleteView(StaffRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/delete_confirm.html'
    success_url = reverse_lazy('pages:page_list')
