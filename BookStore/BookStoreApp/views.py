from ast import Break, Return
from operator import le
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse

from BookStoreApp.models import LoginPage,BookInfoo
# Create your views here.

store = ''
searchedvalue = ''
def loginpage(request):
    if request.method == 'POST': 
        if (request.POST['username'] == '' or request.POST['password'] == '') or (request.POST['username'] == '' and request.POST['password'] == ''):
            loginerror = {'loginerror': 'Please enter all fields'}
            return render(request,"loginpage.html",loginerror)
        else:
            username = request.POST['username']
            global store
            store = username
            password = request.POST['password']
            try:
                user = LoginPage.objects.get(username=username,password=password)
                if user is not None:
                    return redirect('/mainpage')
            except:
                loginfailed = {'loginerror': 'Given username or password is invalid, please register if not registered'}
                return render(request,"loginpage.html",loginfailed)
    return render(request,"loginpage.html")

def registerpage(request):
    if request.method == 'POST':
        if (request.POST['username'] == '' and request.POST['password'] == '') or (request.POST['username'] == '' or request.POST['password'] == ''):
            registererror = {'registererror': 'Please enter all fields'}
            return render(request,"registerpage.html",registererror)
            #return render(request,"registererror.html")
        else:
            username = request.POST['username']
            password = request.POST['password']
            logindetails = LoginPage.objects.all()
            loginlist = []
            for i in logindetails:
                loginlist.append(i.username)
            k = len(loginlist)
            for i in range(k):
                if username == loginlist[i]:
                    already_added = {'already_added': 'Given username is already esixt, try new one'}
                    return render(request,"registerpage.html",already_added)
            else:
                k = LoginPage(username=username,password=password)
                k.save()
                success = {'success': 'Successfully registered'}
                return render(request,"registerpage.html",success)
    return render(request,"registerpage.html")

def mainpage(request):
    stored = {'store':store}
    errormsg = {'error':'Looks like you have not selected any alphabet'}
    if 'alph' in request.POST:
        clicked = request.POST.get('alph')
        print(clicked)
        if clicked == 'a':
            return redirect('/a')
        elif clicked == 'b':
            return redirect('/b')
        elif clicked == 'c':
            return redirect('/c')
        else:
             return render(request,"home.html",errormsg)
    elif 'search-btn' in request.POST:
        searchbtn = request.POST.get('search')
        global searchedvalue
        searchedvalue = searchbtn
        print(searchedvalue)
        bookdetails = BookInfoo.objects.all()
        booklist = []
        for i in bookdetails:
            booklist.append(i.bookname)
            k = len(booklist)
            for i in range(k):
                if searchbtn == booklist[i]:
                    return redirect('/search')
        else:
            bookname = {'bookname' : searchbtn,'msg':'No book found with','store':store}
            return render(request, "home.html",bookname)
        
    return render(request,"home.html",stored)

def a(request):
    a_books_set = BookInfoo.objects.all()
    nameofbook = []
    priceofbook = []
    urlofbook = []
    for i in a_books_set:
        if(i.bookname[0]=='a' or i.bookname[0]=='A'):
            nameofbook.append(i.bookname)
            priceofbook.append(i.bookprice)
            urlofbook.append(i.bookurl)
    abooks = {'abooks':nameofbook,'aprice':priceofbook,'store':store,'aurl':urlofbook}
    return render(request,"aBooks.html",abooks)
    
def b(request):
    b_books_set = BookInfoo.objects.all()
    nameofbook = []
    priceofbook = []
    urlofbook = []
    for i in b_books_set:
        if(i.bookname[0]=='b' or i.bookname[0]=='B'):
            nameofbook.append(i.bookname)
            priceofbook.append(i.bookprice)
            urlofbook.append(i.bookurl)
    bbooks = {'bbooks':nameofbook,'bprice':priceofbook,'store':store,'burl':urlofbook}
    return render(request,"bBooks.html",bbooks)

def c(request):
    c_books_set = BookInfoo.objects.all()
    nameofbook = []
    priceofbook = []
    urlofbook = []
    for i in c_books_set:
        if(i.bookname[0]=='c' or i.bookname[0]=='C'):
            nameofbook.append(i.bookname)
            priceofbook.append(i.bookprice)
            urlofbook.append(i.bookurl)
    cbooks = {'cbooks':nameofbook,'cprice':priceofbook,'store':store,'curl':urlofbook}
    return render(request,"cBooks.html",cbooks)

def search(request):
    all_books_set = BookInfoo.objects.all()
    nameofbook = []
    priceofbook = []
    urlofbook = []
    for i in all_books_set:
        if(searchedvalue == i.bookname):
            nameofbook.append(i.bookname)
            priceofbook.append(i.bookprice)
            urlofbook.append(i.bookurl)

    sbooks = {'sbooks':nameofbook,'sprice':priceofbook,'store':store,'surl':urlofbook,'searchedbookname':searchedvalue}
    return render(request,"search.html",sbooks)

print(searchedvalue)