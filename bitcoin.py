#import the necessary modules required for this program to run(here, requests and sys)
import requests
import sys
try:
   #the length of the command line argument should be 2
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    #if the input is an alphabet, ask the user for an input again
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    #if the length of the command line argument is more than 1, then get the json file from the api of coindesk and print the final rate
    elif (len(sys.argv) > 1 ):
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        output = response.json()

        rateFloat = output["bpi"]["USD"]['rate_float']

        perCoin = rateFloat * float(sys.argv[1])
        #round the final price to 4 digits
        print(f"${perCoin:,.4f}")

except requests.RequestException:
    sys.exit()