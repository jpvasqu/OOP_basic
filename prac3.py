# In this Code we use TRY And Except to handle the error
#If the user Input a string or character the system will print Invalid input

try:
    #Inputting the Element that separated by space
    print("Enter elements separated by space:",end="")
    var1=list(map(int,input().split()))

    #Varible to find the element 
    list_var=int(input("Enter in a list:"))

    x=[i for i in var1 if i==list_var] 
    

    print(f"The elemet {list_var} appears {len(var1)} times in the list")
    

except ValueError: 
# https://www.google.com/search?q=value+error+in+python&oq=value+error+in+&aqs=chrome.2.0i512j69i57j0i512l8.9457j0j7&sourceid=chrome&ie=UTF-8
    print("Invalid Input")