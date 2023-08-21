from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.shortcuts import redirect

html_base = """
      <h1>AUCAR</h1>
      <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Nosotros</a></li>
        <li><a href="/modelos/">Modelos</a></li>
        <li><a href="/contact/">Contacto</a></li>
      </ul>  
"""         

# Create your views here.
def home(resquest):
   return render (resquest, "core/home.html")

def about(resquest):
     return render (resquest, "core/about.html")

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('nombre')
        last_name = request.POST.get('apellido')
        email = request.POST.get('email')
        phone = request.POST.get('telefono')

        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone
        )

        messages.success(request, '¡Gracias por tu mensaje! Te contactaremos pronto.')
        return redirect('contact')

    return render(request, 'core/contact.html')