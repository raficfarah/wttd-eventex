import hashlib
from django.conf import settings
from django.template.loader import render_to_string
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})



def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    subscription = form.save()    
    subscription.save()

    # Send subscripton email
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    return HttpResponseRedirect(r('subscriptions:detail', subscription.hashid))


def detail(request, hashid):
    try:
        subscription = Subscription.objects.get(hashid=hashid)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])


def value_hasher(*args):
    to_be_hashed = ''
    to_be_hashed = [to_be_hashed + i for i in args]
    
    hashed_values = hashlib.md5(''.join(to_be_hashed).encode()).hexdigest()

    return hashed_values