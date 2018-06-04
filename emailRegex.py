import re

#open the file to be written from, for reading
emailDoc = open(r'')
emailDocContents = emailDoc.read()

#create a regex object for the email address
emailRegexObj = re.compile(r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-z]+')
matchObj = emailRegexObj.findall(emailDocContents)

#append all the email address in the match object to a list
emailList = []
for items in matchObj:
    emailList.append(items)

#write the email addresses to the desired file

#open the destination file for writing
destinationEmailFile = open(r'', 'w')
for items in emailList:
	destinationEmailFile.write(items + '\n')

#close all open files
emailDoc.close()
destinationEmailFile.close()

#report success
print("copy has been concluded")   

#separate the addresses by domain
sepAdd = open(r'')
sepAddContent = sepAdd.readlines()

gmailAdd = open(r'', 'w')
yahooAdd = open(r'', 'w')
otherAdd = open(r'', 'w')

for i in range(len(sepAddContent)):
    if "gmail" in sepAddContent[i]:
        gmailAdd.write(sepAddContent[i])
    elif "yahoo" in sepAddContent[i]:
        yahooAdd.write(sepAddContent[i])
    else:
        otherAdd.write(sepAddContent[i])
                    
                    

gmailAdd.close()
otherAdd.close()
yahooAdd.close()    
sepAdd.close()

print("all operation complete")
               
    


