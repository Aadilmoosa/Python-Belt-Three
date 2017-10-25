from django.shortcuts import render, redirect, HttpResponse

from .models import *

from django.contrib import messages

# ===================================================
#                   Render
# ===================================================

def index(request):
    return render(request, "login_reg/index.html")

def Dashboard(request):
    if 'user_id' not in request.session:
        return redirect("/")

    user = User.objects.get(id=request.session['user_id'])

    friends = user.friends.all()

    friendslist = []
    for friend in friends:
        friendslist.append(friend)
    nonfriends = User.objects.all().exclude(first_name=user.first_name)
    for friend in friendslist:
        nonfriends = nonfriends.exclude(first_name=friend.first_name)
    context = {
        'user': user,
        'friends': friends,
        'nonfriends': nonfriends,
    }
    return render(request, "login_reg/Dashboard.html", context)


# ===================================================
#                   Process
# ===================================================

def register(request):
    errors = User.objects.regvalidation(request.POST)

    if errors:
        for key, message in errors.iteritems():
            messages.error(request, message, extra_tags=key)
        return redirect("/")
    user = User.objects.newUser(request.POST)
    request.session['user_id'] = user.id
    return redirect("/Dashboard")

def login(request):
    user = User.objects.login(request.POST)
    if user:
        request.session['user_id'] = user.id
        return redirect('/Dashboard')

    messages.error(request,"email or password invalid", extra_tags="login") 
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
        }
    return render(request, "login_reg/2.html", context)

def addfriend(request, user_id):
    newfriend = User.objects.get(id=user_id)
    user = User.objects.get(id=request.session['user_id'])
    user.friends.add(newfriend)
    user.save()
    newfriend.friends.add(user)
    return redirect('/Dashboard')

def deletefriend(request, user_id):
    notfriend = User.objects.get(id=user_id)
    user = User.objects.get(id=request.session['user_id'])
    user.friends.remove(notfriend)
    user.save()
    notfriend.friends.remove(user)
    return redirect('/Dashboard')






# def show_user(request, id):
#     profile = User.objects.get(id=id)
#     context = {
#         'user' : profile
#     }

# def addFriend(request, id):
#     Friend.FriendManager.addFriend(request.session['id'], id)

#     return redirect('/friends')

# def removeFriend(request, id):
#     Friend.FriendManager.removeFriend(request.session['id'], id)

#     return redirect('/friends')