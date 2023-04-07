print("""
     ____         _      ___    
    |    \       /_\    / _  \   (_)   _____
    |  _   \    /|_|\  | |_| |    _   |     |
    | | |   |  | | | | |  _  |   | |  |     |
    | |_|   |  |  _  | | | \ \   | |  |     |
    |______|   |_| |_| |_|  \_|  |_|  |_____| DarioStar999
""")
print("""

     1]print                    3]create a test file             5]Shutdown pc           
            
     2]School averange          4]restart pc                     6]Suspend pc

     7]Create a website         8]Create immage/text             9]coming soon

""")

Select = input("select a mode: ")

if Select == "1":
    F1 = input("type what do you wanna print: ")
    print(F1)

if Select == "2":
    from codes import averange

if Select == "3":
    from codes import Filecreate

if Select == "4": 
    from codes import restart

if Select == "5": 
    from codes import shoutdown

if Select == "6": 
    from codes import suspend

if Select == "7":
    from codes import web

if Select == "8":
    select1 = input("text or immage: ")
    if select1 == "text":
        from codes import text
    if select1 == "immage":
        from codes import immage
        