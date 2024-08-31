# users/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Document
from .forms import DocumentForm
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = []
    
    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        books = Book.objects.filter(title__icontains=search_query)
    
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
@permission_required('users.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'users/document_list.html', {'documents': documents})

@permission_required('users.can_create', raise_exception=True)
def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'users/document_form.html', {'form': form})

@permission_required('users.can_edit', raise_exception=True)
def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'users/document_form.html', {'form': form})

@permission_required('users.can_delete', raise_exception=True)
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'users/document_confirm_delete.html', {'document': document})
