from datetime import date
from datetime import datetime 

class Scheduler:
    def __init__(self,i,name,d,time,description):
        self.i=i
        self.name=name
        self.d=d
        self.time=time
        self.description=description
        
    def add(self,i,name,d,time,description):#enter event details
        obj=Scheduler(i,name,d,time,description)
        ls.append(obj)
        
    def Update(self,d):#check previous date
        flag=1
        t=datetime.now().date()
        x=t.strftime("%m/%d/%Y")
        if(x>d):
            print("You have entered previous date")
            flag=0
            return flag
        else:
            flag=1
            return flag     
                 
    def delete(self,m):#delete event by index
        i=obj.search(m)#first it search the index and then delete record of event index 
        del ls[i]
        
    def search(self,a):#search index for delete operation
        for j in range(ls.__len__()):
            if(ls[j].i==a):
                return j
            
    def datecheck(self,da,t):#for checking date time conflict
        flag=1
        for j in range(ls.__len__()):
            if(ls[j].d==da and ls[j].time==t or (ls[j].d==da and ls[j].time>t)):
                print("Date and Time Conflict")
                flag=0
                return flag
        flag=1
                         
    def display(self,obj):
        print("Index of event: ",obj.i)
        print("Name of event: ",obj.name)
        print("date of event : ",obj.d)
        print("time of event : ",obj.time)
        print("description of event : ",obj.description)
        print("\n")
    
ls=[]
p="1"
while(p!=5):
        p=(input("Enter NUmber : 1. Add Event 2.delete Event by index 3. display Event details 4.exit \n "))
        if p=="1":
            obj=Scheduler(0,"",0,0,"")
            obj.i=int(input("Enter Index starts from 1...: "))
            obj.name=input("Enter name of event : ")
            obj.d=input("Enter date in mm/dd/yyyy format : ")
            
            #validate date format 
            valid=False  
            while not valid:
                try:
                    date = datetime.strptime(obj.d, "%m/%d/%Y").strftime("%m/%d/%Y")
                    valid = True
                except ValueError:
                    print("Incorrect date format, Please enter new date")
                    obj.d=input("Enter date in mm/dd/yyyy format : ")
                    
            #Check date is previous or not
            x=obj.Update(obj.d)     
            while(x==0):
                    print("Entered date is previous date, enter new date")
                    obj.d=input("Enter date in mm/dd/yyyy format : ")
                    x=obj.Update(obj.d)
                            
            obj.time=int(input("Enter time of event: "))
            y=obj.datecheck(obj.d,obj.time)# checking date time conflict   
            while(y==0):
                print("Enter new time because date/time is conflicting")
                obj.time=int(input("Enter time of event: "))
                y=obj.datecheck(obj.d,obj.time)  
            obj.description=input("Enter description of event : ")
            obj.add(obj.i,obj.name,obj.d,obj.time,obj.description)
                
        elif p=="2":#delete event by index
            m=int(input("Enter Index to delete schedule: "))
            obj.delete(m)
            
        elif p=="3":#display all Events
            print("List of Events : \n")
            for j in range(ls.__len__()):
                obj.display(ls[j])  
        else:
            exit()