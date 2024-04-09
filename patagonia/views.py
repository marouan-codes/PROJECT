
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 
from django.contrib import messages
from .models import portfolo
from .models import blog
from .models import adawat
from mysite.forms import contactform
from django.core.mail import EmailMessage

def index(request):
    portfolios = portfolo.objects.all()
    context = {'portfolios' :portfolios}
    return render(request, 'patagonia/index.html', context)

def work(request):
    zorks = portfolo.objects.all()
    context = {'zorks' :zorks}
    return render(request, 'patagonia/portfolio.html', context)

def tool(request):
    adat = adawat.objects.all()  # Use the correct model name 'adawat'
    context = {'tools' :adat}
    return render(request, 'patagonia/adawat.html', context)

def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            # Process the form data here if needed
            if form.is_valid():
    # Access cleaned form data
                full_name = form.cleaned_data['full_name']
                email = form.cleaned_data['email']
                current_website = form.cleaned_data['current_website']
                business_do = form.cleaned_data['business_do']

                subject = 'Contact form submission from {}'.format(full_name)
                message = f"full name: {full_name}\nBusiness Do: {business_do}\nCurrent Website: {current_website}\nemail: {email}"
                from_email = email
                recipient_list = ['marouan.kaboul@webstooone.com']
                reply_to = [email]

                email_message = EmailMessage(subject, message, from_email, recipient_list, reply_to)
                
                # Use send() method on the EmailMessage instance, not on recipient_list
                email_message.send()

            success_message = "Form submitted successfully!"
            messages.success(request, success_message)
            # return redirect('success')
    else:
        form = contactform()


    return render(request, 'patagonia/contact.html', {'form': form})



def portfoliopage(request, slug):
        postl = get_object_or_404(portfolo, slug=slug)
        context = {'p': postl}
        return render(request, 'patagonia/portfoliopage.html', context)



def blogs(request):
    blogi = blog.objects.all()
    context = {'blogi' :blogi}

    if not blogi:  # Check if there are no articles
        context['message'] = "No articles available at the moment."
    
    return render(request, 'patagonia/blog.html', context)


def blogpage(request, slug):
        blogl = get_object_or_404(blog, slug=slug)
        context = {'b': blogl}
        return render(request, 'patagonia/blogpage.html', context)