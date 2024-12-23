from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . forms import CarForms, CarModelForm
from . models import Car, Brand
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

def car(request):
    cars = Car.objects.all()
    return render(request, 'car/list-car.html', {'cars': cars})

class CarView(View):
    
    def get(self, request):
        cars = Car.objects.all()
        return render(request, 'car/list-car.html', {'cars': cars})


class CarListView(ListView):
    template_name  = 'car/list-car.html'
    model = Car
    context_object_name = 'cars'
    
    def get_queryset(self):
        return super().get_queryset().order_by('-value')
    
 
def new_car(request):
    if request.method == "POST":
        # form = CarForms(request.POST, request.FILES)
        form = CarForms(request.POST, request.FILES)
        print(form.data)      
        if form.is_valid():
            form.save()
            return redirect('list-cars')
        
        else:
            print(form.errors)
    
    else:
        form = CarForms()
    
    return render(request, 'car/new-car.html', {'form': form})


class NewCarView(View):
    def get(self, request):
        form = CarForms()
        return render(request, 'car/new-car.html', {'form': form})
    
    def post(self, request):
        form = CarForms(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            
        return render(request, 'car/new-car.html', {'form': form})
            
@method_decorator(login_required(login_url='login'), name="dispatch")
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car/new-car.html'
    success_url = "/"

   
class CarDetailView(DetailView):
    model = Car
    template_name = "car/car-detail.html"


@method_decorator(login_required(login_url='login'), name="dispatch") 
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = "car/car-update.html"
    
    def get_success_url(self):
        return reverse_lazy('car-detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    template_name = "car/car-delete.html"
    success_url = '/'