from datetime import datetime

class Member :
    author = 0
    index = 0
    name= []
    email= []
    pw = []
    profile = []
    friends = []
    writes =[]
    
    def __init__(self) :
        super().__init__()

    def create_member(self) :
        print('회원가입을 위한 회원정보를 입력해주세요.')
        print('-------------------------------------------------------')
        print('이름:', end=' ')
        self.name.append(input())
        print('이메일:', end=' ')
        self.email.append(input())
        print('비밀번호:', end=' ')
        self.pw.append(input())
        print('프로필설명:', end=' ')
        self.profile.append(input())
        print('-------------------------------------------------------')
        print(self.name[self.index]+'님의 가입을 환영합니다. 회원가입이 완료되었습니다.')
        print('-------------------------------------------------------\n')

        print('----------------------가입된 정보----------------------')
        print('이름: '+self.name[self.index])
        print('이메일: '+self.email[self.index])
        print('프로필 설명: '+self.profile[self.index])
        print('-------------------------------------------------------\n\n')
        self.friends.append([])
        self.writes.append([])
        self.index+=1
        
    def update_member_info(self) :
        print('회원정보수정을 위해 다시 정보를 입력해주세요')
        print('-------------------------------------------------------')
        print('이름:', end=' ')
        self.name[self.author]=input()
        print('이메일:', end=' ')
        self.email[self.author]=input()
        print('비밀번호:', end=' ')
        self.pw[self.author]=input()
        print('프로필설명:', end=' ')
        self.profile[self.author]=input()
        print('-------------------------------------------------------')
        print('회원정보가 수정되었습니다.')
        print('-------------------------------------------------------\n\n')
    
    def remove_member(self) :
        print('탈퇴하면 복구가 불가능합니다. 정말 탈퇴하시겠습니까? [y/n]:', end=' ')
        check = input()
        print('\n\n')
        if check=='y' :
            del self.name[self.author]
            del self.email[self.author]
            del self.pw[self.author]
            del self.profile[self.author]
            del self.friends[self.author]
            del self.writes[self.author]
            self.index-=1
            return True
        else : return False
        
    def show_member_info(self) :
        print('보안상의 이유로 모든 정보를 열람하실 수는 없습니다.')
        print('이름/이메일/프로필 설명만 확인 가능합니다\n')
              
        print('----------------------가입된 정보----------------------')
        for i in range(self.index) :
            print('이름: '+self.name[i])
            print('이메일: '+self.email[i])
            print('프로필 설명: '+self.profile[i])
            print('-------------------------------------------------------\n\n')
    
    def login(self) :
        check = True
        time = 0
        logged = False

        while(check) :
            if time==3 :
                print('로그인 시도를 3회 실패하셨습니다.\n\n')
                return False, 'a'
            
            print('대소문자 구분이 안되니 주의하여 입력해주세요.\n')
            print('-------------------------Login-------------------------')
            print('ID(email):', end=' ')
            input_id = input()
            print('비밀번호:', end=' ')
            input_pw = input()
            print('-------------------------------------------------------\n\n')
            

            for i in range (self.index) :
                if input_id==self.email[i] and input_pw==self.pw[i] :
                    self.author = i
                    print('\n\nLogin success')
                    print('환영합니다. '+self.name[self.author]+'님\n\n')
                    check = False
                    logged = True
                    return True, self.name[self.author]
            if check : print('\n\nLogin fail\n\n')
            time += 1
            
        return logged, self.name[self.author]

    def exit(self) :
        print('\n-------------------------------------------------------')
        print('-------------------------종료--------------------------')
        print('-------------------------------------------------------\n\n')

