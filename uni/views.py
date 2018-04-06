# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import quandl
import pandas
from django.shortcuts import render
from uni.forms import UserForm, UserProfileForm, PortfolioForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from uni.models import UserProfile, Post

def index(request):
    context = RequestContext(request)
    val1 = request.user.username
    print(type(request.user))
    print(val1)
    print(type(val1))
    context_dict = {}
    if request.user.is_authenticated:
        for person in UserProfile.objects.all():
            if str(person) == str(val1):
                context_dict['AAPL']=person.AAPLvalue
                context_dict['CSCO']=person.CSCOvalue
                context_dict['CAT']=person.CATvalue
                context_dict['BA']=person.BAvalue
                context_dict['CVX']=person.CVXvalue
        print('Jamapelle')

    print(context_dict)

    return render_to_response('uni/index.html', context_dict, context)


def about(request):
	return HttpResponse("Something will be displayed here.")


def contact(request):
	return HttpResponse("Something will be displayed here.")






def parent(request):
	return HttpResponse("Something will be displayed here.")


def intro(request):
	return HttpResponse("Something will be displayed here.")

def user_portfolio(request):
    val = request.GET 
    print(val)
    #Print current user
    curruser = request.user
    print(curruser)
    print(type(curruser))
    for person in UserProfile.objects.all():
        print('Iterating')
        print(person)
        print(type(person))
        print(str(curruser))
        if str(person) == str(curruser):
            person.AAPLvalue=person.AAPLvalue+10
            print('Value was set to ' + str(person.AAPLvalue))
            person.save()


   
    for person in UserProfile.objects.all():
        print(person.AAPLvalue)
        print(person)
        print(type(person))
        print("Mah")
    return HttpResponse("Something will be displayed here.")


def trending(request):
    val1 = request.user.username
    context = RequestContext(request)
    quandl.ApiConfig.api_key = 't6FmfCu4FXsfHDX4_omH'
    table = quandl.get_table('SHARADAR/SEP', date='2018-02-09', ticker='AAPL,CSCO,CAT,BA,CVX')
	#table = quandl.get_table('SHARADAR/SEP', date='2018-02-09', ticker='AAPL')
    arr = table.to_dict()
    context_dict = arr
	
    if request.user.is_authenticated:
        for person in UserProfile.objects.all():
            if str(person) == str(val1):
                context_dict['AAPL']=person.AAPLvalue
                context_dict['CSCO']=person.CSCOvalue
                context_dict['CAT']=person.CATvalue
                context_dict['BA']=person.BAvalue
                context_dict['CVX']=person.CVXvalue
        print('Jamapelle')

    temp ={}

    if request.user.is_authenticated:
        for person in UserProfile.objects.all():
            if str(person) == str(val1):
                temp['AAPL']=person.AAPLvalue
                temp['CSCO']=person.CSCOvalue
                temp['CAT']=person.CATvalue
                temp['BA']=person.BAvalue
                temp['CVX']=person.CVXvalue

    context_dict['values']=temp


    print(context_dict)

	#print(arr)
    
    return render_to_response('uni/trending.html', context_dict, context)
	#return HttpResponse("Something will be displayed here.")

def news(request):
    
    final_dict = {}
    i=int(0)
    context = RequestContext(request)
    for item in Post.objects.all():
        context_dict={}
        context_dict['title']=item.title
        context_dict['content']=item.content
        context_dict['user']=item.user
        final_dict[i] = context_dict
        print(context_dict)
        print(final_dict[i])
        if i>0:
            print(final_dict[i-1])
        print('End of printing')
        i=i+1

    print('Final dict')
    print(final_dict)
    print('Final dict ended')
    final2_dict={}

    final2_dict['entry'] = final_dict

    print(request.method)
    final2_dict['commentname']=""

    if request.method == 'POST':
        print('Requested method is post')
        print(request.POST['commentname'])
        final2_dict['commentname'] = request.POST['commentname']
        final2_dict['commentuser'] = request.user.username


    return render_to_response('uni/news.html', final2_dict, context)


