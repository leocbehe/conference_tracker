# interface.py

import database


class Interface:
	
	def __init__(self, db):
		self.command = ""
		self.db = db
		self.options = [
			"add",
			"display",
			"delete", 
			"list", 
			"list by state", 
			"quit"
		]
		
	def should_proceed(self):
		return self.command != "quit"
		
	#gets user input and assigns it to self.command if valid
	def get_input(self):
		input_str = self.prompt().lower().strip()		
		while not (input_str in self.options):
			print("\nSorry, I didn't understand that command!")
			input_str = self.prompt().lower().strip()
		self.command = input_str		
		
	#carry out the command currently stored in self.command
	def execute_input(self):
		if self.command == "add":
			self.add_attendee()
		elif self.command == "display":
			self.display_attendee()
		elif self.command == "delete":
			self.delete_attendee()
		elif self.command == "list":
			self.list_name_email()
		elif self.command == "list by state":
			self.list_attendees_by_state()

	#prompt for attendee information and add attendee to list
	def add_attendee(self):
		name = input("What is the name of the attendee you would like to add? ")
		company = input("What is the company of the attendee you would like to add? ")
		state = input("What is the state of the attendee you would like to add? ")
		email = input("What is the email of the attendee you would like to add? ")
		self.db.add_attendee(name, company, state, email)
		
		
	#prompt for attendee name and list corresponding info
	def display_attendee(self):
		attendee_name = input("what is the name of the attendee you want to inspect? ")
		attendee = self.db.get_attendee(attendee_name)
		if attendee:
			self.print_attendee_info(attendee)
		else:
			print("Sorry! That attendee doesn't exist!")
		
	#prompt for attendee name and remove corresponding attendee
	def delete_attendee(self):
		attendee_str = input("Please specify the name of the attendee to delete. ")
		if self.db.remove(attendee_str): 
			print("Attendee deleted.")
		else:
			print("! Sorry, there was an error deleting that attendee. Are you sure " + \
					"the name was spelled correctly? ")
		
	#print the name and email info of each attendee
	def list_name_email(self):
		print("\nHere are all the attendees' names and emails:")
		self.db.list_name_email()
		
		
	#prompt for state name and list associated attendees
	def list_attendees_by_state(self):
		state = input("Please input the standard abbreviation of the state to " + \
						"filter attendees by. ")
		self.db.list_name_email(state)
		
		
	#prompt user for an input command, return command string
	def prompt(self):
		prompt_str = "\nPlease enter a command for what you would like "+ \
							"to do next. Your options are:\n\n"+ \
							"add : add an attendee to the list\n"+ \
							"display : display information on a specific attendee\n"+ \
							"delete : remove an attendee from the list\n"+ \
							"list : list all attendees\n"+ \
							"list by state : list all attendees from a given state\n"+ \
							"quit : exit the program\n"
		input_str = input(prompt_str)
		return input_str
		

	#given an attendee object, print a nice string listing its information.
	def print_attendee_info(self, attendee):
		print()
		print(" *****************")
		print(" * Attendee Info *")
		print(" *****************")
		print("  NAME: ", attendee.name)
		print("  COMPANY: ", attendee.company)
		print("  STATE: ", attendee.state)
		print("  EMAIL: ", attendee.email)