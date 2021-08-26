email = input("Enter Email\t") 
ind = email.index(".") 
at = email.index("@") 
fname = email[0:ind]
lname = email[ind+1:at] 
domain = email[at+1:] 
print("First Name: ",fname) 
print("Last Name: ",lname) 
print("Host Name: ",domain)