def dashboard(request):
    if request.method == 'POST':
        print('Requested method is post')
    else:
        print('Requested method is not post')
    temp ={}
    context = RequestContext(request)
    val1 = request.user.username

    if request.user.is_authenticated:
        for person in UserProfile.objects.all():
            if str(person) == str(val1):
                temp['AAPL']=person.AAPLvalue
                temp['CSCO']=person.CSCOvalue
                temp['CAT']=person.CATvalue
                temp['BA']=person.BAvalue
                temp['CVX']=person.CVXvalue

    return render_to_response('uni/dashboard.html', temp, context)



def blockchain(request):
	return HttpResponse("Something will be displayed here.")


def crypto(request):
	return HttpResponse("Something will be displayed here.")


def colleges(request):
	return HttpResponse("Something will be displayed here.")

def writeblog(request):
    temp = {}
    context = RequestContext(request)
    return render_to_response('uni/writeblog.html', temp, context)

def postblog(request):
    if request.method == 'POST':
        print(request.POST)
    else:
        print("Get request")
    temp ={}
    temp['title'] = request.POST['title']
    temp['content'] = request.POST['content']
    curruser = request.user.username
    temp['curruser'] = curruser
    context = RequestContext(request)
    obj = Post()
    obj.title = request.POST['title']
    obj.content = request.POST['content']
    obj.user = request.user.username
    obj.save()
    print('Object')
    print(obj)
    return render_to_response('uni/postblog.html', temp, context)

def transact(request):
    temp ={}
    context = RequestContext(request)
    val1 = request.user.username

    if request.user.is_authenticated:
        for person in UserProfile.objects.all():
            if str(person) == str(val1):
                temp['AAPL']=person.AAPLvalue
                temp['CSCO']=person.CSCOvalue
                temp['CAT']=person.CATvalue
                temp['BA']=person.BAvalue
                temp['CVX']=person.CVXvalue

    return render_to_response('uni/transact.html', temp, context)

def transact2(request):
    temp ={}
    context = RequestContext(request)
    val1 = request.user.username

    if request.user.is_authenticated:
        for person in UserProfile.objects.all():
            if str(person) == str(val1):
                temp['AAPL']=person.AAPLvalue
                temp['CSCO']=person.CSCOvalue
                temp['CAT']=person.CATvalue
                temp['BA']=person.BAvalue
                temp['CVX']=person.CVXvalue
    temp2={}
    temp2['temp']=temp

    return render_to_response('uni/transact2.html', temp2, context)

def increase(request):

    print(request.method)

    if request.method == 'POST':
        
        print("Amazing")
        print(request.POST)
        user_form = UserForm(data=request.POST)
        portfolio_form = PortfolioForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        extra = request.POST['quantity']
        choice = request.POST['choice']
        extra = int(extra)

        curruser = request.user
 
        for person in UserProfile.objects.all():
            if str(person) == str(curruser):
                if choice=="AAPL":
                    if person.AAPLvalue is not None:
                        person.AAPLvalue = int(person.AAPLvalue) + extra
                    else:
                        person.AAPLvalue = extra
                if choice=="BA":
                    if person.BAvalue is not None:
                        person.BAvalue = int(person.BAvalue) + extra
                    else:
                        person.BAvalue = extra
                if choice=="CSCO":
                    if person.CSCOvalue is not None:
                        person.CSCOvalue = int(person.CSCOvalue) + extra
                    else:
                        person.CSCOvalue = extra
                if choice=="CVX":
                    if person.CVXvalue is not None:
                        person.CVXvalue = int(person.CVXvalue) + extra
                    else:
                        person.CVXvalue = extra
                if choice=="CAT":
                    if person.CATvalue is not None:
                        person.CATvalue = int(person.CATvalue) + extra
                    else:
                        person.CATvalue = extra
                person.save()
        print(person.AAPLvalue)
        

    temp ={}
    context = RequestContext(request)
    val1 = request.user.username

    if request.user.is_authenticated:
        for person in UserProfile.objects.all():
            if str(person) == str(val1):
                temp['AAPL']=person.AAPLvalue
                temp['CSCO']=person.CSCOvalue
                temp['CAT']=person.CATvalue
                temp['BA']=person.BAvalue
                temp['CVX']=person.CVXvalue

    return render_to_response('uni/log.html', temp, context)


