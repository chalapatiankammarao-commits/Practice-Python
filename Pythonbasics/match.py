#match
day = 5
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")

#default value
day  = 5
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case _:
        print("thursday")

#combine values
day = 4
match day:
    case 1 | 2| 3| 4 | 5:
        print("these days are having match")
    case 6| 7:
        print("these days are having not match")
#add if statement
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("yes this month having match")
    case 4 | 5 | 6 | 7 if month == 5:
        print("this month also having match")
                       
           
            
            
            
        
    