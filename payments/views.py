import stripe
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from rest_framework.decorators import api_view
from .serializers import CheckoutSerializer

class SuccessView(TemplateView):
    template_name = 'success.html'

class CancelledView(TemplateView):
    template_name = 'cancelled.html'

stripe.api_key = 'sk_test_51NDXroL8ppG2YRbNq79ejoGYPmhrHoMLXuMcvnKd0UaK9qCIZP1HF0wSaYHe5YilcLYH8FzgmshV0EQ05UGVjyql00l7c4PW2L'
@api_view(['POST'])
def test_payment(request):
    serializer = CheckoutSerializer(data=request.data)
    serializer.is_valid()
    YOUR_DOMAIN = "http://127.0.0.1:8000/payments"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': serializer.data['price'] * 100,
                    'product_data': {
                        'name': serializer.data['name'],
                    },
                },
                'quantity': serializer.data['quantity'],
            },
        ],
        metadata={
            
        },
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/cancel/',
    )
    return JsonResponse({
                'checkout_session': checkout_session.url
            })
