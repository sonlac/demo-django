from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import UploadManager
from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import UploadFileForm
from models import UploadFile
from django.contrib.auth.decorators import login_required

import numpy as np
import datetime

@login_required
def user_model_list(request, username=None):
    if not username:
        username = request.user.username

    latest_model_list = UploadManager.objects.all().order_by('-date_uploaded')
    if username != 'admin':
        latest_model_list = UploadManager.objects.filter(uploaded_by_user=username).order_by('-date_uploaded')

    count_models = UploadManager.objects.filter(uploaded_by_user=username).count()

    badges = {}
    delta = datetime.datetime.now(timezone.utc) - request.user.date_joined
    x = np.timedelta64(delta, 'D')
    y = x/np.timedelta64(1, 'D')

    if count_models > 5:
        badges['Collector'] = True # having the badge 'Collector' if the number of model uploaded > 5 models
    if y > 50: # having the badge 'Pioneer' if the user has been registered since more than 1 year
        # Here to demo, > 50 days -> show badge
        badges['Pioneer'] = True

    # TODO
    # if views > 1k views -> 'Star' badge

    context = {'latest_model_list': latest_model_list, 'username': username, 'badges' : badges}
    return render(request, 'models/user_model_list.html', context)

def upload_model(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            upload_manager = UploadManager()
            upload_manager.filepath='uploads/%Y/%m/%d'
            now = timezone.now()
            upload_manager.filepath = 'uploads/' + now.strftime('%Y:%m:%d').replace(":", "/")
            upload_manager.filename = request.FILES['file']
            user_name = request.user.username
            upload_manager.uploaded_by_user = user_name
            upload_manager.date_uploaded = datetime.datetime.now()
            upload_manager.save()
            new_file.save()

            return HttpResponseRedirect(reverse('models:upload_model'))
    else:
        form = UploadFileForm()

    data = {'form': form}
    return render_to_response('models/upload.html', data, context_instance=RequestContext(request))