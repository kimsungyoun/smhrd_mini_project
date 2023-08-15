import math


# cursor의 description에 각 필드 이름 정보 - 배열
# columns ['id', 'title', 'contents', 'writer']
def dictfetchall(cursor):
    columns = [col[0].lower() for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# << < 1 2 3 4 5 6 7 8 9 10 > >>
# << : 첫 페이지로
# <  : 이전 페이지로 이동(현재 페이지에서 이전 페이지가 있는지 확인)
# >  : 다음 페이지로 이동(현재 페이지에서 다음 페이지가 있는지 확인)
# >> : 마지막 페이지로
class CommonPage:
    # 페이징에 필요한 3가지 정보
    # totalCnt : 전체 데이터 개수
    # pageSize : 한 페이지에 표시할 데이터 개수
    # curPage  :  현재 페이지 위치
    # 전체 페이지 개수 = ceil(totalCnt / pageSize)
    # ex) 232/10 = 23.2 -> 24 페이지(올림)
    def __init__(self, totalCnt = 1 ,curPage = 0, pageSize = 10):
        self.totalCnt = totalCnt
        self.curPage = curPage
        self.totalPage = math.ceil(totalCnt/pageSize)-1
        # 그룹시작
        self.start = (self.curPage // pageSize) * 10
        self.end = self.start + 10
        
        if self.end > self.totalPage:
            self.end = self.totalPage+1

        # 앞으로 이동
        if self.curPage >= 1 : 
            self.isPrev = True
            self.prev_page = self.curPage - 1
        else:
            # 더 이상 못감
            self.isPrev = False
            self.prev_page = self.curPage = 0

        # 뒤로 이동
        if self.curPage < self.totalPage:
            self.isNext = True
            self.next_page = self.curPage+1
        else:
            self.isNext = False
            self.next_page = self.curPage

        self.page_range = range(self.start, self.end)