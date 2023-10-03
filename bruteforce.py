import time
import csv


class BruteForce:
    def __init__(self, name_csv, price):
        self.capacity = price
        self.name_csv = name_csv
        self.data = self.open_csv()

    def main(self):
        time_start = time.time()
        result = self.force_brute(self.capacity, self.data, [])
        print(f"Gain: {result[0][0]}, Prix de vente: {result[1]}, List action: {result[0][1]}")
        print(f"Temps d'executions: {time.time() - time_start} secondes")

    def open_csv(self):
        with open(self.name_csv, newline="", encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=","))
        shares_list = []
        for line in reader[1:]:
            shares_list.append({
                    "name": line[0],
                    "price": float(line[1]),
                    "percentage_profit": float(line[2]),
                    "profit": round((float(line[1]) * float(line[2])) / 100, 2)
                })
        return shares_list

    def force_brute(self, price, data, selected_item):
        if data:
            val1, lstVal1 = self.force_brute(price, data[1:], selected_item)
            data_current = data[0]
            if data_current["price"] <= price:
                val2, lstVal2 = self.force_brute(price - data_current["price"], data[1:], selected_item + [data_current])
                if val1 < val2:
                    return val2, lstVal2
            return val1, lstVal1
        else:
            return [sum([i['profit'] for i in selected_item]), selected_item], sum([i['price'] for i in selected_item])


# BruteForce("./data/small_data.csv", 1.0).main()
# BruteForce("./data/dataset1_Python+P7.csv", 500).main()
# BruteForce("./data/dataset2_Python+P7.csv", 500).main()
