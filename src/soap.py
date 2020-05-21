from zeep import Client

cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
print(cliente.service.Multiply(4,5))
print(cliente.service.Add(4,5))
print(cliente.service.Divide(6,2))
print(cliente.service.Subtract(7,5))


