 # Diamond shape 
def Diamond(rows): 
    q = 1
    for i in range(1, rows + 1): 
        # loop to print spaces 
        for j in range (1, (rows - i) + 1): 
            print(end = " ") 
          
        # loop to print star 
        while q != (i+1): 
            print("*", end = " ") 
            q = q + 1
        q = 1
          
        # line break 
        print() 
  
    s = 0
    q  = 0
    for i in range(1, rows + 1): 
        # loop to print spaces 
        for j in range (1, s + 1): 
            print(end = " ") 
        s = s + 1
          
        # loop to print star 
        while q <= (rows - i): 
            print("*", end = " ") 
            q = q + 1
        q = 0
        print()

rows = 8
Diamond(rows)       
  

