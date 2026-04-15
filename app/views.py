from django.shortcuts import render
from .models import Contact





def home(request):
    
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        

        return render(request, "index.html", {"success": True})

    return render(request, "index.html")

