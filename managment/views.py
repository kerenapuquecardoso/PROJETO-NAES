from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from managment.models import Admin, Category, Client, Clothing, ClothingImages
class IndexView(TemplateView):
    template_name = "managment/index.html"
    base_template = "managment/model.html"

class AboutView(TemplateView):
    template_name = "managment/about.html"


class PhotosList(ListView):
    template_name = "managment/list/photos/photos.html"
    model = ClothingImages

class ClothingList(LoginRequiredMixin, ListView):
    template_name = "managment/list/clothing_list.html"
    model = Clothing
    context_object_name = 'clothing_list'
    paginate_by = 10
    extra_context = {
        "titulo": "Lista de Roupas",
        "subTitulo": "Gerencie todas as roupas cadastradas no catálogo",
    }

#Create
class AdminCreate(CreateView):
    model = Admin
    fields = ['usuario', 'name']
    template_name = 'managment/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        "titulo" : "Cadastre-se",
        "subTitulo" : "Seja um admin e obtenha acesso para cadastrar roupas para o catálogo!",
    }        

class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['usuario', 'name', 'phone']
    template_name = 'managment/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        "titulo" : "Cadastre-se",
        "subTitulo" : "Seja um cliente para obter acesso exclusivo a promoções!",
    }

ClothingImagesFormSet = inlineformset_factory(
    Clothing, ClothingImages,
    fields=['image_url'],
    extra=1,
    can_delete=True
)

class ClothingCreate(LoginRequiredMixin, CreateView):
    model = Clothing
    fields = ['name', 'description', 'size', 'color', 'value', 'category', 'admin']
    template_name = 'managment/form2.html'
    success_url = reverse_lazy('index')
    extra_context = {
        "titulo" : "Cadastar Roupa",
        "subTitulo" : "Preencha todos os campos para cadastrar uma nova roupa",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['images_formset'] = ClothingImagesFormSet(self.request.POST)
        else:
            context['images_formset'] = ClothingImagesFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        images_formset = context['images_formset']
        self.object = form.save()
        if images_formset.is_valid():
            images_formset.instance = self.object
            images_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class CategoryCreate(LoginRequiredMixin,CreateView):
    model = Category
    fields = ['name']
    template_name = 'managment/form.html'
    success_url = reverse_lazy('about')
    extra_context = {
        "titulo" : "Cadastrar categoria",
        "subTitulo" : "",
    }

#Update
class AdminUpdate(LoginRequiredMixin, UpdateView):
    template_name = "managment/form.html"
    model = Admin
    success_url = reverse_lazy("index")
    fields = ['usuario', 'name']
    extra_context = {
        "titulo" : "Atualizar dados do Admin",
        "subTitulo" : "faça isso quando seus dados estiverem desatualizados",
        
    }

class ClientUpdate(LoginRequiredMixin, UpdateView):
    template_name = "managment/form.html"
    model = Client
    success_url = reverse_lazy("index")
    fields = ['usuario', 'name', 'phone']
    extra_context = {
        "titulo" : "Atualizar dados Cliente",
        "subTitulo" : "faça isso quando seus dados estiverem desatualizados",
        
    }

class ClothingUpdate(LoginRequiredMixin, UpdateView):
    model = Clothing
    fields = ['name', 'description', 'size', 'color', 'value', 'category', 'admin']
    template_name = 'managment/formUpdateClothing.html'
    success_url = reverse_lazy('photos')
    extra_context = {
        "titulo" : "Atualizar dados Roupa",
        "subTitulo" : "as roupas podem ser atualizadas quando houver mudança de preço, tamanho ou cor",
        
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['images_formset'] = ClothingImagesFormSet(self.request.POST, instance=self.object)
        else:
            context['images_formset'] = ClothingImagesFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        images_formset = context['images_formset']
        self.object = form.save()
        if images_formset.is_valid():
            images_formset.instance = self.object
            images_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    template_name = "managment/form.html"
    model = Category
    fields = ['name']
    success_url = reverse_lazy("photos")
    extra_context = {
        "titulo" : "Atualizar a Categoria",
        "subTitulo" : "pode ser atualizado quando houver mudança de nome",
        
    }

#Delete
class AdminDelete(LoginRequiredMixin, DeleteView):
    template_name = "managment/form-excluir.html"
    model = Admin
    success_url = reverse_lazy("photos")
    extra_context = {
        "titulo" : "Deletar Admin",
        "subTitulo" : "Tem certeza que deseja deletar o admin?",
        
    }

class ClientDelete(LoginRequiredMixin, DeleteView):
    template_name = "managment/form-excluir.html"
    model = Client
    success_url = reverse_lazy("photos")
    extra_context = {
        "titulo" : "Deletar Cliente",
        "subTitulo" : "Tem certeza que deseja deletar um cliente?",
        
    }

class ClothingDelete(LoginRequiredMixin, DeleteView):
    template_name = "managment/form-excluir.html"
    model = Clothing
    success_url = reverse_lazy("photos")
    extra_context = {
        "titulo": "Deletar Roupa",
        "subTitulo": "Tem certeza que deseja deletar esta roupa e todas as imagens associadas?",
    }

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.images.all().delete()
        return super().delete(request, *args, **kwargs)

class CategoryDelete(LoginRequiredMixin, DeleteView):
    template_name = "managment/form-excluir.html"
    model = Category
    success_url = reverse_lazy("photos")
    extra_context = {
        "titulo" : "Deletar Categoria",
        "subTitulo" : "Tem certeza que deseja deletar esta categoria?",
    }

