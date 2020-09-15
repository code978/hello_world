from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from bs4 import BeautifulSoup as BS
import urllib.request as client

# Create your views here.
url = "https://ticker.finology.in/"

response = client.urlopen(url)
res = response.read()
soup = BS(res)
company_list = soup.find_all('a', class_='complink')

def res(request):
    return HttpResponse("<h1>hello World</h1>")

def Company_name(n):
    return company_list[n].get_text()
    
def response(request):

    return JsonResponse([
        {'Company 1':'{}'.format(Company_name(0))},
        {'Company 2':'{}'.format(Company_name(1))},
        {'Company 3':'{}'.format(Company_name(2))},
        {'Company 4':'{}'.format(Company_name(3))},
        {'Company 5':'{}'.format(Company_name(4))},
        {'Company 6':'{}'.format(Company_name(5))},
        {'Company 7':'{}'.format(Company_name(6))},
        {'Company 8':'{}'.format(Company_name(7))},
        {'Company 9':'{}'.format(Company_name(8))},
        {'Company 10':'{}'.format(Company_name(9))},
    ],safe=False)