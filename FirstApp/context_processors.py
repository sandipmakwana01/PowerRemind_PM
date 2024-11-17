# myapp/context_processors.py
def user_session_data(request):
    user_name = request.session.get('user_name')
    password = request.session.get('password')
    return {
        'user_name': user_name,
        'password': password,
    }
