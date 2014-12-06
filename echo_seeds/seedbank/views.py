
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from django.core.urlresolvers import reverse

from seedbank.models import Seed
from seedbank import forms


class ListSeedView(ListView):
    model = Seed
    template_name = 'seed_list.html'


class CreateSeedView(CreateView):
    model = Seed
    template_name = 'edit_seed.html'
    form_class = forms.SeedForm

    def get_success_url(self):
        return reverse('seeds-list')

    def get_context_data(self, **kwargs):
        context = super(CreateSeedView, self).get_context_data(**kwargs)
        context['action'] = reverse('seeds-new')

        return context


class UpdateSeedView(UpdateView):
    model = Seed
    template_name = 'edit_seed.html'
    form_class = forms.SeedForm

    def get_success_url(self):
        return reverse('seeds-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateSeedView, self).get_context_data(**kwargs)
        context['action'] = reverse('seeds-edit',
                                    kwargs={'pk': self.get_object().id})

        return context


class DeleteSeedView(DeleteView):
    model = Seed
    template_name = 'delete_seed.html'

    def get_success_url(self):
        return reverse('seeds-list')


class SeedView(DetailView):
    model = Seed
    template_name = 'seed.html'


# class EditSeedLocationView(UpdateView):
#     model = Seed
#     template_name = 'edit_location.html'
#     form_class = forms.SeedLocationFormSet

#     def get_success_url(self):
#         # redirect to the Seed view
#         return self.get_object().get_absolute_url()
