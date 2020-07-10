class FeelsLike:
    # Class can be declared with existing temperature and humidity data in lists.
    def __init__(self, temps=[], humid=[]):
        self.temps = temps
        self.humid = humid
        self.time = 0
        self.feels = {}

    # Function that computes the feel like temperature
    @staticmethod
    def calc_feel_like(temp, humid):
        feel = -42.379 + (2.04901523 * temp)
        feel += (10.14333127 * humid) - (0.22475541 * temp * humid)
        feel -= (6.83783 * 1e-3 * temp ** 2)
        feel -= (5.481717 * 1e-2 * humid ** 2) + (1.22874 * 1e-3 * temp ** 2 * humid)
        feel += (8.5282 * 1e-4 * temp * humid ** 2) - (1.99 * 1e-6 * temp ** 2 * humid ** 2)
        return feel

    # Function computes the feel like over a range of time and updates the feels dictionary
    def get_feel_likes(self):
        for i in range(self.time):
            self.feels[i] = self.calc_feel_like(self.temps[i], self.humid[i])

    # Function that adds a temp and humid value point to the data set
    def add_data(self, temp, humid):
        self.time += 1
        self.temps.append(temp)
        self.humid.append(humid)

    # Prints the current feel likes so far
    def __str__(self):
        temp = ""
        for i in len(self.feels):
            temp += 'Time: {} Temp: {} Feels-like: {}'.format(i, self.temps[i], self.feels[i])
            temp += '\n'
        return temp
