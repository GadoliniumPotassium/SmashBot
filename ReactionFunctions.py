import SheetsController

document=SheetsController.getSheet()


def win_loss(message,client,args):
    #find discord ID in spreadsheet
    #go to win column, get the data and add plus one
    #go to the other person mentioned and go to their loss sheet and add one to their loss sheet
    #time to define args 
    #args[0] is the sender
    
    message_split=message.split(" ")
    message_split[2]=message_split[2][3:-1]
    OPcell=document.find(message_split[2])
    UserCell=document.find(args[0])
    if(message_split[0].lower="win"):
        document.update_cell(UserCell.row,UserCell.col+2,int(UserCell.value)+1)
        document.update_cell(OPcell.row,OPcell.col+2,int(OPcell.value)+1)
        return True
    elif(args[1] == "loss"):
        document.update_cell(UserCell.row,UserCell.col+3,int(UserCell.value)+1)
        document.update_cell(OPcell.row,OPcell.col+1,int(OPcell.value)+1)
        return True
    return 0==0

def rankList(message,client,args):
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

def displayRecord(message,client,args):
    #Will display the record of the calling person
    #Will go in by his user ID or username and print out his
    #win loss record as well as his W/L ratio
    str_result=""
    max_cols=len(document.col_values(1))
    for i in range(max_cols+1):
        if(i>1):
            #We are getting the username
            if(document.cell(i,1).value == args[0]):
                str_result="The record of "+str(args[0])+" record is "+ str(document.cell(i,3).value) +" wins and " + str(document.cell(i,3).value) +" losses and he has a Win-Loss ratio of "+ str(document.cell(i,4).value) +"."
            
    return str_result

def joinLeague(message,client,args):
    #will check to see if user is already in database
    #if he is, then return false and go home
    #if he isn't go to the bottom of the list and create a new cell for him.
    row_where_to_add=len(document.col_values(1)) + 1
    column = len(document.row_values(1))
    #args 0 is the username
    document.update_cell(row_where_to_add, 1, args[0])
    #args 1 is the user id
    document.update_cell(row_where_to_add, 2, args[1])
    document.update_cell(row_where_to_add, 3,0)
    document.update_cell(row_where_to_add, 4,0)
    document.update_cell(row_where_to_add, 5,'=IF(D7=0,"Perfect Run",C7/D7)')
    
    return True

def listLeagueMembers(message,client,args):
     max_cols=len(document.col_values(1))
     final_str="Here are the current members of the league:\n"
     for i in range(max_cols+1):
         if(i>1):
             final_str+=(str(document.cell(i,1).value)+"\n")
     return final_str