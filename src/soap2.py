from zeep import Client

cliente = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')

print(cliente.service.NumberToWords(5))

print(cliente.service.NumberToDollars(12.20))


