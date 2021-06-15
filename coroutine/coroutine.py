# -----------------------------------------------------------
#Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
#@author cafedevn
#Contact: cafedevn@gmail.com
#Fanpage: https://www.facebook.com/cafedevn
#Instagram: https://instagram.com/cafedevn
#Twitter: https://twitter.com/CafedeVn
#Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
# -----------------------------------------------------------


# Python3 program for demonstrating  
# coroutine execution 
  
def print_name(prefix): 
    print("Searching prefix:{}".format(prefix)) 
    while True: 
        name = (yield) 
        if prefix in name: 
            print(name) 
  
# calling coroutine, nothing will happen 
corou = print_name("Dear") 
  
# This will start execution of coroutine and  
# Prints first line "Searchig prefix..." 
# and advance execution to the first yield expression 
corou.__next__() 
  
# sending inputs 
corou.send("Atul") 
# corou.send("Dear Gnut")
# corou.send("Dear Atul") 