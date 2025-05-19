nokia = True
while nokia:
 mainMenu = """
 List of menu functions
		press:
		1. Phone_book
		2. Messages
		3. Chat
		4. Call_register
		5. Tones
		6. Settings
		7. Call_divert
		8. Games
		9. Calculator
		10. Reminders
		11. Clock
		12. Profiles
		13. SIM_services
		0. Exit
""";
 print(mainMenu)
 number = int(input('enter a number to select: '))
 match number:
  case 1:
   
    phone_book = """
			PhoneBook
			press;
			1 - Search
			2 - Service Nos.
			3 - Add name
			4 - Erase
			5 - Edit
			6 - Assign tone
			7 - Send b'card
			8 - Options
			9 - Speed dails
			10 - Voice tags
			0 - Back to main menu
""";
 print(phone_book)
 while True: 
  phone_book_selection = int(input('Select Menu: '))
  match phone_book_selection:
   case 1:
     print('search')
     break
   case 2:
     print('Service_Nos')
   case 3:
     print('Add_name')
   case 4:
     print('Erase')
   case 5:
     print('Edit')
   case 6:
     print('Assign_Tone')
   case 7:
     print('Send_b_card')
   case 8:

     options = """
			Options
			press;
			1 - Type of view
			2 - Memory status
			0 - Back to main menu

""";

 print(options)
 while True:
  option_selection = int(input('Selection options: '))
  match option_selection:
   case 1:
     print('Type of view')
   case 2:
     print('Memory status')
   case 0:
     print('Back to phonebook menu')
     break
   case 9:
     print('Speed_dials')
   case 10:
     print('Voice_tags')
   case 0:
     print('Back to main menu')
     
     break
     

   case 2: 

      messageBox = """
			Select mesaage menu
			Press:
			1 -  Write messages
			2 - Inbox
			3 - Outbox
			4 - Picture messages
			5 - Templates
			6 - Smileys
			7 - Message settings
			8 - Info service
			9 - Voice mailbox number
			10 - Service command editor
			0 - Back to main menu
""";
 print(messageBox)
 while True:
  select_message_menu = int(input('Select message menu: '))
  match select_message_menu:
   case 1:
     print('Write message')
   case 2:
     print('Inbox')
   case 3:
     print('Outbox')
   case 4:
     print('Picture messages')
   case 5:
     print('Templates')
   case 6:
     print('Smileys')
   case 7:
     print('Message settings')
   case 8:
     print('Info service')
   case 9:
     print('Picture messages')
   case 10:
     print('Service command editor')
   case 0:
     print('Back to message menu')
     break
   case 3: 
    chat
   case 4:
    Call_register
   case 5:
    Tones
   case 6:
    Settings
   case 7:
    Call_divert
   case 8:
    Games
   case 9:
    Calculator
   case 10:
    Reminders
   case 11:
    Clock
   case 12:
    Profiles
   case 13:
    SIM_services
   case 0:
    print('goodbye')
    break
   case _:
    print('invalid input')

		
 	
			