class Timeline :
    index = 0
    user = ''
    writer = []
    time = []
    num = []
    writing = []
    tag = []
    like = []
    comment = []

    def set_user(self, user) :
        self.user = user
    
    def input_timeline(self) :
        print('--------------------타임라인 글 게시-------------------')
        print('고유번호:', end=' ')
        Num = int(input())

        same = Num in self.num
        while(same) :
            print('이미 존재하는 고유번호입니다. 다시 입력해주세요.')
            print('고유번호:', end=' ')
            Num = int(input())
            same = Num in self.num
            
        self.num.append(Num)
        print('게시글:', end=' ')
        self.writing.append(input())
        print('태그항목:', end=' ')
        self.tag.append(input())
        print('-------------------------------------------------------\n')
        print('타임라인 글 작성이 완료되었습니다.\n\n')
        self.index += 1
        self.time.append(self.get_time())
        self.writer.append(self.user)
        self.like.append([])
        self.comment.append([])

    def get_time(self) :
        now = datetime.now()
        month = '0'+str(now.month) if int(str(now.month))<10 else str(now.month)
        day = '0'+str(now.day) if int(str(now.day))<10 else str(now.day)
        hour = '0'+str(now.hour) if int(str(now.hour))<10 else str(now.hour)
        minute = '0'+str(now.minute) if int(str(now.minute))<10 else str(now.minute)
        second = '0'+str(now.second) if int(str(now.second))<10 else str(now.second)

        return str(now.year)+'/'+month+'/'+day+' '+hour+':'+minute+':'+second

    def remove_timeline(self) :
        print('삭제하시면 돌이킬 수 없습니다. 삭제하시겠습니까? [y/n]', end=' ')
        YN = input()

        if(YN=='y') :
            print('\n\n삭제하고 싶은 게시물의 고유번호를 입력해주세요.')
            print('(단, 본인의 게시물만 삭제 가능합니다. 가입인사 글은 삭제할 수 없습니다.):', end=' ')
            idx = int(input())
            for i in range(self.index) :
                if idx==self.num[i] and self.writer[i]==self.user :
                    del self.writer[i]
                    del self.time[i]
                    del self.num[i]
                    del self.writing[i]
                    del self.tag[i]
                    del self.like[i]
                    del self.comment[i]
                    self.index -= 1

    def add_like_response(self) :
        print('좋아요 누를 게시글의 고유번호를 입력하세요:', end=' ')
        Num = int(input())

        for i in range(self.index) :
            if self.num[i]==Num :
                if self.user in self.like[i] :
                    print('이미 좋아요를 누르셨습니다.\n\n')
                else :
                    print(self.writer[i]+': 좋아해주셔서 감사해요!\n\n')
                    self.like[i].append(self.user)
                break


    def input_message(self) :
        print('댓글을 작성할 게시글의 고유번호를 입력하세요:', end=' ')
        Num = int(input())
        print('댓글 입력', end=' ')
        Comment = input()
        for i in range(self.index) :
            if self.num[i]==Num :
                print(self.writer[i]+': 댓글 감사합니다!')
                self.comment[i].append(self.user+': '+Comment)
                break


    def show_timeline(self) :
        print('-----------------타임라인 글 목록----------------------')
        for i in range(self.index) :
            print('고유번호: '+str(self.num[i]))
            print('작성자: '+self.writer[i])
            print('게시시간: '+self.time[i])
            print('게시글: '+self.writing[i])
            print('태그항목: '+self.tag[i])
            print('\n❤좋아요 수: '+str(len(self.like[i])))
            print('|댓글|')
            for comment in self.comment[i] :
                print(comment)
            print('-------------------------------------------------------\n') 
        print('-------------------------------------------------------\n\n')
    

def main() :
    m = Member()
    t = Timeline()
    logged = False
    user = ''
    
    while(True) :

        if(logged) :
            t.show_timeline()
            t.set_user(user)
            menu = menuPage()
            
            if menu==1 :
                t.input_timeline()
            elif menu==2 :
                t.add_like_response()
            elif menu==3 :
                t.input_message()
            elif menu==4 :
                t.remove_timeline()
            elif menu==5 :
                m.update_member_infNSo()
            elif menu==6 :
                m.show_member_info()
            elif menu==7 :
                if m.remove_member() : logged=False
            elif menu==8 :
                logged = False
            else :
                print('잘못누르셨습니다. 다시 선택해주세요.\n\n')

        else :
            menu = mainPage()

            if menu==1 :
                logged, user = m.login()
            elif menu==2 :
                m.create_member()
            elif menu==3 :
                m.exit()
                break
            else :
                print('잘못누르셨습니다. 다시 선택해주세요.\n\n')
        
    
def mainPage() :
    print('------------------------메인화면-----------------------')
    print('(1)                      로그인')
    print('(2)                     회원가입')
    print('(3)                       종료')
    print('-------------------------------------------------------\n')
    print('메뉴 선택:', end=' ')
    menu = int(input())
    print('\n\n')
    return menu

def menuPage() :
    print('------------------------내 메뉴------------------------')
    print('(1). 타임라인 게시')
    print('(2). 좋아요 누르기')
    print('(3). 댓글 작성')
    print('(4). 타임라인 글 삭제')
    print('(5). 회원정보수정')
    print('(6). 다른 회원 정보 열람')
    print('(7). 회원탈퇴')
    print('(8). 로그아웃')
    print('-------------------------------------------------------\n')
    print('메뉴 선택:', end=' ')
    return int(input())
    
main()
