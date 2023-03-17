# Importing the libs
import csv
from matplotlib import pyplot as plt
from collections import defaultdict as dd
import time

# Class that separate each info rom athlete by atribute.
class Athlete:
    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.sex = data[2]
        self.age = data[3]
        self.height = data[4] 
        self.weight = data[5]
        self.team = data[6]
        self.noc = data[7]
        self.games = data[8]
        self.year = data[9]
        self.season = data[10]
        self.city = data[11]
        self.sport = data[12]
        self.event = data[13]
        self.medal = data[14]

# Defining a list of all continents
CONTINENTS =  ['Africa', 'Asia', 'Europe', 'North America', 'South America','Oceania']
  

# The project will have somethin about 5 options of filter. The first one is already implemented in this version.
def main():
        start_time = time.time()
        # Opening the files
        athletes = csv.reader(open('athlete_events.csv'))
        countries_continents = csv.reader(open('countries-continents.csv'))
        nocs = csv.reader(open('noc_regions.csv'))
        

        # The first step in this algorithm is to make a first reading to generate the structrues that are used inside the actual tasks. 
        
        # noc_country = dict key/country e value/noc
        noc_country = dd(lambda: [], {})
        country_noc_continent = dd(lambda: [], {})
        next(nocs)
        # In this reading, it was necessary to explicit inform the Hong Kong occurrence because iw was part from the database information incosistencies
        for line in nocs:
            noc = line[0]
            country = line[1]
            aux = line[2]
            if aux == "Hong Kong":
                country = "Hong Kong"
                noc = "HKG"
            noc_country[noc].append(country)
            country_noc_continent[country].append(noc)
        
        
        
        # Func to correct some database information incosistencies
        def trap(country):
            equal_to = {
            "Burkina": "Burkina Faso", 
            "Congo":"Republic of Congo", 
            "Congo, Democratic Republic of": "Democratic Republic of the Congo",
            "Burma (Myanmar)": "Myanmar", 
            "East Timor":"Timor-Leste", 
            "Korea, North": "North Korea",
            "Korea, South": "South Korea", 
            "Russian Federation":"Russia", 
            "CZ": "Czech Republic",
            "United Kingdom":"UK", 
            "Vatican City":"NA", 
            "Antigua and Barbuda": "Antigua", 
            "Saint Kitts and Nevis" : "Saint Kitts", 
            "Saint Vincent and the Grenadines":"Saint Vincent",
            "Trinidad and Tobago": "Trinidad", 
            "US":"USA", "Tuvalu":"NA", 
            "Bolivia":"NA"
            }
            
            eq_to = dd(lambda: country, equal_to)

            
            return eq_to[country]
        

        # continent_countries = dict key/continent e value/array from countries
        # Use of default dict to avoid the step of define each new occurence in dict.
        continent_countries = dd(lambda: [], {})
        event_athletes = dd(lambda: [], {})
        season_athletes = dd(lambda: [], {})

        # country_athlete = dict key/country and value/array containing class Athlete 
        country_athletes = {}

        # Feeding countries_continents
        next(countries_continents)
        for line in countries_continents:
            continent = line[0]
            country = trap(line[1])
            data = [country, country_noc_continent[country]]
            continent_countries[continent].append(data)
            country_noc_continent[country].append(continent)
            country_athletes[country]= []
            
        # Feeding Athlete_country
        next(athletes)
        for line in athletes:
            athlete = Athlete(line)
            event = athlete.event
            season = athlete.season
            try:
                Athlete_country = noc_country[athlete.noc][0]
                country_athletes[Athlete_country].append(athlete)
            except KeyError:
                continue
            except IndexError:
                continue

            event_athletes[event].append(athlete)
            season_athletes[season].append(athlete)
        
        print(f'The app needed {(time.time() - start_time):.2} to execute the first reading of database.')


        
        
        

        '''
        Storage structures created.
        continent_countries = dict key/continent e value/array dos countryes 
        noc_country = dict key/noc e value/country
        country_noc_continent = dict key/country e value/noc
        country_athlete = dict key/country e value/array de objetos Athlete
        event_athletes = dicionário com key/esporte e value/array de objetos Athlete
        season_athletes = dicionário com key/season e value/array de objetos Athlete
        '''

        
        # Task1 generate a line plot by filtering the athletes that are included in the specifications of user's input. 
        def task1():
            print("Task 1 just Started!\n.\n.")

            # Storage variables Declaration.
            
            # List to store the years in sorted order.
            years = []

            # A dict to store each with all the 6 counters to each continent.
            data_year = dd(lambda: {"Africa":0, "Asia":0, "Europe":0, "North America":0, "South America":0, "Oceania":0}, {})
            # Lists to each continent with the values to each year in a way that it follows the sorted order frm data_year
            africa, asia, europa, na, oceania, sa =  [], [], [], [], [], []
            # Athletes that were filtered.
            count = 0

            # User inputs to determinate the filter conditions
            startAT = input("Insert the bottom limit year: ")
            endAT = input("Insert the top limit year: ")
            t_medal = input("Insert the medal type: ")
            t_season = input("Insert the season of the Games: ")

            start_time = time.time()
            # Filtering the athletes from the specific season storage structure. 
            for at in season_athletes[t_season]:
                if startAT <= at.year <= endAT:
                    if at.medal == t_medal:
                        count += 1
                        country = noc_country[at.noc][0]
                        continent = country_noc_continent[country][-1]
                        data_year[at.year][continent] += 1

            # I/O to User in terminal.
            print(f'\n\n{count} athletes filtered in Task 1.')
            print("Close the plot window to end the Task!")

            # Separating the data rom data_year to each continent list
            for year in sorted(data_year):
                years.append(year)
                for continent in data_year[year]:
                    if continent == "Africa" : out = africa
                    elif continent == "Asia": out = asia
                    elif continent == "Europe": out = europa
                    elif continent == "North America": out = na
                    elif continent == "Oceania": out = oceania
                    elif continent == "South America": out = sa
                    out.append(data_year[year][continent])

            # Creating the plot
            plt.plot(years, africa, marker=".", label="Africa")
            plt.plot(years, asia,marker='.', label='Asia')
            plt.plot(years, europa,marker='.', label='Europa')
            plt.plot(years, na,marker='.', label='America do Norte')
            plt.plot(years, sa, marker=".", label="América do Sul")
            plt.plot(years, oceania, marker=".", label="Oceania")
            plt.legend()
            plt.xlabel('Years')
            plt.ylabel(f'{t_medal} quantity')
            plt.title(f'{t_medal} Medal progression from {startAT} to {endAT}.')
            print(f'.\n.\nTask 1 needed {time.time() - start_time:.2f} to terminate.')
            plt.show()
           


        # In the final version, there will be a user interaction menu to define the task to be performed.
        # For now, the call will be explicit.
        task1()




            

        





try:
    main()
except KeyboardInterrupt:
    print("\nApp closed!")
