from time import sleep
from tkinter import *
from tkinter import messagebox


class Chronometer(Tk):
    def __init__(self):
        # Defining dimension
        Tk.__init__(self)

        self.geometry('300x300')
        self.title('Darlan\'s Chronometer')

        # Creating display frame
        self.display_frame = LabelFrame(self)
        self.display_frame.pack()

        # Variables hour,min and seconds
        self.seconds = 0
        self.hour = 0
        self.minutes = 0

        # Display Label
        self.display_time = Label(self.display_frame, text='00:00:00', font=('Verdana', 25))
        self.display_time.pack()

        # Frame to choose time
        self.choose_time_frame = Frame(self)
        self.choose_time_frame.pack()
        # Spin related to Hour (0-23)
        self.spin_hour = Spinbox(self.choose_time_frame, width=2, from_=0, to_=23, font=('Verdana', 15))
        self.spin_hour.pack(side=LEFT)
        # Separator
        self.separate_hour_min = Label(self.choose_time_frame, text=':', font=('Verdana', 10))
        self.separate_hour_min.pack(side=LEFT)
        # Spin related to Minutes (0-59)
        self.spin_minute = Spinbox(self.choose_time_frame, width=2, from_=0, to_=59, font=('Verdana', 15))
        self.spin_minute.pack(side=LEFT)
        # Separator
        self.separate_min_seconds = Label(self.choose_time_frame, text=':', font=('Verdana', 10))
        self.separate_min_seconds.pack(side=LEFT)
        # Spin related to Seconds (0-59)
        self.spin_seconds = Spinbox(self.choose_time_frame, width=2, from_=0, to_=59, font=('Verdana', 15))
        self.spin_seconds.pack(side=LEFT)

        # Button start frame
        self.button_frame = Frame(self)
        self.button_frame.pack()
        # Button start
        self.button_start = Button(self.button_frame, text='Start', font=('Verdana', 15), command=self.start)
        self.button_start.pack(side=LEFT)
        # Button Reset
        self.button_reset = Button(self.button_frame, text='Reset', font=('Verdana', 15), command=self.reset)
        self.button_reset.pack(side=RIGHT)



        self.result_frame = Frame(self)
        self.result_frame.pack()

        self.lresult = Label(self.result_frame, text='')
        self.lresult.pack()

    # Função para iniciar o timer
    def start(self):
        # This variable needs to be here so the system don't bug, it'll be called only once if this is on main
        # constructor. But this way, everytime we click on start button, it sets to True and then initiate the timer
        self.lestgo = True

        # Get the values from the spin boxes
        self.seconds = int(self.spin_seconds.get())
        self.minutes = int(self.spin_minute.get())
        self.hour = int(self.spin_hour.get())

        # In case no value's chosen, it show a message saying that a time should be chosen
        if self.seconds == 0 and self.minutes == 0 and self.hour == 0:
            messagebox.showinfo('Waring', 'Please choose a time')
        else:
            # Disable buttons start and the spin boxes so it can be changed until timer runs out
            self.button_start.config(state=DISABLED)
            self.spin_seconds.config(state=DISABLED)
            self.spin_hour.config(state=DISABLED)
            self.spin_minute.config(state=DISABLED)
            # Set the timer value to be run on our label
            self.display_time.config(
                text=f'{self.hour}:{self.minutes}:{self.seconds}' if int(self.spin_seconds.get()) > 10
                else f'0{self.hour}:0{self.minutes}:0{self.seconds}')
            self.chronometer()

    def chronometer(self):
        # Always decrease seconds by 1
        self.seconds -= 1

        # If all values equals zero, it sets lestgo to false and stops the 'after' function
        if self.seconds == 0 and self.hour == 0 and self.minutes == 0:
            self.lestgo = False
            # Enable button start and spin boxes
            self.button_start.config(state=NORMAL)
            self.spin_seconds.config(state=NORMAL)
            self.spin_minute.config(state=NORMAL)
            self.spin_hour.config(state=NORMAL)
            self.lresult.config(text='PARE!', font=('Calibri', 40))
        # If seconds is less than zero, sets seconds to 59
        if self.seconds < 0:
            self.seconds = 59
            # When seconds equals to zero, it checks if minutes is greater than zero and decrease it
            if self.minutes > 0:
                self.minutes -= 1
                # and also if minute equals zero and hour greater than zero, decreases hour by 1
                if self.minutes == 0 and self.hour > 0:
                    self.hour -= 1
        # Prepar the string to update our timer
        hours = f'{self.hour}' if self.hour > 9 else f'0{self.hour}'
        minutes = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
        seconds = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        # Shows the string
        self.display_time.config(text=hours + ':' + minutes + ':' + seconds)
        # This variable is set so it can be used as a parameter to stop the 'after' function if reset button is clicked
        global update_time
        if self.lestgo:
            # It'll wait 1 second until the next execution
            update_time = self.after(1000, self.chronometer)

    # Function to reset the timer at any time
    def reset(self):
        # Variable to set the value of the spin boxes to zero
        var = IntVar(self)
        var.set(0)
        # Set the start button to be clickable
        self.button_start.config(state=NORMAL)
        # Reset to 0 hour, minutes and seconds
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
        # Make the spin boxes clickable and the their value to 0
        self.spin_seconds.config(state=NORMAL, textvariable=var)
        self.spin_minute.config(state=NORMAL, textvariable=var)
        self.spin_hour.config(state=NORMAL, textvariable=var)
        # Cancel the 'after' function previously started
        self.after_cancel(update_time)
        # Text to be exhibited once reset button is clicked
        self.display_time.config(text='00:00:00')


# Main loop
if __name__ == '__main__':
    app = Chronometer()
    app.mainloop()
