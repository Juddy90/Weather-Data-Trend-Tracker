class WeatherData:
    
    __month = "MMM-YY"
    __temperature = 0
    __windspeed = 0
    __rainfall = 0
    __hazard_rating = None

    def __init__(self,month_data,temperature_data,windspeed_data,rainfall_data,
                 hazard_data):

        self.__month=month_data
        self.temperature=temperature_data
        self.windspeed=windspeed_data
        self.rainfall=rainfall_data
        self.__hazard_rating=hazard_data

    @property
    def month(self):
        return self.__month

    @property
    def temperature(self):
        return self.__temperature

    @property
    def windspeed(self):
        return self.__windspeed

    @property
    def rainfall(self):
        return self.__rainfall

    @property
    def hazard_rating(self):
        return self.__hazard_rating


    @temperature.setter
    def temperature(self, new_temperature):
        if(new_temperature < 0):
            raise ValueError ("Value cannot be a negative")
        self.__temperature = new_temperature


    @windspeed.setter
    def windspeed(self, new_windspeed):
        if(new_windspeed < 0):
            raise ValueError ("Value cannot be a negative")
        self.__windspeed = new_windspeed


    @rainfall.setter
    def rainfall(self, new_rainfall):
        if(new_rainfall < 0):
            raise ValueError ("Value cannot be a negative")
        self.__rainfall = new_rainfall



class ProgramManager:
    def __init__(self):
        self.__data_list=[]

    def get_data_list(self):
        return self.__data_list
    
    @property
    def get_list_len(self):
        return len(self.__data_list)

    def load_csv(self):
            with open ("data.csv","r") as data_file:
                for line in data_file:
                    fields = line.strip().split(",")
                    month_data = fields[0]
                    temperature_data = float(fields[1])
                    windspeed_data = float(fields[2])
                    rainfall_data = float(fields[3])
                    hazard_data = fields[4]
                    self.append_to_list(month_data,temperature_data,
                                        windspeed_data,rainfall_data,
                                        hazard_data)


    def append_to_list(self,month_data,temperature_data,windspeed_data,
                       rainfall_data,hazard_data):
        weather_data = WeatherData(month_data,temperature_data,windspeed_data,
                                   rainfall_data,hazard_data)


        self.__data_list.append(weather_data)
