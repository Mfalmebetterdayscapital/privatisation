
from django.http import response
from django.shortcuts import render
import requests
from .models import Video,Gallery
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
from .models import PrivitasationUsers,Gallery,Video,AvailableOpening


# /home/willy/backend/django gava/views.py

from django.shortcuts import render

def act_view(request):
    return render(request, 'act.html')

def benefits_view(request):
    return render(request, 'benefits.html')

def board_view(request):
    return render(request, 'board.html')

def business_view(request):
    return render(request, 'business.html')

def completed_view(request):
    return render(request, 'completed.html')

def contact_view(request):
    return render(request, 'contact.html')

def corporate_view(request):
    return render(request, 'corporate.html')

def csr_view(request):
    return render(request, 'csr.html')

def entreprise_view(request):
    return render(request, 'entreprise.html')

def expressions_view(request):
    return render(request, 'expressions.html')

def images_view(request):
    images=Gallery.objects.all()
    return render(request, 'images.html',{'images':images})

def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def management_view(request):
    return render(request, 'management.html')

def mandate_view(request):
    return render(request, 'mandate.html')

def mechanism_view(request):
    return render(request, 'mechanism.html')

def news_view(request):
    return render(request, 'news.html')

def plan_view(request):
    return render(request, 'plan.html')

def policy_view(request):
    return render(request, 'policy.html')

def portal_view(request):
    position=AvailableOpening.objects.all()
    user_id=request.session.get('user_id')
    return render(request, 'portal.html',{'positions':position,'user_id':user_id})

def privatisation_view(request):
    return render(request, 'privatisation.html')

def process_view(request):
    return render(request, 'process.html')

def proposal_view(request):
    return render(request, 'proposal.html')

def recent_view(request):
    return render(request, 'recent.html')

def register_view(request):

    return render(request, 'register.html')

def research_view(request):
    return render(request, 'research.html')

def search_view(request):
    return render(request, 'search.html')

def status_view(request):
    return render(request, 'status.html')

def success_view(request):
    return render(request, 'success.html')

def tenders_view(request):
    return render(request, 'tenders.html')

def text_view(request):
    return render(request, 'text.html')

def vacancies_view(request):
    return render(request, 'vacancies.html')

def videos_view(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', {'videos': videos})

def message (request):
    phone = request.POST.get('phone',False)
    email = request.POST.get('email',False)
    name = request.POST.get('name',False)
    message = request.POST.get('message',False)
    sender=settings.EMAIL_HOST_USER
    recipients = ['wilsonmwaura697@gmail.com']
    subject="your have a message from "  + name
    print(subject)
    message=f'{phone}\nMessage: {message}'
    
    

    try:
        send_mail(subject, message, sender, recipients)

        print('Your message has been sent successfully.')
        return redirect('/index')  # Redirect to a success page or some other page
    except Exception as e:
        print('An error occurred: {e}')
        return redirect('/index')

def create_account(request):
    password1= request.POST.get('password', False)
    print(password1)
    password2 = request.POST.get('password1', False)
    print(password2)
    email = request.POST.get('email', False)
    print(email)
    name = request.POST.get('name', False)
    print(name)
    phone = request.POST.get('phone', False)
    print(phone)
    company = request.POST.get('company', False)
    print(company)
    kra = request.POST.get('name', False)
    print(kra)

    


    if  password1 != password2:
        message="the two passwords are diffrent."
        return render(request, "register.html", {"message": message})

        # Check if email and password are provided
    if not email or not password1:
        message="Email and password are required."
        return render(request, "register.html", {"message": message})

        # Check if user already exists
    if PrivitasationUsers.objects.filter(email=email).exists():
        
        message="User with this email already exists.."
        return render(request, "register.html", {"message": message})

        # Create user
    user = PrivitasationUsers.objects.create(email=email, password=password1,name=name,company=company,kra=kra,phone=phone)
    try:
        
        subject = 'Thank you'
        message = '''Thank you for signing up,
            Your Account is now active,
             use:
           https://privatisation.go.ke/ '''
  
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        print("sending email")
        try:
            send_mail(subject, message, from_email, recipient_list)
            return redirect("/login")
        except:
            return redirect("/login")
    
    except Exception as e:
        print(f"Failed to send email. Error message: {str(e)}")
        return redirect("/register")
def auth_login(request):
    email = request.POST.get('email',False)
    password = request.POST.get('password',False)

        # Check if an email and password are provided
    if not email or not password:
        
        message= "Email and password are required."
        return render(request, "login.html", {"message": message})

    try:
            # Check if user exists
        user =PrivitasationUsers.objects.get(email=email,password=password)
    except PrivitasationUsers.DoesNotExist:
        
        message= "User does not exist.You need to sign up please."
        return render(request, "login.html", {"message": message})

        # Check if password is correct
    if user.password != password:
        
        message= "You provided an incorrect password."
        return render(request, "login.html", {"message": message})
    request.session['user_id'] = user.id

 
    return redirect('index')

def logout(request):
    user_id=request.session.get('user_id')
    if user_id is  not None:
        del request.session['user_id']
        return redirect("/index")
    else:
        return redirect("/index")

def downloads(request):
    return render (request,"downloads.html")
