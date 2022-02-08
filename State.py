"""
Description: This class collects values of each field and allows for the retrieval of those values,
                or to intechange values at any index.

Author: Eyob Tekle
Version: February 4, 2022
"""
class State:
    """
    Description: State constructor, takes in several values of state records
    :param State name
    :param State capitol
    :param State region
    :param State us house seating
    :param State population size
    :param covid cases
    :param covid deaths
    :param full vaccination rates
    :param median household income
    :param violent crime rates
    :return N/A    
    """
    def __init__(self, name, capitol, region, us_house_seats, population, covid_cases, covid_deaths, fvaccination_rates, med_house_inc, violent_crime_rate):
        self.name = name
        self.capitol = capitol
        self.region = region
        self.us_house_seats = us_house_seats
        self.population = population
        self.cov_cases = covid_cases
        self.covid_deaths = covid_deaths
        self.fvaccination_rates = fvaccination_rates
        self.med_house_inc = med_house_inc
        self.violent_crime_rate = violent_crime_rate

    """
    Getters
    """

    """
    Description: retrieves state names
    :param self
    :return state name
    """
    def get_name(self):
        return self.name

    """
    Description: retrieves name of state capitol
    :param self
    :return state capitol
    """
    def get_cap(self):
        return self.capitol

    """
    Description: retrieves name of state region
    :param self
    :return state region
    """
    def get_reg(self):
        return self.region

    """
    Description: retrieves number of state house seats
    :param self
    :return us house seats
    """
    def get_seats(self):
        return self.us_house_seats

    """
    Description: retrieves state population size
    :param self
    :return state populatio
    """
    def get_pop(self):
        return self.population

    """
    Description: retrieves number of state covid cases
    :param self
    :return state covid cases
    """
    def get_cases(self):
        return self.cov_cases
    
    """
    Description: retrieves number of state covid deaths
    :param self
    :return state covid deaths
    """
    def get_deaths(self):
        return self.covid_deaths

    """
    Description: retrieves state full vaccination rate
    :param self
    :return state full vaccination rate
    """
    def get_vaccine(self):
        return self.fvaccination_rates

    """
    Description: retrieves state median household income
    :param self
    :return state median household income
    """
    def get_income(self):
        return self.med_house_inc

    """
    Description: retrieves state violent crime rate
    :param self
    :return state violent crime rate
    """
    def get_violent(self):
        return self.violent_crime_rate

    """
    Setters
    """
    """
    Description: sets state names
    :param self
    :param state name
    :return N/A
    """
    def set_name(self, name):
        self.name = name

    """
    Description: sets state capitol
    :param self
    :param state capitol
    :return N/A
    """
    def set_cap(self, captiol):
        self.capitol = captiol

    """
    Description: sets state region
    :param self
    :param state region
    :return N/A
    """    
    def set_reg(self, region):
        self.region = region

    """
    Description: sets number of state house seats
    :param self
    :param state us house seating
    :return N/A
    """
    def set_seats(self, us_house_seats):
        self.seats = us_house_seats 

    """
    Description: sets state population size
    :param self
    :param state population
    :return N/A
    """
    def set_pop(self, population):
        self.population = population
    
    """
    Description: sets number of state covid cases
    :param self
    :param state covid cases
    :return N/A
    """
    def set_cases(self, covid_cases):
        self.cov_cases = covid_cases
    
    """
    Description: sets number of state covid deaths
    :param self
    :param state covid deaths
    :return N/A
    """
    def set_deaths(self, covid_deaths):
        self.covid_deaths = covid_deaths

    """
    Description: sets rate of full vaccinations
    :param self
    :param state full vaccine rate
    :return N/A
    """
    def set_vaccine(self, vaccine_rate):
        self.fvaccination_rates = vaccine_rate

    """
    Description: sets state median household income
    :param self
    :param state median household income
    :return N/A
    """
    def set_income(self, med_income):
        self.med_house_inc = med_income

    """
    Description: sets state violent crime rate
    :param self
    :param state violent crime rate
    :return N/A
    """
    def set_violent(self, violence):
        self.violent_crime_rate = violence

    """
    Description: returns true if current object's state name has a higher rank than state name of compared object
    :param self
    :param state object
    :return True or False
    """
    def __gt__(self, state):
        return self.name > state.get_name()

    """
    Description: prints out string of state object
    :param self
    :return object string
    """
    def __str__(self):
        return ("State Name: " + self.name + "\nCapitol: " + self.capitol + "\nRegion: " + self.region + "\nUS House Seats: "
         + self.us_house_seats + "\nPopulation: " + self.population + "\nCovid Cases: " + self.cov_cases + "\nCovid Death: " + self.covid_deaths
         + "\nFull Vaccination Rate: " + self.fvaccination_rates + "\nMedian House Income: " + self.med_house_inc + "\nViolent Crime Rate: " 
         + self.violent_crime_rate + "\n")


