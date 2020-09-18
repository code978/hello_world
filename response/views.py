from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from bs4 import BeautifulSoup as BS
import urllib.request as client

url = "https://ticker.finology.in/"

response = client.urlopen(url)
res = response.read()
soup = BS(res)
company_list = soup.find_all('a', class_='complink')

def Company_name(n):
    return company_list[n].get_text()

def get_href(n):
    href = company_list[n].get('href')
    return href

def get_html(n):
    response = client.urlopen(url+get_href(n))
    res = response.read()
    soup = BS(res)
    return soup

def High_price(soup,n):
    price_summary = soup.find(id="mainContent_ltrlTodayHigh").get_text()
    return price_summary

def low_price(soup,n):
    price_summary = soup.find(id="mainContent_ltrlTodayLow").get_text()
    return price_summary

def week_52_high(soup,n):
    price_summary = soup.find(id="mainContent_ltrl52WH").get_text()
    return price_summary

def week_52_low(soup,n):
    price_summary = soup.find(id="mainContent_ltrl52WL").get_text()
    return price_summary

def find_company_number(pk):
    index = 0
    for i in range(len(company_list)):
        if pk == Company_name(i):
            index = i
    return index

def Share_holding_pattern(soup,index):
    price_summary = soup.find(id="Share-chart-area").get_text()
    return price_summary

def response(request,pk):

    index = find_company_number(pk)

    soup = get_html(index)

    if index:
    
        return JsonResponse([
        {
            'Company':'{}'.format(pk),
            'details':{
                "price_summary":{
                    'High_price':High_price(soup,index),
                    "low_price":low_price(soup,index),
                    "52_Week_High":week_52_high(soup,index),
                    "52_Week_Low":week_52_low(soup,index),
                },
                "Company_details":{
                    "Market_cap":{},
                    "Enterprice_value":{},
                    "No. of Shares":{},
                    "P/E":{},
                    "P/B":{},
                    "Face_value":{},
                    "div_Yeild":{},
                    "Book_value_(TTM)":{},
                    "Cash":{},
                    "Debt":{},
                    "promoter_holding":{},
                    "Eps(TTM)":{},
                    "Sales_growth":{},
                    "Roe":{},
                    "Roce":{},
                    "profit_growth":{},
                },
                "FinStart":{

                },
                "Charts":{

                },
                "Peers":{

                },       
                "Share_holding_pattern":{

                },
                "Quaterly(all figures in cr.)":{
                    "particulars":{
                        "net_sales":{},
                        "Total_expenditue":{},
                        "operating_profit":{},
                        "other_income":{},
                        "interest":{},
                        "Deprection":{},
                        "Exceptional_itmes":{},
                        "profit_before_tax":{},
                        "tax":{},
                        "profit_after_tax":{},
                        "Adjusted_Eps(rs)":{},
                    },
                },
                "Profit_&_Loss":{
                    "particulars":{
                        "net_sales":{},
                        "Total_expenditue":{},
                        "operating_profit":{},
                        "other_income":{},
                        "interest":{},
                        "Deprection":{},
                        "Exceptional_itmes":{},
                        "profit_before_tax":{},
                        "tax":{},
                        "profit_after_tax":{},
                        "Adjusted_Eps(rs)":{},
                    },
                },
                "Balance_Sheet":{
                    "Equity":{
                        "Share_Capital":{},
                        'Total_reservers':{},
                        'borrowings':{},
                        'other n/c liabilites':{},
                        'current_liabilites':{},
                        'total_liabailtes':{},
                        },
                    "Assets":{
                            "net_block":{},
                            'capital_wip':{},
                            'investment':{},
                            'loan&advances':{},
                            'other n/c assets':{},
                            'current_assets':{},
                            'total_assests':{},
                        },
                    },
                "Cash_flows":{
                    "profit_before_tax":{},
                    "adjustment":{},
                    'Working_capital_changes':{},
                    'tax_paid':{},
                    'operating_cash_flow':{},
                    'investing_cash_flow':{},
                    'financing_cash_flow':{},
                    'net_cash_flow':{},
                },
            
            },
         },

    ],safe=False)

    else:
        return JsonResponse([{"error":"Company not found"},],safe=False)