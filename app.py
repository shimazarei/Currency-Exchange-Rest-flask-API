from flask import Flask, request, abort
import xmltodict
import json
import requests
app = Flask(__name__)

SOURCE_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml"

currency_temp = {}

def CurrenciesRate(url):
    def URL_LOAD():
        data = requests.get(url)
        xpars = xmltodict.parse(data.text)
        bankdata = json.dumps(xpars)
        return json.loads(bankdata)
    def FILE_LOAD():
            datafile = open(url, 'r') 
            return xmltodict.parse(datafile.read())

    if url.find("https://") != -1:
        print("Data is loading from url")
        data = URL_LOAD()
    else:
        print("Data is loading from file")
        data = FILE_LOAD()
    for i in data["gesmes:Envelope"]["Cube"]["Cube"]:
        time = i["@time"]
        for j in i["Cube"]:
            if not time in currency_temp:
                currency_temp[time] = {}
            currency_temp[time][j["@currency"]] = j["@rate"]
    return currency_temp

@app.route("/currencyexchange/", methods=['GET'])
def Currency_Exchange(data=None):
    if not data:
        data = request.json
    amount = data["amount"]
    reference_date = data["reference_date"]
    Primary_currency = data["src_currency"]
    Exchanged_currency = data["dest_currency"]
    if not reference_date in currency_temp:
        return json.dumps({"message": "Error the date is not valid!"})

    Primary_currency = Primary_currency.upper()
    Exchanged_currency = Exchanged_currency.upper()
    if Primary_currency != "EUR":
        rate_src = currency_temp[reference_date][Primary_currency]
        currency_conversion = amount / float(rate_src)
    else:
        # If EUR exchange to another currency
        rate_dest = currency_temp[reference_date][Exchanged_currency]
        currency_conversion = amount * float(rate_dest)

    return json.dumps({'amount': currency_conversion, 'currency': Exchanged_currency})

# For web API port 5000 must be used
if __name__ == '__main__':
    CurrenciesRate(SOURCE_URL)
    app.run(host='0.0.0.0', port=5000, debug=True)

# For test to return result in json format:
    CurrenciesRate("data/eurofxref-hist-90d.xml")
    print ( json.loads( Currency_Exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2020-04-15"}) )["amount"]  )
 
    
