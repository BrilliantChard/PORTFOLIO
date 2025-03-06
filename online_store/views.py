from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "index.html")
    return render(request, "index.css")
    return render(request, "form.css")
    return render(request, "footer.css")
