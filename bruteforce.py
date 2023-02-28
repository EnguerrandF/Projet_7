ACTIONS = {
    'Action-1': {'prix': 20, 'pourcentage': 5},
    'Action-2': {'prix': 30, 'pourcentage': 10},
    'Action-3': {'prix': 50, 'pourcentage': 15},
    'Action-4': {'prix': 70, 'pourcentage': 20},
    'Action-5': {'prix': 60, 'pourcentage': 17},
    'Action-6': {'prix': 80, 'pourcentage': 25},
    'Action-7': {'prix': 22, 'pourcentage': 7},
    'Action-8': {'prix': 26, 'pourcentage': 11},
    'Action-9': {'prix': 48, 'pourcentage': 13},
    'Action-10': {'prix': 34, 'pourcentage': 27},
    'Action-11': {'prix': 42, 'pourcentage': 17},
    'Action-12': {'prix': 110, 'pourcentage': 9},
    'Action-13': {'prix': 38, 'pourcentage': 23},
    'Action-14': {'prix': 14, 'pourcentage': 1},
    'Action-15': {'prix': 18, 'pourcentage': 3},
    'Action-16': {'prix': 8, 'pourcentage': 8},
    'Action-17': {'prix': 4, 'pourcentage': 12},
    'Action-18': {'prix': 10, 'pourcentage': 14},
    'Action-19': {'prix': 24, 'pourcentage': 21},
    'Action-20': {'prix': 114, 'pourcentage': 18},
}
ACTION_TWO = {
    'Action-1': {'prix': 20, 'pourcentage': 5},
    'Action-2': {'prix': 30, 'pourcentage': 10},
    'Action-3': {'prix': 50, 'pourcentage': 15},
    'Action-4': {'prix': 70, 'pourcentage': 20},
}


class BruteForceOfficiel:
    def __init__(self, data, price):
        self.capacity = price
        self.data = data
        self.conv_data = []

    def main(self):
        self.calculate_renta()
        result = self.force_brute(self.capacity, self.conv_data, [])
        self.calculate_gain_action(result)

    def force_brute(self, capacite, elements, elements_selection):
        if elements:
            val1, lstVal1 = self.force_brute(capacite, elements[1:], elements_selection)
            val = elements[0]
            if val[1] <= capacite:
                val2, lstVal2 = self.force_brute(capacite - val[1], elements[1:], elements_selection + [val])
                if val1 < val2:
                    return val2, lstVal2

            return val1, lstVal1
        else:
            return sum([i[2] for i in elements_selection]), elements_selection

    def calculate_renta(self):
        for value in self.data:
            self.conv_data.append([value, self.data[value]["prix"], (self.data[value]["prix"] * self.data[value]["pourcentage"])/100])

    def calculate_gain_action(self, result):
        result_data = 0
        result_data_gain = 0
        for action in result[1]:
            result_data += self.data[action[0]]["prix"]
            result_data_gain += self.data[action[0]]["prix"] + action[2]

        print("Algo brute : ", result_data, result_data_gain)
        print("Algo brute : ", result)


BruteForceOfficiel(ACTIONS, 500).main()
