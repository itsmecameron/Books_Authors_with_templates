from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):

    context = {
        'Books': Books.objects.all()
    }

    return render(request,"books_authors_app/index.html",context)
#---------------------------------------------------------
#form to post a new book
#---------------------------------------------------------
def add_book(request):
    if request.method == "POST":

        Books.objects.create(title=request.POST["title"], description=request.POST["description"])

        return redirect("/")
#---------------------------------------------------------
#page to show a selected book by id
#---------------------------------------------------------
def show_book(request, val):
    context = {
        'book' : Books.objects.get(id=val),
        'authors': Authors.objects.all()
    }
    return render(request,"books_authors_app/show_book.html",context)
#---------------------------------------------------------
#form to add an author(s) to a specific book(id)
#---------------------------------------------------------
def add_author(request):
    if request.method == "POST":
        id = request.POST["book_id"]
    author_id = request.POST["authors"]
    book = Books.objects.get(id=id)
    author = Authors.objects.get(id=author_id)

    book.publishers.add(author)
        

    return redirect("books/" + id)
#---------------------------------------------------------
#form to show all authors
#---------------------------------------------------------

def author(request):

    context = {
        'Author': Authors.objects.all()
    }

    return render(request,"books_authors_app/authors.html", context)
#---------------------------------------------------------
#form to post a new author
#---------------------------------------------------------
def add_author(request):
    if request.method == "POST":

        Authors.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], notes = request.POST["notes"])

        return redirect("/authors")
#---------------------------------------------------------
#page to show a selected author by id
#---------------------------------------------------------

def show_author(request, val):
    context = {
        'author' : Authors.objects.get(id=val),
        'books': Books.objects.all()
    }
    return render(request,"books_authors_app/show_authors.html",context)
#---------------------------------------------------------
#form to add an book(s) to a specific author(id)
#---------------------------------------------------------
def add_book(request):
    if request.method == "POST":
        id = request.POST["author_id"]
    book_id = request.POST["books"]

    book = Books.objects.get(id = book_id)
    author = Authors.objects.get(id=id)

    author.books.add(book)
        

    return redirect("authors/" + id)

