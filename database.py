# database.py

import attendee

class Database:
	
	def __init__(self, fname):
		self.fname = fname
		self.load_list()
	
	
	def load_list(self):
		self.attendee_list = []
		with open(self.fname, "r") as f:
			self.populate_list(self.attendee_list, f)
			

	def populate_list(self, attendee_list, f):
		for line in f:
			name, company, state, email = line.rstrip().split(":")
			self.add_attendee(name, company, state, email)
			
	#create attendee with inputs and append to attendee list
	def add_attendee(self, name, company, state, email):
		att = attendee.Attendee(name, company, state, email)
		self.attendee_list.append(att)
	
	#write the current attendee list to the fname file
	def flush_list(self):
		with open(self.fname, "w") as fwrite:
			for attendee in self.attendee_list:
				fwrite.write(attendee.to_string()+"\n")
				
	#given a string of an attendee's name, return the 
	#corresponding attendee object
	def get_attendee(self, attendee_str):
		selection = None
		for attendee in self.attendee_list:
			if attendee_str.lower() == attendee.get_name().lower():
				return attendee
		return None
		
		
	#given an attendee's name, remove that attendee from the 
	#attendee list.
	def remove(self, attendee_str):
		#return whether or not an attendee was removed.
		for attendee in self.attendee_list:
			if attendee_str.lower() == attendee.get_name().lower():
				self.attendee_list.remove(attendee)
				return True
		return False
		
	def list_name_email(self, state="none"):
		print()
		for attendee in self.attendee_list:
			if state == attendee.get_state() or state == "none":
				print("Attendee: {0}, Email: {1}".format(attendee.get_name(), attendee.get_email()))