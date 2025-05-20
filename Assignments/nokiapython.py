
mainMenu = """
List of menu functions
press:
1. Phone_book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
0. Goodbye
"""
mainmenuselect = True
while mainmenuselect: 
	print(mainMenu)
	number = int(input('enter a number to select: '))
	match number:
		case 0:
			mainmenuselect = False
		case 1:
			phonebook =     """
 			PhoneBook
 				press;
 				1 - Search
 				2 - Service Nos
 				3 - Add name
 				4 - Erase
 				5 - Edit
			        6 - Assign tone
			        7 - Send b card
 				8 - Options
 				9 - Speed dails
 				10 - Voice tags
			        0 - Back to main menu
				""";
			phoneBook = True
			while phoneBook:
				print(phonebook) 
				phonebookselection = int(input('Select Menu: '))
				match phonebookselection:
					case 0:
						phoneBook = False
					case 1:
    						print('search')
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
    						print('Send b card')
					case 8: 
						options = """
							Options menu
							Press;
							1 - Type of view
							2 - Memory status
							0 - Back to phonebook menu

							""";
						optionselect = True
						while optionselect:
							print(options)
							optionsselection = int(input('Select options: '))
							match optionsselection:
								case 0: 
									optionselect = False
								case 1:
									print('Type of view')
								case 2:
									print('Memory status')
								case _:
									print('invalid number')

					case 9:
						print('Speed tags')
					case 10:
    						print('Voice tags')
					case _:
						print('invalid number')

		case 2:
			messageBox ="""
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
			messageselection = True
			while messageselection:
				print(messageBox)
				messageselectionoption = int(input('Select message options: '))
				match messageselectionoption:
					case 0:
						messageselection = False 
					case 1:
						print('Write messages')
					case 2:
						print('Inbox')
					case 3:
						print('Outbox')
					case 4:
						print('Picture messages')
					case 5:
						print('Teplates')
					case 6:
						print('Write messages')
					case 7:
						Messagesettingsmenu = """
							Press:
							1 - Set 1
							2 - Common
							0 - Back to message menu
							"""
						messagesettings =True
						while messagesettings:
							print(Messagesettingsmenu)	
							messagesettingsselect = int(input('Select message settings option:'))
							match messagesettingsselect:
								case 0:
									messagesettings = False
								case 1:
									set1 = """
									Select set
									Press:
									1 - Message center number
									2 - Messages sent as
									3 - Message validity
									0 - Back to message menu

									"""
									set = True
									while set:
										print(set1)
										setselectoption = int(input('Select set1 options: '))
										match setselectoption:
											case 0:
												set = False
											case 1:
												print('Message center number')
											case 2:
												print('Message sent as')
											case 3:
												print('Message validity')
											case _:
												print('invalid number')

								case 2:
									common = """
									To select common
									Press:
									1 - Delivery reports
									2 - Reply via same centre number
									3 - Character support
									0 - Back to message menu
									"""
									commonoption = True
									while commonoption:
										print(common)
										commonselection = int(input('Select common: '))
										match commonselection:
											case 0:
												commonoption = False
											case 1:
												print('Delivery reports')
											case 2:
												print('Reply via same centre number')
											case 3:
												print('Character support')
											case _:
												print('invalid number')

					case 8:
						print('Info service')
					case 9: 
						print('Voice mailbox number')
					case 10: 
						print('Service command editor')
					case _:
						print('invalid number')


		case 3:
			print('Chat')

		case 4:
			callRegister = """
			Call register
			Press:
			1 - Missed calls
			2 - Recieved calls
			3 - Dial numbers
			4 - Erase recent call lists
			5 - Show call duration
			6 - Show call cost
			7 - Call cost settings
			8 - prepaid credit
			0 - Exist to main menu
			""";
			callregistermenu = True
			while callregistermenu:
				print(callRegister)
				callregisterselection = int(input('Select call register option: '))
				match callregisterselection:
					case 0:
						callregistermenu = False
					case 1: 
						print('Missed calls')
					case 2: 
						print('Recieved calls')
					case 3: 
						print('Dial numbers')
					case 4: 
						print('Erase recent call lists')
					case 5:
						showCallDuration = """
						Select call duration menu
						press:
						1 - Last call duration
						2 - All calls' duration
						3 - Received calls' duration
						4 - Dialed calls' duration
						5 - Clear timer
						0 - Back to call register menu
						""";
						callduratution = True
						while callduratution:
							print(showCallDuration)
							selectcallduration = int(input('Select call duration option: '))
							match selectcallduration:
								case 0:
									callduratution = False
								case 1:
									print('Last call duration')
								case 2:
									print('All calls duration')
								case 3:
									print('Received calls duration')
								case 4:
									print('Dailed calls duration')
								case 5:
									print('Clear timer')
								case _:
									print('invalid number')
					case 6:
						showCallCost = """
						Select call cost
						press:
						1 - Last call cost
						2 - All calls' cost
						3 - Clear counters
						0 - Back to call register menu	
						"""
						callcost = True
						while callcost:
							print(showCallCost)
							callcostoption = int(input('Select call cost option: '))
							match callcostoption:
								case 0:
									callcost = True
								case 1: 
									Print('Last call cost')
								case 2: 
									Print('AA calls cost')
								case 3: 
									Print('Clear counters')
								case _:
									print('invalid number')
					case 7: 
						callCostSettings = """
						Select call cost
						press:
						1 - Call cost limit
						2 - Show costs in
						0 - Back to call register menu
						"""
						costsettings = True
						while costsettings:
							print(callCostSettings)
							callcostsettingsoption = int(input('Select call cost settings option: '))
							match callcostsettingsoption:
								case 0:
									costsettings = False
								case 1:
									print('Print call cost limit')
								case 2:
									print('Show cost in')
								case _:
									print('invalid number')
					case 8:
						print('Prepaid credit')
					case _:
						print('invalid number')
		
		case 5:
			tones = """
				Tones
				press:
				1 - Ringing tone
				2 - Ringing tone volume
				3 - Incoming call alert
				4 - Composer
				5 - Message alert tone
				6 - Keypad tones
				7 - Warning and game tones
				8 - Vibrating alert
				9 - Screen saver
				0 - Exist to main menu
				"""
			tonemenu  = True
			while tonemenu:
				print(tones)
				toneoption = int(input('Select tones option: '))
				match toneoption:
					case 0:
						tonemenu = False
					case 1:
						print('Ringing tone')
					case 2:
						print('Ringing tone volume')
					case 3:
						print('Incoming call alert')
					case 4:
						print('Composer')
					case 5:
						print('Message alert tone')
					case 6:
						print('Keypads tone')
					case 7:
						print('Warning and game tones')
					case 8:
						print('Vibrating alert')
					case 9:
						print('Screen saver')
					case _:
						print('invalid number')

		case 6:
			settings = """
				settings
				Press:
				1 - Call settings
				2 - Phone settings
				3 - Security settings
				4 - Restore factory settings
				0 - Back to main menu
				"""
			settingmenu = True
			while settingmenu:
				print(settings)
				selectsettingoption = int(input('Select settings options: '))
				match selectsettingoption:
					case 0:
						settingmenu = False
					case 1:
						callsettings = """
							Select call settings
							Press:
							1 - Automatic redial
							2 - Speed dailling
							3 - Call waiting options
							4 - Own number sending
							5 - Phone line in use
							6 - Automatic answer
							0 - Back to settings menu
							"""
						callsettingmenu = True
						while callsettingmenu:
							print(callsettings)
							callsettingselect = int(input('Select call setting option: '))
							match callsettingselect:
								case 0:
									callsettingmenu = False
								case 1:
									print('Automatic redial')
								case 2:
									print('Speed dailling')
								case 3:
									print('Call waiting options')
								case 4:
									print('Own number sending')
								case 5:
									print('Phone line in use')
								case 6:
									print('Automatic answer')
								case _:
									print('invalid number')

					case 2:
						phonesettings = """
							Select phone settings
							Press:
							1 - Language
							2 - Cell info display
							3 - Welcome note
							4 - Network selection
							5 - Light
							6 - Confirm SIM Service actions
							0 - Back to setting menu
							"""
						phonesettingmenu = True
						while phonesettingmenu:
							print(phonesettings)
							phonesettingselect = int(input('Select phone settings option: '))
							match phonesettingselect:
								case 0:
									phonesettingselect = False
								case 1:
									print('Language')
								case 2:
									print('Cell info display')
								case 3:
									print('Welcome note')
								case 4:
									print('Network selection')
								case 5:
									print('Light')
								case 6:
									print('Confirm SIM Service actions')
								case _:
									print('invalid number')
					case 3:
						securitysettings = """
							Select security settings
							Press:
							1 - Pin code request
							2 - call barring request
							3 - Fixed dialling
							4 - Closed user group
							5 - Phone security
							6 - Change access codes	
							0 - Back to setting menu
							"""
						securitysettingmenu = True
						while securitysettingmenu:
							print(securitysettings)
							securitysettingselect = int(input('Select phone settings option'))
							match securitysettingselect:
								case 0:
									securitysettingmenu = False
								case 1:
									print('Pin code request')
								case 1:
									print('call barring request')
								case 1:
									print('Fixed dialling')
								case 1:
									print('Closed user group')
								case 1:
									print('Phone security')
								case 1:
									print('Change access codes')
								case _:
									print('invalid number')
					case 4:
						print('Restore factory settings')
					case _:
						print('invalid number')	
								
		case 7:
			print('Call divert')

		case 8:
			print('Games')

		case 9:
    			print('Calculator')

		case 10:
			print('Reminders')

		case 11:
			clock = """
				Select clock display
				Press:
				1 - Alarm clock
				2 - Clock settings
				3 - Date settings
				4 - Stopwatch
				5 - Countdown timer
				6 - Auto update of date and time
				0 - Back to main menu
				"""
			clockmenu = True
			while clockmenu:
				print(clock)
				clockmenuselect = int(input('Select clock menu: '))
				match clockmenuselect:
					case 0:
						clockmenu = False
					case 1: 
						print('larm clock')
					case 1: 
						print('Clock settings')
					case 1: 
						print('Date settings')
					case 1: 
						print('Stopwatch')
					case 1: 
						print('Countdown timer')
					case 1: 
						print('Auto update of date and time')

		case 12:
			print('Profiles')

		case 13:
			print('SIM_services')

		case 0:
			print('Goodbye')

		case _:
			print('invalid number')
		

     
 