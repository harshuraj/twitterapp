from django.shortcuts import render
import tweepy
import re
from tweepy import OAuthHandler
from .models import Product
# Create your views here.
def home(request):
	#ckey=request.POST['ckkey']
	#csecret=request.POST['cssecret']
	#atoken=request.POST['attoken']
	#asecret=request.POST['assecret']
	ckey='RU1y7RD1QkUhz7yGCJhnXVBre'
	csecret='edq2ZWYribc1EIHKmDkirmAOGFeM8epAiJa4w9gJX8b9k7ZljK'
	atoken='972772531496202240-BIjYJxl6yVKFf63RTA5Fa5fbhfgnKQG'
	asecret='8qr06qvIx2KD1iDaB2VXIwofq3WL9URkBZxsxSD6P4PnO'
	url=re.compile(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([^/. ]*\/?)*')

	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	api = tweepy.API(auth)
	for status in api.home_timeline(count=100):
	    # Process a single statu
	    product=Product()
	    val1=""
	    product.name=status.user._json['name']
	    str=status.text
	    str=str.rsplit(' ', 1)[0]
	    mo=url.finditer(str)
	    l=list(mo)
	    for i in l:
	        val1=i.group()
	        if val1.startswith('http://') or val1.startswith('https://'):
	            product.url=val1
	            product.pub_date=status.created_at
	            product.save()
	return render(request,'loginfeed/login.html')

def index(request):
	    products = Product.objects
	    return render(request,'loginfeed/index.html',{'products':products})