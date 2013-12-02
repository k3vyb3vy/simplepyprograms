#Object Oriented Button Clicker
#Made by k3vyb3vy.
#https://github.com/k3vyb3vy
#License: GNU GPL v2
#Share your improvements!
#Creates a button in a GUI, each time you click it updates the count!
from tkinter import * #Imports everything from Tkinter.

class Application(Frame):
	""" Clicky Clicky Button """
	
	def __init__(self, master):
		""" Initialize the frame """
		Frame.__init__(self, master)
		self.grid()
		self.button_clicks =0 #counts the clicks.
		self.create_widgets()
		
		
	def create_widgets(self):
		""" Creates a click-counting button! """
		#creates button
		self.button = Button(self)
		self.button["text"] = "Clicks = 0" 
		self.button["command"] = self.update_count
		self.button.grid()
		
		
	def update_count(self):
		""" Increases the click count by one each click and changes the button to display the new click number! """
		self.button_clicks += 1
		self.button["text"] = "Clicks = " + str(self.button_clicks)
		
		
#This stuff sets the title and size of the window, and calls everything.
root = Tk()
root.title("Clicky Clicky button by k3vyb3vy")
root.geometry("200x85")

app = Application(root)

root.mainloop()
