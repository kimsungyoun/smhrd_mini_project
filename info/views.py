from django.shortcuts import render

from django.db import connection 
from common.CommonUtil import dictfetchall

# Create your views here.
def list(request):
    # keyword = request.POST.get('keyword') 
    # if keyword == None:
    #     keyword=""
    location = request.GET.get('location')
    cursor1 = connection.cursor()
    if location == '3':
        keyword ="인천"
    elif location == '1':
        keyword ="경기"
    elif location == '2':
        keyword ="서울"
    elif location == '4':
        keyword ="충청북도"
    elif location == '5':
        keyword ="전라"
    elif location == '6':
        keyword ="충청남도"
    elif location == '7':
        keyword ="제주" 
    elif location == '8':
        keyword ="부산"                        
    else:
        keyword =""

    sql1=f"select * from enterprise WHERE ENT_ADDRESS LIKE '%{keyword}%'"
    cursor1.execute(sql1)
    List1 = dictfetchall(cursor1)

    return render(request, "info/info.html", 
                  {'boardList':List1} )