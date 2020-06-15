from django.shortcuts import render, redirect
from .models import User ,SubscribeUser


def user_save(req):
    if req.method == 'GET':
        return render(req, 'index.html')
    else:
        user = User(name = req.POST['uname'],
                    email = req.POST['uemail'],
                    message = req.POST['umessage'],
                    contact = req.POST['uphone'], )

        user.save()
        return render(req, 'index.html', {"user": User.objects.all()})



def sub_user_save_faq(req):
    if req.method == 'GET':
        return render(req, 'faq.html')

    else:
        subuser = SubscribeUser(sub_email = req.POST['semail'],)

        subuser.save()
        return render(req, 'faq.html',{
                                      "sub_user": SubscribeUser.objects.all()})

def sub_user_save_media(req):
    if req.method == 'GET':
        return render(req, 'media-and-insights.html')

    else:
        sub = SubscribeUser(sub_email = req.POST['semail'],)

        sub.save()
        return render(req, 'media-and-insights.html',{
                                      "sub_user": SubscribeUser.objects.all()})
