from django.utils.deprecation import MiddlewareMixin

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print "44444444444444444"

    def process_response(self,request,response):
        print "3333333333333333"
        return response

class  Row2(MiddlewareMixin):
    def process_request(self,request):
        print "22222222222222222222222"

    def process_response(self,request,response):
        print "111111111111111"
        return response
