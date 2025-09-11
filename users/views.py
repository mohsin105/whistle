from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sslcommerz_lib import SSLCOMMERZ
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def initiate_payment(request):
    user=request.user
    amount= request.data.get('amount')
    order_id=request.data.get('orderId')
    settings = { 'store_id': 'whist68c2cfd4cd24a', 
                'store_pass': 'whist68c2cfd4cd24a@ssl', 
                'issandbox': True }
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = f"txn_{order_id}"
    post_body['success_url'] = "http://localhost:5173/dashboard/payment/success/"
    post_body['fail_url'] = "http://localhost:5173/dashboard/payment/success/"
    post_body['cancel_url'] = "http://localhost:5173/dashboard/"
    post_body['emi_option'] = 0
    post_body['cus_name'] = f"{user.first_name}"
    post_body['cus_email'] = user.email
    post_body['cus_phone'] = user.phone_number
    post_body['cus_add1'] = user.location
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Premium-subcription"
    post_body['product_category'] = "Social-Media-Service"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) # API response
    print(response)
    # return Response(response)
    if response.get('status') == 'SUCCESS':
        return Response({'payment_url':response['GatewayPageURL']})
    return Response({"error":"Payment Integration Failed"}, status=status.HTTP_400_BAD_REQUEST)