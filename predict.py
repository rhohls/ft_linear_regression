import json
# 396286 (0 price)

def estimatePrice(theta0, theta1, dist):
    return theta0 + (theta1 * dist)


def loadvalues():
    with open('theta_values.json') as json_file:
        data = json.load(json_file)
    return data["theta0"], data["theta1"]


def main():
    try:
        theta0, theta1 = loadvalues()
    except:
        print("There was an issue loading theta values, please try re-running the training program")
        exit()

    inputstr = ""
    while inputstr.lower().strip() != "exit":
        inputstr = input("Enter a distance\n")

        try:
            result = estimatePrice(theta0, theta1, float(inputstr))
            print("The estimate price is:", round(result,2))
        except:
            print("There was an error")


 if __name__ == "__main__":
    main()
