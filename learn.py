import csv
import json


class LinearLearn:

    def __init__(self):
        self.theta0 = 0.0
        self.old_theta0 = 1.0
        self.theta1 = 0.0
        self.data = []
        self.data_length = 1

        self.error = 0.0001
        self.learn_rate = 0.01

    def estimatePrice(self, dist):
        return self.theta0 + (self.theta1 * dist)

    def load_data(self):
        with open( "data.csv", 'r' ) as theFile:
            reader = csv.DictReader(theFile)
            for line in reader:
                self.data.append([int(line["km"]), int(line["price"])])
        if len(self.data) < 1:
            raise Exception("no data")
        self.data_length = len(self.data)

    def min_error(self):
        if self.theta0 > self.old_theta0:
            er = self.theta0 - self.old_theta0
        else:
            er = self.old_theta0 - self.theta0
        return er > self.error



    def calc_theta(self):
        #data = [km, price]
        while self.min_error():
            val0 = 0.0
            val1 = 0.0

            for dist, price in self.data:
                val0 += self.estimatePrice(dist) - price
                val1 += (self.estimatePrice(dist) - price) * dist

            print("val0", val0)
            self.old_theta0 = self.theta0
            self.theta0 += self.learn_rate * (val0 / self.data_length)
            self.theta1 += self.learn_rate * (val1 / self.data_length)
            print("thr", self.theta0)


    def write_values(self):
        data = {"theta0": self.theta0, "theta1": self.theta1}
        with open('theta_values.json', 'w') as outfile:
            json.dump(data, outfile)


def main():

    # estPrice = theta0 + (theata1 * dist)
    # theta0 = learnRate * 1/m * SUM(estPrice(dist) - price)
    # theta1 = learnRate * 1/m * SUM((estPrice(dist) - price)*dist)
    # error = theta0_i  -  theta0_i-1

    linear = LinearLearn()
    linear.load_data()
    linear.calc_theta()
    linear.write_values()

    print(linear.theta0, linear.theta1)


if __name__ == "__main__":
    main()