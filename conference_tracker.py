# conference_tracker.py

import interface
import database

#print welcome message
def print_welcome():
	print("\n")
	print("********************************************************")
	print("* Welcome to the metaverse. This program allows you to *")
	print("* interact with a list of attendees of a conference.   *")
	print("********************************************************")
	print()
	
	
#call db constructor
def init_database(fname):
	return database.Database(fname)
	
#call interface constructor
def init_interface(database):
	return interface.Interface(database)
	
	
#print goodbye message
def print_goodbye():
	print("\nSee ya next time!")
	
	
#get input file name from user
def get_list_filename():
	filename = input("Please provide the name of the file containing " + \
					"conference attendee information: ")
	return filename
	

def main():
	print_welcome()
	fname = get_list_filename()
	db = init_database(fname)
	iface = init_interface(db)	
	while iface.should_proceed():
		iface.get_input()
		iface.execute_input()
	db.flush_list()
	print_goodbye()

if __name__ == "__main__": main()