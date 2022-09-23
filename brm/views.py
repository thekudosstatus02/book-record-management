from django.shortcuts import render
from brm.forms import NewBookForm,SearchBook
from django.http import HttpResponse,HttpResponseRedirect
from brm import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='http://localhost:8000/brm/login')
def viewBooks(request):
    books=models.Book.objects.all()
    res=render(request,'brm/view_books.html',{'books':books})
    return res

def userLogin(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('http://localhost:8000/brm/view-books')
        else:
            data['error']="Either username or password is incorrect"
            res=render(request,'brm/login.html',data)
            return res
    else:
        res=render(request,'brm/login.html',data)
        return res

    res=render(request,'brm/login.html')
    return res

@login_required(login_url='http://localhost:8000/brm/login')
def userLogout(request):
    logout(request)
    del request.session['username']
    return HttpResponseRedirect('http://localhost:8000/brm/login')

@login_required(login_url='http://localhost:8000/brm/login')
def searchBook(request):
    form=SearchBook()
    res=render(request,'brm/search.html',{'form':form})
    return res

@login_required(login_url='http://localhost:8000/brm/login')
def search(request):
    if request.method=='POST':
        form=SearchBook(request.POST)
        title=form.data['title']
        books=models.Book.objects.filter(title=title)
        res=render(request,'brm/search.html',{'form':form,'books':books})
        return res

@login_required(login_url='http://localhost:8000/brm/login')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['book_id'])
    print(book)
    fields={'title':book.title,'author':book.author,'price':book.price,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'brm/edit_book.html',{'form':form,'book':book})
    return res

@login_required(login_url='http://localhost:8000/brm/login')
def edit(request):
    if request.method=='POST':
        book=models.Book.objects.get(id=request.GET['book_id'])
        form=NewBookForm(request.POST)
        book.id=request.GET['book_id']
        book.title=form.data['title']
        book.author=form.data['author']
        book.price=form.data['price']
        book.publisherlogin_=form.data['publisher']
        book.save()
        return HttpResponseRedirect('http://localhost:8000/brm/view-books')

@login_required(login_url='http://localhost:8000/brm/login')
def deleteBook(request):
    book_id=request.GET['book_id']
    book=models.Book.objects.filter(id=book_id)
    book.delete()
    return HttpResponseRedirect('http://localhost:8000/brm/view-books')

@login_required(login_url='http://localhost:8000/brm/login')
def newBook(request):
    form=NewBookForm()
    res=render(request,'brm/new_book.html',{'form':form})
    return res

@login_required(login_url='http://localhost:8000/brm/login')
def addBook(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.author=form.data['author']
        book.price=form.data['price']
        book.publisher=form.data['publisher']
        book.save()
        msg="Record saved in Database"
    else:
        msg="Record cannot be saved in Database"
    msg=msg+'<br><a href="http://localhost:8000/brm/view-books">View Books</a>'
    return HttpResponse(msg)
