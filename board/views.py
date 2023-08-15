# def index(request):
#    return render(request, " 'MINI > 해당경로로 바꿔라' .html" ) 
from django.shortcuts import render
from board.models import Board

from django.db import connection
from common.CommonUtil import dictfetchall

# Create your views here.
def list(req):
    type = req.GET.get('type')
    
    cursor = connection.cursor()
    
    if type =='4':
        keyword = 'talk'
    elif type == '3':
        keyword = '구직'
    elif type == '2':
        keyword = '구인'
    else:
        keyword = ''
    
    sql = f"select * from board where board_type like '%{keyword}%'"

    cursor.execute(sql)
    boardList = dictfetchall(cursor)

    return render(req, "board/board.html", {'boardList':boardList})




# def view(req, id):
#     board = Board.objects.get(id=id)

#     return render(req, "board/board_view.html", {'boardItem':board})

