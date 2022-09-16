from django.shortcuts import render,redirect
from django.http import HttpResponse
from stripe_api.models import Item
import stripe
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, "index.html")

def info_item(request, id):
    try:
        item = Item.objects.get(id=id)
        data = {"item": item}
        return render(request, "item_info.html", data)
    except ObjectDoesNotExist as e:
        return HttpResponse("Данный объект не существует в БД")
    except Exception as e:
        return HttpResponse(e)
    

    

stripe.api_key = 'sk_test_51Lhw8lJv44QRunnSBix4VHqjJxGeUZkayk6Xf03SHj6GyRNY1e6SybvPPKSf7AjRT4VgyDUDmJEZr8G09WQMzNIW00vfdt4uwE'

def buy_item(request, id):
    item = Item.objects.get(id=id)
    session = stripe.checkout.Session.create(
        line_items=[{
        'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': item.name,
            'description': item.get_description()
            },
            'unit_amount_decimal': item.price * 100,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )

    return redirect(session.url, code=303)
