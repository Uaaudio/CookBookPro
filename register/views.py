
from django.shortcuts import render, redirect
from .forms import AuthorForm  # <--- Importe o form

# Create your views here.


def register_page(request):

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect para a pagina de login após o sucesso no rgistro.
    else:
        form = AuthorForm()

    return render(request, "register_page.html", {'form': form})
