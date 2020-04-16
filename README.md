# Currency Exchange application in Python 3
This application is a flask API web application which is designed for currency exchange in python. The source url is indicated in this link: https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml

To call this API use following command:

```
curl -X POST -H "Content-Type: application/json" -d '{"amount": 25.789, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2020-04-15"}' http://localhost:5000/currencyexchange/
```

The response is in Json format like:

    {"amount":  0.87385, "currency": "GBP"}

1) In order to run this application Docker is used. For building application with docker run following command on terminal:

   $ docker build . -t pyconv

2) To run appication execute following command:

   $ docker run --name pyconv -p 5000:5000 -d pyconv

3) To run the test file:

   $ docker exec -it pyconv pytest
   
4) For stoping api run below commands:

   $ docker stop pyconv
   
   $ docker rm pyconv   

