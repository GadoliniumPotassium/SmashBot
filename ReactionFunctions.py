import SheetsController

document=SheetsController.getSheet()
def win_loss(me,split_command):
    #find discord ID in spreadsheet
    #go to win column, get the data and add plus one
    #go to the other person mentioned and go to their loss sheet and add one to their loss sheet
    #time to define args 
    #me is the sender
    Foundhim=False
    Foundme=False
    rowMe=0
    colMe=0
    rowHim=0
    colHim=0
    max_cols=len(document.col_values(1))
    split_command[3]=split_command[3][2:-1]
    print("----------")
    print (me)
    print (split_command[3])
    
    print("-------------")
    print("commencing first loop")
    for i in range(max_cols+1):
        if(i>1):
            print("searching for calling user")
            if(str(document.cell(i,2).value)==str(me)):
                print("Found the calling user")
                Foundhim=True
                rowMe=i
                colMe=1
            print("searching for opponent")
            print(document.cell(i,2).value)
            if(str(document.cell(i,2).value)==str(split_command[3])):
                print("Found the opponent")
                Foundme=True
                rowHim=i
                colHim=1

    if(Foundhim and Foundme):
        print("Both people were found")
        #cell update begins here
        if(split_command[1].lower()=="win"):
            print("updating in win")
            document.update_cell(rowMe,colMe+2,str(int(document.cell(rowMe,colMe+2).value)+1))
            document.update_cell(rowHim,colHim+3 ,str(int(document.cell(rowHim,colHim+3).value)+1))
            return "Data has been updated, check record to see your current record"
        elif(split_command[1].lower()=="loss"):
            print("updating in loss")
            document.update_cell(rowMe,colMe+3,str(int(document.cell(rowMe,colMe+3).value)+1))
            document.update_cell(rowHim,colHim+2,str(int(document.cell(rowHim,colHim+2).value)+1))
            return "Data has been updated, check record to see your current record"
        else:
            print ("Something wrong")
            return "Something wrong"
    else:
        return "One of you two is not there, make sure you're in the league."
        




def rankList(args):
    #Will sort through all the players and print them
    # in order of highest to lowest Win/Loss Ratio
    stat_list={}
    max_cols=len(document.col_values(1))
    for i in range(max_cols+1):
        if(i>1):
            #We are getting the username 
            stat_list[str(document.cell(i,1).value)]=document.cell(i,5).value
    a=sorted(stat_list, key=stat_list.get)
    a.reverse()
    pos=1
    final_str="Rankings:\n"
    for i in a:
        final_str += str(pos)+" -> "+str(i)+" : "+str(stat_list[i])+"\n"
        #When we find your position, we will append that message to the beginning of the list and say something
        #of the like, we found you at position number x. 
        if(i == args[0]):
            final_str="You were found at position number "+str(pos)+"\n" + final_str
        pos+=1
    
    return final_str

def displayRecord(args):
    #Will display the record of the calling person
    #Will go in by his ID and print out his
    #win loss record as well as his W/L ratio
    str_result=""
    isThere=False
    row=0
    col=0
    max_cols=len(document.col_values(1))
    for i in range(max_cols+1):
        if(i>=2):
            if(args[0]==document.cell(i,1).value):
                row=i
                col=1
                isThere=True
    for i in range(max_cols+1):
        if(i>=2):
            if(args[0]==document.cell(i,2).value):
                row=i
                col=2
                isThere=True
                    
    if isThere:
        if(col==2):
            str_result="The record of " + document.cell(row,col-1).value+ " is " + document.cell(row,3).value+ " wins and " + document.cell(row, 4).value+" losses for a Win-Loss ratio of "+ document.cell(row,5).value
        if(col==1):
            str_result="The record of "+document.cell(row,col).value+" is "+ document.cell(row,3).value+" wins and " + document.cell(row, 4).value+" losses for a Win-Loss ratio of "+ document.cell(row,5).value
        return str_result
    else:
        return "One of the two players are not there"

def joinLeague(args):
    #will check to see if user is already in database
    #if he is, then return false and go home
    #if he isn't go to the bottom of the list and create a new cell for him.
    row_where_to_add=len(document.col_values(1)) + 1
    column = len(document.row_values(1))
    try:
        document.find(args[0])
        return "Player already exists in the league, cannot join again"
    except Exception as e:
          #args 0 is the username
        document.update_cell(row_where_to_add, 1, str(args[0]))
        #args 1 is the user id
        document.update_cell(row_where_to_add, 2, str(args[1]))
        document.update_cell(row_where_to_add, 3,0)
        document.update_cell(row_where_to_add, 4,0)
        document.update_cell(row_where_to_add, 5, str('=IF(D' + str(row_where_to_add) + '=0, "Perfect Run", C' + str(row_where_to_add)+ "/" + "D"+ str(row_where_to_add) + ")"))
        return str(args[0]) + " has joined the league"

def listLeagueMembers():
     max_cols=len(document.col_values(1))
     final_str="Here are the current members of the league:\n"
     for i in range(max_cols+1):
         if(i>1):
             final_str+=(str(document.cell(i,1).value)+"\n")
     return final_str

def listCommands():
    return "command_list = Here are the following commands:\n!falcon: {\nrank\nmembers\njoin\n'win vs @member'\n'loss vs @member'\nrecord\n}"

