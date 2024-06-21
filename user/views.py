from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from .models import Account, Admin, User
from .serializers import AccountSerializer, AdminSerializer
import json

def returnJson(data = None, errorCode = 0, cookies = ''):
    if data is None:
        data = []
    return JsonResponse({'errorCode' : errorCode, 'data' : data, 'cookies' : cookies})

# get all account
def accounts_list(request):
    if request.method == 'GET':
        accounts = Admin.objects.all()
        return returnJson([dict(account.body()) for account in accounts])

# get all admin
def admins_list(request):
    if request.method == 'GET':
        admins = Admin.objects.all()
        return returnJson([dict(admin.body()) for admin in admins])
    
# get specific account
def account(request, pk):
    try:
        account = Account.objects.get(id = pk)
    except Account.DoesNotExist:
        return returnJson([], 404)
    return returnJson([dict(account.body())])

# get specific admin
def admin(request, pk):
    try:
        admin = Admin.objects.get(id = pk)
    except Admin.DoesNotExist:
        return returnJson([], 404)
    return returnJson([dict(admin.body())])

# login
def user_login(request):
    data = json.loads(request.body)

    username = data["username"]
    password = data["password"]
    user = authenticate(request, username = username, password = password)

    if user is not None:
        login(request, user)

        try:
            account = Account.objects.get(username = username)
            return returnJson([dict(account.body())], 0, {'user': 'Account', 'id' : account.id, 'username' : account.username})
        except Account.DoesNotExist:
            try:
                admin = Admin.objects.get(username = username)
                return returnJson([dict(admin.body())], 0, {'user': 'Admin', 'id' : admin.id, 'username' : admin.username})
            except Admin.DoesNotExist:
                logout(request)
                return returnJson([], 404)
    else:
        return returnJson([], 404, {'username' : username, 'password' : password})

# logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return returnJson([])
    else:
        return returnJson([], 404)

# create an account   
def create_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            user = User.objects.get(username = data["username"])
        except User.DoesNotExist:
            account = Account.objects.create()
            account.username = data["username"]
            account.set_password(data["password"])
            account.gender = data["gender"]

            account.save()
            return returnJson([dict(account.body())])
        return returnJson([], 400)

# delete an account
def delete_account(request, pk):
    if request.method == 'DELETE':
        try:
            account = Account.objects.get(id = pk)
            account.delete()

            accounts = Account.objects.all()
            return returnJson([dict(account.body()) for account in accounts])
        except Account.DoesNotExist:
            return returnJson([], 400)

def delete_admin(request, pk):
    if request.method == 'DELETE':
        try:
            admin = Admin.objects.get(id = pk)
            admin.delete()

            return returnJson([], 0)
        
        except Admin.DoesNotExist:
            return returnJson([], 400)
        
# create an admin account   
def create_admin(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            user = User.objects.get(username = data["username"])
        except User.DoesNotExist:
            admin = Admin.objects.create()
            admin.username = data["username"]
            admin.set_password(data["password"])
            admin.gender = data["gender"]

            admin.save()
            return returnJson([dict(admin.body())])
        return returnJson([], 400)

# edit username
def edit_username(request, pk):
    try:
        admin = Admin.objects.get(id = pk)

        if request.method == 'POST':
            data = json.loads(request.body)

            try:
                check = Admin.objects.get(username = data['username'])
                return returnJson([], 404)
            
            except:
                admin.username = data['username']
                admin.save()

                return returnJson([dict(admin.body())])
    
    except Admin.DoesNotExist:
        try:
            account = Account.objects.get(id = pk)

            if request.method == 'POST':
                data = json.loads(request.body)

                try:
                    check = Account.objects.get(username = data['username'])
                    return returnJson([], 404)
                
                except:
                    account.username = data['username']
                    account.save()

                    return returnJson([dict(account.body())])

        except Account.DoesNotExist:
            return returnJson([], 0, 0, 404)

def edit_gender(request, pk):
    data = json.loads(request.body)

    try:
        admin = Admin.objects.get(id=pk)
        admin.gender = data["gender"]
        admin.save()

        return returnJson([dict(admin.body())])
    
    except Admin.DoesNotExist:
        account = Account.objects.get(id=pk)
        account.gender = data["gender"]
        account.save()

        return returnJson([dict(account.body())])
        

# admin change password
def admin_change_password(request, pk):
    try:
        admin = Admin.objects.get(id=pk)

    except Admin.DoesNotExist:
        return returnJson([], 404)
    
    if request.method == 'PUT':
        data = json.loads(request.body)

        admin.set_password(data['password'])
        admin.save()

        return returnJson([dict(admin.body())])
    
# account change password
def account_change_password(request, pk):
    try:
        account = Account.objects.get(id=pk)

    except Account.DoesNotExist:
        return returnJson([], 404)
    
    if request.method == 'PUT':
        data = json.loads(request.body)

        account.set_password(data['password'])
        account.save()

        return returnJson([dict(account.body())])