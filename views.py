from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from checksum import *
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
import os
from os.path import abspath, dirname

def index(request):
	return render(request, 'merchant.html')
def posttozaakpay(request):
	if request.method == 'POST':
                post_data = {}
		data = request.POST
		for x in data:
			post_data[x] = data[x]
        checksum = Checksum(post_data)
	alldata = checksum.getAllParams()
	chcksum = checksum.calculateChecksum(secret, alldata)
	a = checksum.outputForm(chcksum)
	html_template = open(os.getcwd() + '/zaakpay/templates/posttozaakpay.html').read()
	output = html_template % a
	return HttpResponse(output)
@csrf_exempt
def response(request):
    	if request.method =='POST':
		post_data2 = {}
		data2 = request.POST
		for x in data2:
			post_data2[x] = data2[x]
	recvd_checksum = data2['checksum']
	oid = data2['orderId']
	resc = data2['responseCode']
	resd = data2['responseDescription']
	amount = data2['amount']
	paymet = data2['paymentMethod']
	cardhid = data2['cardhashid']
	alldata1 = "'"+oid+"''"+resc+"''"+resd+"''"+amount+"''"+paymet+"''"+cardhid+"'" 
	print alldata1
	checksum2 = Checksum(post_data2)
	alldata2 = checksum2.getAllParams()
	checksum_cal = checksum2.calculateChecksum(secret, alldata1)
	checksum_check = checksum2.verifyChecksum(recvd_checksum, alldata1, secret)
	a2 = checksum2.outputResponse(checksum_check)
	html_template2 = open(os.getcwd() +  '/zaakpay//templates/response.html').read()
        output2 = html_template2 % a2
	return HttpResponse(output2)

