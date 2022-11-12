#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ipl = []
class TEAM:
    def __init__(self,name,points,last5):
        self.name = name
        self.points = points
        self.last5 = last5
    
    def get_last5(self):
        return self.last5
    
    def get_points(self):
        return self.points
    
    def add_team(self,team,points,last5):
        team = TEAM(team,points,last5)
        ipl.append(team)
        
        
    def show_data(self):
        print ("{:<8} {:<10} {:<10}".format( self.name, self.points, self.last5))
    
    
   

print()
def cons_loss(loss,result):
    res = []
    for i in range(len(ipl)):
        s = ipl[i].get_last5()
        count = 0
        conloss = 0
        for j in range(len(s)):
            if(s[j]==result):
                count += 1
                conloss = max(conloss,count)
            else:
                count = 0
        if(conloss==loss):
            res.append(ipl[i])
    return res

def queries():
    try:
        n = int(input("""Enter 1 for points table.
Enter 2 to search consecutive win/loss teams
Enter any other digit to exit."""))

        if n==1:
            print ("{:<12} {:<10} {:<10}".format("Team","Pts","Last 5"))
            for i in range(len(ipl)):
               print("{:<4}".format(i+1),end="") 
               ipl[i].show_data()
            queries()
        elif n==2:
            num = int(input("Enter the consective win/loss you are looking for?"))
            result = input("Type W for win or L for lose.")
            res = cons_loss(num, result)
            
            sum_points = 0
            for i in range(len(res)):
                    res[i].show_data()
                    sum_points += res[i].get_points()
            
            if len(res)!=0:
                print("Avg :  ",sum_points/len(res)) 
            
            queries()
    except ValueError as e:
        print("\n\nInvlaid Input, Try again")
        queries()
        
    print()

def main():
    team = TEAM("",0,"")
    team.add_team("GT",20,"WWLLW")
    team.add_team("LSG",18, "WLLWW")
    team.add_team("RR",16,"WLWLL")
    team.add_team("DC",14,"WWLWL")
    team.add_team("RCB",14,"LWWLL")
    team.add_team("KKR",12,"LWWLW")
    team.add_team("PBKS",12,"LWLWL")
    team.add_team("SRH",12,"WLLLL")
    team.add_team("CSK",8,"LLWLW")
    team.add_team("MI",6,"LWLWW")
    
    res = cons_loss(2,"L")
    print("List of teams who lost 2 matches consecutivily.")
    sum_points = 0
    for i in range(len(res)):
            res[i].show_data()
            sum_points += res[i].get_points()
    
    print("Avg  :  " , sum_points/len(res))
    
    queries()
    
main()


# In[ ]:





# In[ ]:




