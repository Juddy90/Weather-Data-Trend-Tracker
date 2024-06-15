import sys
import backend



class ProgramUI:
    def __init__(self):
        self.__program_manager = backend.ProgramManager()
        self.run_program()

    def run_program(self):
        introduction = ("This program allows you to add weather data to track ")
        introduction+=("fire hazards\n")
        introduction+=("What would you like to do?\n")
        sys.stdout.write(introduction)

        try:
            self.__program_manager.load_csv()
        except:
            sys.stdout.write("\n"*5+"Error: Could not load file"+
                             ", incorrect values in file"+"\n"*5)

        choice = self.menu()
        while(choice!=5):
            if choice == 1:
                self.add_entry()
            elif choice == 2:
                self.display_entries()
            elif choice == 3:
                self.remove_data()
            elif choice == 4:
                self.save_all_data()
            else:
                ProgramUI.get_string("That is not an option. Click return to continue\n")

            choice=self.menu()

        sys.stdout.write("Thank you for using this program!\n")


    def menu(self):
        menu=("\n[1] Add Monthly Data\n")
        menu+=("[2] Display Monthly Data\n")
        menu+=("[3] Remove entry\n")
        menu+=("[4] Save All Data\n")
        menu+=("[5] Exit\n\n")

        sys.stdout.write(menu)

        user_choice = self.get_int("Choose an option ")

        return user_choice
    
    @staticmethod
    def get_string(prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        response = sys.stdin.readline().strip()
        return response

    def get_int(self,prompt):
        response = None
        while(response == None):
            try:
                response=int(ProgramUI.get_string(prompt))
            except:
                prompt = "Must select a menu \"number\". Try again: "
        return response

    def get_float(self,prompt):
        response = None
        while(response == None):
            try:
                response = float(ProgramUI.get_string(prompt))
            except:
                prompt = "Must be a number value. Try again: "
            return response
                         


    def add_entry(self):
        
        month_data = ProgramUI.get_string("\nPlease enter month as MMM: ").lower()
        temperature_data = self.get_float("\nEnter the temperature value: ")
        windspeed_data = self.get_float("\nEnter the windspeed value: ")
        rainfall_data = self.get_float("\nEnter the rainfall value: ")
        hazard_data = ProgramUI.get_string("\nEnter your fire hazard rating: ").lower()
        program_manager = backend.ProgramManager()

        try:
            self.__program_manager.append_to_list(month_data,temperature_data,
                                                  windspeed_data,rainfall_data,
                                                  hazard_data)
        except:
            sys.stdout.write("\n"*5+"Error: That didnt work, try again"+"\n"*5)


        
    def display_entries(self):
        x=0
        while(x<self.__program_manager.get_list_len):

            for data in self.__program_manager.get_data_list():
                sys.stdout.write("\nMonth: "+data.month+"\nTemperature: "+
                                 str(data.temperature)+"degrees\nWindspeed: "+
                                 str(data.windspeed)+"km/h\nRainfall: "+
                                 str(data.rainfall)+"mm\nHazard Rating: "+
                                 data.hazard_rating+"\n\n")
            
                x+=1
                
    def save_all_data(self):
        program_manager = backend.ProgramManager()
        x=0
        num_month = self.__program_manager.get_list_len
        try:
            data_file = open("data.csv","w")
            while(x<num_month):
                data_file.write(self.__program_manager.get_data_list()[x].month+",")
                data_file.write(str(self.__program_manager.get_data_list()[x].temperature)+",")
                data_file.write(str(self.__program_manager.get_data_list()[x].windspeed)+",")
                data_file.write(str(self.__program_manager.get_data_list()[x].rainfall)+",")
                data_file.write(self.__program_manager.get_data_list()[x].hazard_rating+"\n")
                x += 1
            data_file.close()
        except:
            sys.stdout.write("Error, could not save")
        

    def remove_data(self):
            program_manager = backend.ProgramManager()
            if  self.__program_manager.get_list_len<=0:
                sys.stdout.write("There are no entries yet, add an entry first!\n")
                return
            
            search_month = ProgramUI.get_string("What month do you want to delete? ").lower()

            x=0
            while(x<self.__program_manager.get_list_len):
                if (search_month == self.__program_manager.get_data_list()[x].month):

                    del (self.__program_manager.get_data_list()[x])

                    x-=1
                    
                x += 1



program_UI = ProgramUI()



    
