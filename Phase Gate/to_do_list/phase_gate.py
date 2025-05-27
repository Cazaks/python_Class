
menu = """
	To-Do List Manager;
	1. Add task
	2. View task
	3. Mark task as complete
	4. Delete a task
	5. Exist
	"""
menuselect = True
while menuselect:
	print(menu)
	number = int(input('enter a number to select: '))
	match number:
		case 0:
			menuselect = false
		case 1:
			taskselect = """
			To-Do List Manager;
			1. Add task
			2. View task
			3. Mark task as complete
			4. Delete a task
			5. Exist
			"""
			print("Add task")
			print("Task added")
		case 2:
			viewselect = """
			To-Do List Manager;
			1. Add task
			2. View task
			3. Mark task as complete
			4. Delete a task
			5. Exist
			"""
			print("view tast") 
			print("Task viewed")

		case 3: 
			markselect = """
			To-Do List Manager;
			1. Add task
			2. View task
			3. Mark task as complete
			4. Delete a task
			5. Exist
			"""
			print("mark as complete")
			print("Task completed")

		case 4: 
			deleteselect = """
			To-Do List Manager;
			1. Add task
			2. View task
			3. Mark task as complete
			4. Delete a task
			5. Exist
			"""

			print("Delecte task")
			print("Task delected")

		case 5:
			print("Exit")
		case _:
			print("Invalid number")
		

	