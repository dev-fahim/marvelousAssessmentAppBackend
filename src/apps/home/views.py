from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project.core.utils.utils import get_main_user_model
# Create your views here.


@login_required
def home(request):
    main_user = get_main_user_model(request)
    return render(request, 'index.html', {'user': main_user})