def decrease(request):

    print(request.method)

    if request.method == 'POST':
        
        print("Amazing")
        print(request.POST)
        user_form = UserForm(data=request.POST)
        portfolio_form = PortfolioForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        extra = request.POST['quantity']
        choice = request.POST['choice']
        extra = int(extra)



        curruser = request.user

        flag = False

        for person in UserProfile.objects.all():
            if str(person) == str(curruser):
                if choice=="AAPL":
                    if extra>person.AAPLvalue:
                        print('Exception found')
                        flag=True
                if choice=="BA":
                    if extra>person.BAvalue:
                        print('Exception found')
                        flag=True
                if choice=="CSCO":
                    if extra>person.CSCOvalue:
                        print('Exception found')
                        flag=True
                if choice=="CVX":
                    if extra>person.CVXvalue:
                        print('Exception found')
                        flag=True
                if choice=="CAT":
                    if extra>person.CATvalue:
                        print('Exception found')
                        flag=True



 
        for person in UserProfile.objects.all():
            if str(person) == str(curruser):
                if choice=="AAPL" and flag==False:
                    if person.AAPLvalue is not None:
                        person.AAPLvalue = int(person.AAPLvalue) - extra
                    else:
                        person.AAPLvalue = extra
                if choice=="BA" and flag==False:
                    if person.BAvalue is not None:
                        person.BAvalue = int(person.BAvalue) - extra
                    else:
                        person.BAvalue = extra
                if choice=="CSCO" and flag==False:
                    if person.CSCOvalue is not None:
                        person.CSCOvalue = int(person.CSCOvalue) - extra
                    else:
                        person.CSCOvalue = extra
                if choice=="CVX" and flag==False:
                    if person.CVXvalue is not None:
                        person.CVXvalue = int(person.CVXvalue) - extra
                    else:
                        person.CVXvalue = extra
                if choice=="CAT" and flag==False:
                    if person.CATvalue is not None:
                        person.CATvalue = int(person.CATvalue) - extra
                    else:
                        person.CATvalue = extra
                person.save()
        print(person.AAPLvalue)
        

    temp ={}
    context = RequestContext(request)
    val1 = request.user.username

    if request.user.is_authenticated:
        for person in UserProfile.objects.all():
            if str(person) == str(val1):
                temp['AAPL']=person.AAPLvalue
                temp['CSCO']=person.CSCOvalue
                temp['CAT']=person.CATvalue
                temp['BA']=person.BAvalue
                temp['CVX']=person.CVXvalue
    if flag==True:
        temp['flag']=1
    else:
        temp['flag']=0

    return render_to_response('uni/log.html', temp, context)






def register(request):
    registered = False

    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()

            
            user.set_password(user.password)
            user.save()

            print('User is saved')

            
            profile = profile_form.save(commit=False)
            profile.user = user

            
         

            
            profile.save()

            
            registered = True

        
        else:
            print user_form.errors, profile_form.errors

    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    
    return render(request,
            'uni/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



def user_login(request):

    print("Login was called")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        
        if user:
            
            if user.is_active:
               
                login(request, user)
                return HttpResponseRedirect('/uni/')
            else:
                
                return HttpResponse("Your account is disabled.")
        else:
            
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    
    else:
     
        return render(request, 'uni/login.html', {})


from django.contrib.auth import logout


def user_logout(request):
    
    logout(request)

    
    return HttpResponseRedirect('/uni/')