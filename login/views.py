from django.shortcuts import render,redirect
from register.forms import AuthorForm
from recipes.models import Author

def login_page(request):
    form = AuthorForm()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['author_name']
            password = form.cleaned_data['author_password']

            try:
                author = Author.objects.get(author_name=name, author_password=password)
                # Login bem-sucedido — renderiza página recipes.html passando o autor
                return redirect('recipes')
            except Author.DoesNotExist:
                form.add_error(None, 'Nome ou senha inválidos.')

    return render(request, 'login_page.html', {'form': form})
