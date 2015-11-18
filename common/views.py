from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, DetailView


class FormView(FormView):
    template_name = 'forms/generic.html'

    @classmethod
    def as_view(cls, form_class=None, **initkwargs):
        if hasattr(form_class, 'success_url'):
            initkwargs['success_url'] = reverse_lazy(form_class.success_url)
        return super().as_view(form_class=form_class, **initkwargs)


    def form_valid(self, form):
        # apparently saving the model doesn't occur by default...
        form.save()
        return super().form_valid(form)


class DetailView(DetailView):
    pass