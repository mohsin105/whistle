from django.shortcuts import render,redirect,HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sslcommerz_lib import SSLCOMMERZ
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from users.models import Order
from users.serializers import OrderSerializer, OrderCreateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.conf import settings as mainSettings
# Create your views here.


class OrderViewSet(ModelViewSet):
    queryset=Order.objects.prefetch_related('user').all()
    # serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    http_method_names=['get','post','delete','patch','head','options']

    def get_serializer_class(self):
        if self.request.method=='POST':
            return OrderCreateSerializer
        return OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,package_name='Verified Member')
    
    def create(self, request, *args, **kwargs):
        existing_order= Order.objects.filter(user=request.user).first()

        if existing_order:
            print("Order already exisit.s")
            serializer= self.get_serializer(existing_order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        print("New order should be created")
        return super().create(request, *args, **kwargs)

@api_view(['POST'])
def initiate_payment(request):
    user=request.user
    # print(request)
    print(request.data)
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
    post_body['success_url'] = f"{mainSettings.BACKEND_URL}/api/v1/payment/success/"
    post_body['fail_url'] = f"{mainSettings.BACKEND_URL}/api/v1/payment/fail/"
    post_body['cancel_url'] = f"{mainSettings.BACKEND_URL}/api/v1/payment/cancel/"
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
    print(response['GatewayPageURL'])
    # print(response)
    # return Response(response)
    if response.get('status') == 'SUCCESS':
        return Response({'payment_url':response['GatewayPageURL']})
    return Response({"error":"Payment Integration Failed"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def payment_success(request):
    print("success url hit")
    print(request.data)
    order_id= request.data.get('tran_id').split('_')[1]
    print(order_id)
    order=Order.objects.get(id=order_id)
    order.status='ACTIVE'
    order.save()
    return HttpResponseRedirect(f"{mainSettings.FRONTEND_URL}/dashboard/payment/success/")


@api_view(['POST'])
def payment_fail(request):
    print("failed url hit")
    return HttpResponseRedirect(f"{mainSettings.FRONTEND_URL}/dashboard/")

@api_view(['POST'])
def payment_cancel(request):
    print("cancel url hit")
    return HttpResponseRedirect(f"{mainSettings.FRONTEND_URL}/dashboard/")