from django.shortcuts import render
from django.http import HttpResponse
from .models import featured_ideas , features_web


 #Create your views here.
def index(request):

    feats_ideas = featured_ideas.objects.all() 
    feats_web = features_web.objects.all()
    return render(request, 'index.html' , {'feats_ideas' : feats_ideas , 'feats_web' : feats_web}  )


def login(request):
    return render(request, 'login.html')


def postsign(request):
    email = request.POST.get('user')
    passw = request.POST.get('password')

    '''try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "Invalid Credentials"

        return render(request, 'login.html', {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'welcome.html', {"e": email})'''


def logout(request):
    auth.logout(request)
    return render(request, "login.html")


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('pass')
    user = authe.create_user_with_email_and_password(email, password)

    uid = user['localId']
    data = {"name": name, "status": "1"}

    database.child("users").child(uid).child("details").set(data)

    return render(request, "login.html")



























'''def index(request):
    feat1 = featured_ideas()
    feat1.idea_title = 'machine learning'
    #feat1.img = 
    feat1.desc = 'The batman who laughs'

    feat2 = featured_ideas()
    feat2.idea_title = 'machine learning'
    #feat2.img = 
    feat2.desc = 'The batman who laughs'

    feat3 = featured_ideas()
    feat3.idea_title = 'machine learning'
    #feat3.img = 
    feat3.desc = 'The batman who laughs'

    feats = [feat1 , feat2 , feat3]
    return render(request,"index.html" , {'feats' : feats})'''
