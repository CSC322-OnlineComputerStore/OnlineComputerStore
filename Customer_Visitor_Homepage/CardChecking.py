from authorizenet import apicontractsv1
from authorizenet.apicontrollers import createTransactionController
from decimal import Decimal

class CreditCard:
    def __init__(self, number, exp_date, code):
        self.number = number
        self.expiration_date = exp_date
        self.code = code
        #self.name_on_card = name_on_card

    number = None
    expiration_date = None
    name_on_card = None
    code = None
    #    CVC_code = None
    def setNumber(self, number):
        self.number = number

    def setExpDate(self, expDate):
        self.expiration_date = expDate

    def setCode(self, code):
        self.code = code

    def showInfo(self):
        print("Number: "+self.number)
        print("Code: "+self.code)
        print("Exp Date: "+self.expiration_date)

class Response:
    success = False
    messages = []

def get_transaction_id():
    return "28Y3c4d6KY385jHv"

def get_api_login_id():
    return "3TJ94yrL"

def purchase(card, amount):
    authorization = apicontractsv1.merchantAuthenticationType()
    authorization.name = get_api_login_id()
    authorization.transactionKey = get_transaction_id()

    card_info = apicontractsv1.creditCardType()
    card_info.cardNumber = card.number
    card_info.expirationDate = card.expiration_date
    card_info.cardCode = card.code

    payment = apicontractsv1.paymentType()
    payment.creditCard = card_info

    request_info = apicontractsv1.transactionRequestType()
    request_info.transactionType = "authCaptureTransaction"
    request_info.amount = Decimal(amount)
    request_info.payment = payment

    request = apicontractsv1.createTransactionRequest()
    request.merchantAuthentication = authorization
    request.refId = "MerchantID-0001"
    request.transactionRequest = request_info

    controller = createTransactionController(request)
    controller.execute()

    api_response = controller.getresponse()
    response = response_options(api_response)
    return response

def response_options(api_response):
    response = Response()

    if api_response is None:
        response.messages.append("No response from api")
        return response

    if api_response.messages.resultCode == "Ok":
        response.success = hasattr(api_response.transactionResponse, 'messages')
        if response.success:
            response.messages.append(f"Success")
        else:
            if hasattr(api_response.transactionResponse, 'errors') is True:
                response.messages.append(f"Error")
        return response

    response.success = False
    response.messages.append(f"response code: {api_response.messages.resultCode}")
    return response

def read_line(filename, line_num):
    readfile = open(filename, "r")
    lines = readfile.readlines()
    line = readfile.readline(line_num)
    readfile.close()
    return lines

def remove_new_line_char(string_name):
    string_name.replace('\n', '')
    return string_name

def main():

    amount = "5000.00"
    card = CreditCard
    card.number = "4007000000027"
    card.expiration_date = "2050-01"
    card.code = "123"

    #card2 = CreditCard("4007000000027", "2050-01", "123")
    card2 = CreditCard
    card2.setNumber(card2, "4007000000027")
    card2.setCode(card2, "123")
    card2.setExpDate(card2, "2050-01")


    result = purchase(card2, 50.00)
    print("Card 2")
    print(result.success)


    file_info = read_line("info.txt", 0)
    print(file_info)
    amount_str = file_info[0]
    amount_str = amount_str.replace('\n', '')
    amount = Decimal(remove_new_line_char(file_info[0]))
    print(amount)


    response = purchase(card, amount)

    print(response.success)
    print(response.messages)

if __name__ == '__main__':
    main()