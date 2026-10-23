f1 = open(save_file, "w") 

for i in range(3): 
    name = input("Enter the name of the employee: ") 
    f1.write(name) 
    f1.write("\n") 
	
f1.close() 
print("Data is written into the file.")