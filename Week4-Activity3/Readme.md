Exchange Currency Project – Class Diagram Explanation

1. Class Diagram – Domain/Entity Model

The class diagram represents the main business entities involved in the currency exchange system. It describes the data associated with customers, currencies, exchange rates, exchange requests, beneficiaries, and payments.

Main Classes

1. Customer

Represents a person who uses the currency exchange system.

Attributes:

customerId
fullName
email
phone
createdAt
Main functionality:

Store customer information
Identify the customer who makes an exchange

Relationship:

A customer can make multiple exchange requests.
A customer can have beneficiary information.

2. User

Represents the system login/account information.

Attributes:

userId
username
passwordHash
role
status
createdAt

Main functionality:

Register a user
Authenticate/login
Maintain account status
A Customer is associated with a User account.


3. Currency

Represents a currency supported by the system.

Attributes:

currencyId
code
name
country
symbol

Relationship:

An ExchangeRequest uses two currencies:

Sending currency
Receiving currency

4. ExchangeRate

Represents the exchange rate between two currencies.

Attributes:

rateId
fromCurrency
toCurrency
rate
validFrom
validTo

Functionality:

The system retrieves the exchange rate when the customer enters the amount to exchange.

5. Beneficiary

Represents the recipient of the exchanged money.

Attributes:

beneficiaryId
requestId
fullName
bankOrWallet
accountNo
country

Functionality:

Stores information about the person or account receiving the exchanged funds.


6. ExchangeRequest

This is the central class of the system.

It represents a customer’s currency exchange request.

Attributes:

requestId
customerId
sendCurrency
receiveCurrency
sendAmount
receiveAmount
exchangeRate
status
createdAt
Functionality:

It records:

The currency being sent
The currency being received
The amount being exchanged
The exchange rate
The calculated receiving amount
The current exchange status

7. Payment

Represents the payment made for an exchange request.

Attributes:

paymentId
requestId
cardHolderName
cardNumber
amount
paymentStatus
paidAt

Functionality:

Stores payment information and records whether payment was successful.


8. ExchangeStatus

An enumeration representing the current state of an exchange.

Possible values include:

PENDING
PROCESSING
COMPLETED
FAILED
CANCELLED
The status is updated as the exchange progresses.


Main Relationships

The important relationships are:

Customer → ExchangeRequest: One customer can make many exchange requests.
User → Customer: A user account is associated with a customer.
ExchangeRequest → Currency: Each request has a sending currency and receiving currency.
ExchangeRequest → ExchangeRate: An exchange request uses an exchange rate.
ExchangeRequest → Beneficiary: An exchange request has a recipient/beneficiary.
ExchangeRequest → Payment: An exchange request has payment information.
ExchangeRequest → ExchangeStatus: Each request has one current status.
