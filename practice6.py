class City:
    """
    attributes:
    name the name of a city [str]
    high: the record high temeratures [length-12 list of int]
    low: the record low temperatures [length-12 list of int]
    """
    def __init__(self,cityName,theHighs,theLows):
        """Returns a reference to a City object
        PreC: cityName is a string that names a city.
        theHighs is a length 12 list of ints.
        theHighs[k] is the record high for month k (Jan is month 0)
        theLows is a length 12 list of ints
        theLowss[k] is the record high for month k (Jan is month 0) """
        self.name = cityName
        self.high = theHighs
        self.low = theLows
    
    def HotMonths(self):
        """ Returns the number of months where the record high is strictly
        greater than 80.
        """
        count = 0
        for month in self.high:
            if month > 80:
                count +=1
        return count
    
    def Hotter(self,other):
        """Returns True if the city encoded in self has strictly more hot months than
        the city encoded in other.
        A month is hot if the record high for that month is > 80
        PreC: other is a city object """
        hot_months_1 = self.HotMonths()
        hot_months_2 = other.HotMonths()
        if hot_months_1 > hot_months_2:
            return True
        else:
            return False
    
    def Variation(self):
        """ Returns a length 12 list of ints whose k-th entry
        is the record high for month k minus the record low for month k. """
        variation_list = []
        for i in range(len(self.high)):
            variation = self.high[i] - self.low[i]
            variation_list.append(variation)
        return variation_list
    
    def Exaggerate(self):
        """ Modifies self.high so that each entry is increased by 1 and modifies
        self.low so that each entry is decreased by 1.
        """
        for i in range(12):
            self.high[i] = self.high[i] + 1
            self.low[i] = self.low[i] + 1
        return self.high, self.low

    def Hottest(C):
        """ Returns an item from C that represents the city that has the most
        hot months.
        PreC: C is a list of references to City objects """
        hottest_city = None
        max_hot_months = 0

        for city in C:
            hot_months = city.HotMonths()
            if hot_months > max_hot_months:
                max_hot_months = hot_months
                hottest_city = city.name
        
        return hottest_city



my_city_instance = City("Seattle", [99,101,102,103,104,105,106,106,106,106,107,108], [33,33,34,34,35,36,37,37,38,39,40,41])
print(my_city_instance.HotMonths())

other_city_instance = City("Georgia", [79,79,79,79,80,80,80,80,99,99,99,99], [22,22,22,22,33,33,33,33,44,44,44,44])
print(my_city_instance.Hotter(other_city_instance))

print(my_city_instance.Variation())

print(my_city_instance.Exaggerate())

print(City.Hottest([my_city_instance, other_city_instance]))