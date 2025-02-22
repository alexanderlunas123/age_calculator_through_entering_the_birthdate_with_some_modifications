# import libraries

import tkinter as tk
from datetime import date

# GUI App class
class App:
    def __init__(self):
        # initialized window
        self.master = tk.Tk()
        self.master.geometry('600x300') 
        self.master.configure(bg="lightblue")
        self.master.resizable(0, 0)
        self.master.title('Age Calculator')
        self.statement = tk.Label(self.master)

    def run(self):
        # creating a label for person's name to display
        self.l1 = tk.Label(text="Name: ", font="courier 10", bg="lightblue")
        self.l1.grid(row=1, column=0)
        nameValue = tk.StringVar()

        # creating a entry box for input
        self.nameEntry = tk.Entry(self.master, textvariable=nameValue, relief="solid")
        self.nameEntry.grid(row=1, column=1, padx=10, pady=10)

        # label for year in which user was born
        self.l2 = tk.Label(text="Year: ", font="courier 10", bg="lightblue")
        self.l2.grid(row=2, column=0)
        yearValue = tk.StringVar()
        self.yearEntry = tk.Entry(self.master, textvariable=yearValue, relief="solid")
        self.yearEntry.grid(row=2, column=1, padx=10, pady=10)

        # label for month in which user was born
        self.l3 = tk.Label(text="Month: ", font="courier 10", bg="lightblue")
        self.l3.grid(row=3, column=0)
        monthValue = tk.StringVar()
        self.monthEntry = tk.Entry(self.master, textvariable=monthValue, relief="solid")
        self.monthEntry.grid(row=3, column=1, padx=10, pady=10)

        # label for day/date on which user was born
        self.l4 = tk.Label(text="Day: ", font="courier 10", bg="lightblue")
        self.l4.grid(row=4, column=0)
        dayValue = tk.StringVar()
        self.dayEntry = tk.Entry(self.master, textvariable=dayValue, relief="solid")
        self.dayEntry.grid(row=4, column=1, padx=10, pady=10)


        def check_year():
            #simple method to check the validity of a user input birth year
            self.statement.destroy()
            today = date.today()
            try:
                year = int(self.yearEntry.get())
                if today.year - year < 0:
                    self.statement = tk.Label(text=f"{nameValue.get()}'s age cannot be negative.", font="courier 10", bg="lightblue")
                    self.statement.grid(row=6, column=1, pady=15)
                    return False
                else:
                    return True
            except Exception as e:
                self.statement = tk.Label(text=f"{nameValue.get()}'s birth year cannot parse to int.", font="courier 10", bg="lightblue")
                self.statement.grid(row=6, column=1, pady=15)
                return False

        def check_month():
            #simple method to check the validity of a user input birth month
            self.statement.destroy()
            try:
                month = int(self.monthEntry.get())
                if month < 0 or month > 12:
                    self.statement = tk.Label(text=f"{nameValue.get()}'s birth month is outside 1-12.", font="courier 10", bg="lightblue")
                    self.statement.grid(row=6, column=1, pady=15)
                    return False
                else:
                    return True
            except Exception as e:
                self.statement = tk.Label(text=f"{nameValue.get()}'s birth month cannot parse to int.", font="courier 10", bg="lightblue")
                self.statement.grid(row=6, column=1, pady=15)
                return False
        
        def check_day():
            #simple method to check the validity of a user input birth day
            self.statement.destroy()
            try:
                day = int(self.dayEntry.get())
                if day < 0 or day > 31:
                    self.statement = tk.Label(text=f"{nameValue.get()}'s birth day is outside 1-31.", font="courier 10", bg="lightblue")
                    self.statement.grid(row=6, column=1, pady=15)
                    return False
                else:
                    return True
            except Exception as e:
                self.statement = tk.Label(text=f"{nameValue.get()}'s birth month cannot parse to int.", font="courier 10", bg="lightblue")
                self.statement.grid(row=6, column=1, pady=15)
                return False
            
        def get_zodiac_sign(day, month):
            astro_sign = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]    
            if month == 1:
                if day < 20:
                    astro_sign_index = astro_sign[0]
                else:
                    astro_sign_index = astro_sign[1]    
            elif month == 2:
                if day < 19:
                    astro_sign_index = astro_sign[1]
                else:
                    astro_sign_index = astro_sign[2]
            elif month == 3:
                if day < 21:
                    astro_sign_index = astro_sign[2]
                else:
                    astro_sign_index = astro_sign[3]    
            elif month == 4:
                if day < 20:
                    astro_sign_index = astro_sign[3]
                else:
                    astro_sign_index = astro_sign[4]    
            elif month == 5:
                if day < 21:
                    astro_sign_index = astro_sign[4]
                else:
                    astro_sign_index = astro_sign[5]    
            elif month == 6:
                if day < 21:
                    astro_sign_index = astro_sign[5]
                else:
                    astro_sign_index = astro_sign[6]    
            elif month == 7:
                if day < 23:
                    astro_sign_index = astro_sign[6]
                else:
                    astro_sign_index = astro_sign[7]    
            elif month == 8:
                if day < 23:
                    astro_sign_index = astro_sign[7]
                else:
                    astro_sign_index = astro_sign[8]    
            elif month == 9:
                if day < 23:
                    astro_sign_index = astro_sign[8]
                else:
                    astro_sign_index = astro_sign[9]    
            elif month == 10:
                if day < 23:
                    astro_sign_index = astro_sign[9]
                else:
                    astro_sign_index = astro_sign[10]    
            elif month == 11:
                if day < 22:
                    astro_sign_index = astro_sign[10]
                else:
                    astro_sign_index = astro_sign[11]
            elif month == 12:
                if day < 22:
                    astro_sign_index = astro_sign[11]
                else:
                    astro_sign_index = astro_sign[0]                
            return astro_sign_index        

        # defining the function for calculating age
        def ageCalc():
            self.statement.destroy()
            today = date.today()
            #adding some stuff for checking validity of inputs
            if check_year() and check_month() and check_day():
                birthDate = date(int(self.yearEntry.get()), int(
                    self.monthEntry.get()), int(self.dayEntry.get()))
                age = today.year - birthDate.year
                if today.month < birthDate.month or today.month == birthDate.month and today.day < birthDate.day:
                    age -= 1
                zodiac_sign = get_zodiac_sign(int(self.dayEntry.get()), int(self.monthEntry.get()))        
                self.statement = tk.Label(text=f"{nameValue.get()}'s age is {age}. Zodiac Sign: {zodiac_sign}.", font="courier 10", bg="lightblue")
                self.statement.grid(row=6, column=1, pady=15)

        # create a button for calculating age
        self.button = tk.Button(text="Calculate age", font="courier 12 bold", fg="white", bg="dodgerblue", command=ageCalc)
        self.button.grid(row=5, column=1)
        
        # infinite loop to run program
        self.master.mainloop()
        

if __name__ == '__main__':
    age_calc = App()
    age_calc.run()