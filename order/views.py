from django.shortcuts import render, redirect, HttpResponse, Http404

from .models import Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views import generic

# Create your views here.


# def order_form(request, id=0):
#     if request.method == 'GET':
#         if id == 0:
#             form = OrderForm()
#         else:
#             order = Order.objects.get(pk=id)
#             form = OrderForm(instance=order)
#         return render(request, 'order_form.html', {'form': form})
#     else:
#         if id == 0:
#             form = OrderForm(request.POST)
#         else:
#             order = Order.objects.get(pk=id)
#             form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#         return redirect('/order/list/')


# def order_list(request):
#     context = Order.objects.all()
#     return render(request, 'order_list.html', {'orders': context})
#
#
# def del_order(request, id):
#     try:
#         order = Order.get_by_id(id)
#         if order is None:
#             raise Order.DoesNotExist()
#     except Order.DoesNotExist:
#         return Http404(f'User with id: {id} does not exist')
#     order.delete()
#     return redirect('/order/list/')


class OrderCreate(CreateView):
    model = Order
    fields = ['user', 'book', 'end_at', 'plated_end_at']
    success_url = reverse_lazy('orders')


class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__'


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders')


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 3


