# rent room problem in python------------------------------------------
rent_room = int(input("enter rent for your room: "))
food = int(input("enter food bill: "))
elec_bill = int(input("enter electric bill: "))
persons = int(input("enter total person: "))
total= rent_room+food+elec_bill
rent_per_person = total/persons
print("bill of each person is: ", rent_per_person)



# Scissor, paper, rock game in python----------------------------------
import random
item_list = ["Rock", "Paper", "Scissor"]
user_ch = input("enter your choice from (Rock, Paper, Scissor) -> ")
comp_ch = random.choice(item_list)
print(f"user_choice is-> {user_ch}, computer_choice is-> {comp_ch}")
if(user_ch==comp_ch):
    print("Both are same, so match is tie . . .")
elif(user_ch=="Rock"):
    if(comp_ch=="Paper"):
        print("Paper win in this game . . .")
    elif(comp_ch=="Scissor"):
        print("Rock is win in this game . . .")
elif(user_ch=="Paper"):
    if(comp_ch=="Rock"):
        print("Paper win in this game . . .")
    elif(comp_ch=="Scissor"):
        print("Scissor is win in this game . . .")
elif(user_ch=="Scissor"):
    if(comp_ch=="Paper"):
        print("Seissor win in this game . . .")
    elif(comp_ch=="Rock"):
        print("Rock is win in this game . . .")



import qrcode
upi_id = input("enter your upi id-> ")
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
# phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonepe_qr= qrcode.make(phonepe_url)
googlepe_qr= qrcode.make(googlepe_url)

phonepe_qr.save('phonepe_qr.png')
googlepe_qr.save('googlepe_qr.png')

phonepe_qr.show()
googlepe_qr.show()