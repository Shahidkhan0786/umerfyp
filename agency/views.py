from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer

from .models import MyProfile,orders
from django.views.generic import UpdateView, DetailView
from django.views.generic.detail import  DetailView
from flydigital import settings
# Create your views here.
from . serializers import ordersSerializer

def index(request):
    return render(request , 'agency/index.html')


def Support(request):
    if request.method=="POST":

        name=request.POST['name']
        mail = request.POST['mail']
        message = request.POST['message']

        if name and message and mail:
            try:
                ctx = {

                    'user': name,

                    'emaill': mail,
                    'message': message,
                }
                message = get_template('agency/maill.html').render(ctx)
                msg = EmailMessage(
                    "Support Email",
                     message,
                    'settings.EMAIL_HOST_USER',
                    ["myflydigital@gmail.com"],
                )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
                messages.success(request ,"Mail successfully sent")
                return render(request , '/support')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/support')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request , 'agency/contactus.html')

@login_required()
def pricingx(request):
    return render(request , 'agency/pricingx.html')

def Postpro(request):
    return render(request , 'agency/porno.html')

def Custom(request):
    return render(request , 'agency/custom.html')


def order_requirments(request):

    if request.method=="POST":

        ser=request.POST['service']
        runt = request.POST['time']
        fdat = request.POST['date']
        pro = request.FILES['proj']
        sam = request.FILES['sample']
        scont = request.POST['content']
        pkr = request.POST['pkg']
        userx= request.user
        print(userx)
        usr = MyProfile.objects.get(user = userx)
        print(usr)
        x=orders(client=usr , service=ser ,package =pkr, run_time=runt , video=pro , sample_video=sam, finish_date=fdat ,Requirments = scont)
        x.save()

        return redirect('/payment/')
    return render(request , 'agency/order_requirment.html')


def post_production(request):
    return render(request , 'agency/post-production.html')


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = MyProfile
    fields = ["name", "age",'city', "address", 'zipcode',"status", "gender", "phone_no", "description", "pic"]


# @method_decorator(login_required, name="dispatch")
# class MyProfileDetailView(DetailView):
#     print("hoooooooooooooooooo")
#     model = MyProfile


class ProfileDetailView(DetailView):
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,")
    model = MyProfile


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usr=MyProfile.objects.get(user = self.request.user)
        try:
            xt=orders.objects.filter(client=usr).first()
            context['id'] = xt.id
            context['status'] = xt.status
            context['end'] = xt.finish_date
            context['time'] = xt.time
        except:
            print("")

        return context



def orders_history(request):
    usr= request.user;
    getord=MyProfile.objects.get(user = usr)
    orderss=orders.objects.filter(client= getord)

    dat = {'ord':orderss}
    return render(request , 'agency/orderhistory.html' ,dat)


def cancelord(request , id):

    try:
        instance=orders.objects.get(id = id)

    except:
        pass
    return render(request , 'agency/payment.html')






def payment(request):
    return render(request , 'agency/payment.html')
def about(request):
    return render(request , 'agency/corporate.html')



def orderss_detail(request):
    stu = orders.objects.all()
    serializer = ordersSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data , content_type='application/json')