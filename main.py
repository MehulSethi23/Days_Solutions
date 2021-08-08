import datetime
import calendar

def findDay(strdate):

    currdate=strdate.split("-") #to remove all the "-"
    currdate=currdate[::-1] # change it to DD MM YYYY format from YYYY MM DD

    date=" ".join(currdate) #joining the list to a string

    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() #using the libraries to get the day
    return (calendar.day_name[born])

def solution():
    n=int(input()) #size of input dictionary
    d = dict(input().split() for _ in range(n)) #input the dictionary

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

    new_dict={}
    new_sorted_dict={}

    for key in d:
        day = findDay(key)
        if new_dict.get(day) is None: #to avoid default value error
            new_dict[day]=int(d[key])
        else:
            new_dict[day]+=int(d[key])
    print(new_dict)
    #to get the sorted dictionary
    for i in week_days:
        if(new_dict.get(i) != None):
            new_sorted_dict[i]=new_dict[i]


    # case where week days not present
    i=0
    while i<7:
        if new_sorted_dict.get(week_days[i]) is None:
            prev=new_sorted_dict[week_days[i-1]]
            j=i
            while new_sorted_dict.get(week_days[j]) is None:
                j+=1
            next=new_sorted_dict[week_days[j]]
            undef_days = j-i
            new_val= (next-prev)/(undef_days+1)

            while i<j:
                new_sorted_dict[week_days[i]]=prev+new_val
                prev+=new_val
                i+=1
        else:
            i+=1


    #returning the final dictionary
    final_dict={}
    for i in week_days:
        final_dict[i[:3]]=int(new_sorted_dict[i])

    return final_dict


#calling the main function
print(solution())


