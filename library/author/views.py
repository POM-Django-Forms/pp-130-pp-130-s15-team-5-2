from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Author
from book.models import Book
from .forms import AuthorForm


@login_required
def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors/all_authors.html', {'authors': authors})


@login_required
def create_author(request):
    form = AuthorForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('all_authors')
    
    return render(request, 'authors/create_author.html', {'form': form})

@login_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if not Book.objects.filter(authors=author).exists():
        author.delete()
    return redirect('all_authors')

