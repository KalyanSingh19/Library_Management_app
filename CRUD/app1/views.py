from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import BookRegistration
from .models import Books
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


# Create your views here.
@csrf_protect
def home(request):
    
    if request.method == 'POST':
        det = BookRegistration(request.POST)
        if det.is_valid():
            regis = det.cleaned_data['reg']
            title = det.cleaned_data['title']
            issued = det.cleaned_data['issued']
            author = det.cleaned_data['author']
            availability = det.cleaned_data['availability']
            show = Books()
            show.reg = regis
            show.title = title
            show.issued = issued
            show.author = author
            show.availability = availability
            show.save()
    else:
        
        det = BookRegistration()
    stud = Books.objects.all()
        
    return render(request,'add.html',{'form':det,'book':stud})

def delete_data(request,id):
    if request.method == 'POST':
        pi = Books.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
#def update_data(request,id):
    #if request.method == 'POST':
        #pi = Books.objects.get(pk=id)
        #det = BookRegistration(request.POST,instance=pi)
        #if det.is_valid:
           # det.save()
    #else:
        #pi = Books.objects.get(pk=id)
        #det = BookRegistration(instance=pi)
    #return render(request,'new.html',{'form':det})

def update_data(request, id):
    book = get_object_or_404(Books, pk=id)  # Ensure book exists before update
    if request.method == 'POST':
        det = BookRegistration(request.POST, instance=book)  # Update existing book
        if det.is_valid():
            det.save()  # Success message
            return HttpResponseRedirect('/')  # Redirect to homepage after update
        else:
            messages.error(request, 'Please correct the errors in the form.')  # Error message
    else:
        det = BookRegistration(instance=book)  # Pre-populate the form for GET
    return render(request, 'new.html', {'form': det})