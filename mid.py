class Star_Cinema:
    __hall_list=[]
    def __init__(self) -> None:
        pass
    
    def entry_hall(self,rows,cols,hall_no):
        hall=Hall(rows,cols,hall_no)
        self.__hall_list.append(hall)
        
    def get_Hall_list(self):
        return self.__hall_list
        
    
    
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.__show_list=[]
        self.seats={}
        
    def __repr__(self) -> str:
        return self.hall_no
        
    def entry_show(self,id,movie_name,time):
        s1=(id,movie_name,time)
        self.__show_list.append(s1)
        
        self.seats[id]=[[0 for i in range(self.cols)] for j in range(self.rows)]
            
            
    def book_seats(self,id,seat_t):
        try:
            if id not in self.seats:
                raise ValueError("Invalid ID")
            if row<1 or row>self.rows or col<1 or col>self.cols:
                raise ValueError("INVALID Seat")
            if self.seats[id][row-1][col-1]!=0:
                raise ValueError("Seat already BOOKED")

        except ValueError as e:
            print(f'Error: {e}')
            return
            
        self.seats[id][row-1][col-1]=1
        print(f'\tseat({row},{col}) booked for show {id}')
            
                
    
    def view_show_list(self):
        for show in self.__show_list:
            print(f'MOVIE NAME:{show[1]}({show[0]}) SHOW ID:{show[0]} {show[2]}')
            
    def view_available_seats(self,id):
        try:
            if id not in self.seats:
               raise ValueError('INVALID SHOW ID')
        except ValueError as e:
            print(f'Error:{e}')
            return
            
        for row in self.seats[id]:
            print(row)
        
        
        
c1=Star_Cinema()
c1.entry_hall(5,5,'101')
c1.entry_hall(8,8,'102')
c1.entry_hall(10,8,'103')

c1.get_Hall_list()[0].entry_show(1,'asd','25/4/2023 7:00PM')
c1.get_Hall_list()[0].entry_show(2,'jawan','26/4/2023 9:00PM')
c1.get_Hall_list()[0].entry_show(3,'spiderman','25/4/2023 11:00AM')
c1.get_Hall_list()[0].entry_show(4,'halua','27/4/2023 8:00PM')


run=True

while run:
    print('''
          1. VIEW ALL SHOW TODAY
          2. VIEW AVAILABLE SEATS
          3. BOOK TICKET
          4. Exit
          ''')
    print('ENTER OPTION:',end='')
    i=int(input())
    if i==1:
        print(c1.get_Hall_list()[0].view_show_list())
    if i==2:
        id=int(input('\tENTER SHOW ID: '))
        c1.get_Hall_list()[0].view_available_seats(id)
    if i==3:
        id=int(input('\tShow Id: '))
        row=int(input('\tEnter Seat Row: '))
        col=int(input('\tEnter Seat Column: '))
        c1.get_Hall_list()[0].book_seats(id,(row,col))
    if i==4:
        break

