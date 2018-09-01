# attendee.py

class Attendee:
	
	def __init__(self, name, company, state, email):
		self.name = name
		self.company = company
		self.state = state
		self.email = email
		
	def get_name(self):
		return self.name
		
	def set_name(self, name):
		self.name = name
		
	def get_company(self):
		return self.company
		
	def set_company(self, company):
		self.company = company
		
	def get_state(self):
		return self.state
		
	def set_state(self, state):
		self.state = state
		
	def get_email(self):
		return self.email
		
	def set_email(self, email):
		self.email = email
		
	def to_string(self):
		str = ":".join([self.name, self.company, self.state, self.email])
		return str