while (True) :
    total = 0
    deleted = 0
    
    product_id = {
        1 :{
            "Product name"                : "apple",
            "kilos available"             :  70 ,
            "cost per kilo"               :  40
        
        },
        2 :{
            "Product name"                : "banana",
            "kilos available"             :  90 ,
            "cost per kilo"               :  20 
        },
        3 :{
            "Product name"                : "orange",
            "kilos available"             :  80 ,             
            "cost per kilo"               :  10 
        },
        4 :{
            "Product name"                : "tomatoes",
            "kilos available"             :  100 ,
            "cost per kilo"               :  10 
        },
        5 :{
            "Product name"                : "Cucumber",
            "kilos available"             :  100 ,
            "cost per kilo"               :  7 
        },
        6 :{
            "Product name"                : "Onions",
            "kilos available"             :  50 ,
            "cost per kilo"               :  5 
        }
        

    }
    
    
                                        
    print("\n")
    print("<<<<<<<< Welcome To ITI Store >>>>>>>>")
    print("\n")
    print("Select Mode : \n         -For Customer Press 1 \n         -For Owner Press 2 \n         -To Exit Press 0 ")
    mode = int(input("          Enter Your Mode = "))
    print("-"*50)


    if mode == 1 :
        back_1 = 1 
        back_2 = 1
        while(back_1!=0 or back_2!=0):
            print("Hello Customer....")
            print("         -To show our products press 1      \n         -To Buy from our products press 2   \n         -To print the bill press 3   \n         -To Exit press 0")
            choice = int(input("          Enter Your choice = "))
            print("-"*50)
            if choice == 1 :
                print("                                     Menu of Our Products     ")
                print("                                     --------------------")
                n = range(1,len(product_id)+1,1)
                for i in n:
                    print(product_id[i])
       
        
            elif choice == 2 :
                flag = 1 
                while(flag !=0) : 
                    buy_pro = input("Product name you Want to buy  : ")
                    buy_qua = int(input("Please Enter The Number of kilos = "))
                    n = range(1,len(product_id)+1,1)
        
                    
                    for i in n:
                        if buy_pro == product_id[i]["Product name"] :
                            product_id[i]["kilos available"]-=buy_qua
                        #print(product_id[i]["kilos available"])
                            brk = int(input("You want More ? "))
                            total += buy_qua*product_id[i]["cost per kilo"]
                        #print(total)
                            if (brk == 0):
                                flag = 0
                            break
                
                    bill = total    
                    
                 

             
                
            elif choice == 3 : 
                print("********************************************************")
                print("                Your bill = %f"%(bill))
                print("|                                                        |")

                print("********************************************************")
            elif choice == 0 : 
                break
            print("-"*100)    

            
           
 


    if(mode == 2):
        correct_user = "hader"
        correct_pass = "12345"
        back_1 = 1 
        back_2 = 1
        user_name = input("UserName : ")
        password = input("Password : ")
        if((user_name == correct_user) and (password == correct_pass)):
            while(back_1!=0 or back_2!=0):
                print("         -Add new products press 1      \n         -show products press 2   \n         -change cost press 3   \n         -remove product press 4 \n         -Exit press 0   ")
                choice = int(input("          Enter Your choice = "))
                if choice == 1 : 
                    pro_name = input("Enter Product name : ")
                    num_killos = int(input("Enter kilos available "))
                    cost_kilo = int(input("Enter cost per kilo  "))
                    product_new = {"Product name"                : pro_name,
                                   "kilos available"   :  num_killos ,
                                   "cost per kilo"               :  cost_kilo }
                    product_id[len(product_id)+1] = product_new               
                
                
                elif choice == 2 : 
                    print("                                     Menu of Our Products     ")
                    print("                                     --------------------")
                
                    print(product_id)
                            
                    
                    
                    print("-"*100)    

                
                elif choice == 3 : 
                    
                    pr_nme = input("Product name you Want to change cost : ")
                    cost_chg = int(input("Enter New Cost : "))
                    x = range(1,len(product_id)+1,1)
                    for j in x:
                        if pr_nme == product_id[j]["Product name"] :
                            product_id[j]["cost per kilo"] = cost_chg
                                
                            break
                            
                elif choice ==4 :
                    pr_nme = input("Product name you Want remove from list : ")
                    x = range(1,len(product_id)+1,1)
                    for j in x:
                        if pr_nme == product_id[j]["Product name"] :
                            del product_id[j]
                            
                            deleted = j 
                            
                           
                            break
                    
                 
                elif choice == 0 : 
                    break            
                            
                           
                    

                
            
        
        else:
            print("UserName or Password incorrect try again..")
    
    if(mode == 0) :
        break