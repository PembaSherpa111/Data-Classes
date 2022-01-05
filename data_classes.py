from dataclasses import dataclass, field

@dataclass
class Orders:
    OrderID : int
    CustomerID : int
    SalespersonPersonID : int
    PickedByPersonID : int
    ContactPersonID : int
    BackorderOrderID : int
    OrderDate : 
    ExpectedDeliveryDate : date
    CustomerPurchaseOrderNumber : str
    IsUndersupplyBackordered : bool
    Comments : str
    DeliveryInstructions : str
    InternalComments : str
    PickingCompletedWhen : date
    LastEditedBy : int
    LastEditedWhen : date

    def __gt__(self,other):
        if self.OrderDate > other.OrderDate:
            print(True)
        else:
            print(False)
    
    def __ge__(self,other):
        if self.OrderDate >= other.OrderDate:
            print(True)
        else:
            print(False)

@dataclass
class Invoices:
    InvoiceID : int
    CustomerID : int
    BillToCustomerID : int
    OrderID : int
    DeliveryMethodID :int
    ContactPersonID : int
    AccountsPersonID : int
    SalespersonPersonID : int
    PackedByPersonID : int
    InvoiceDate : date
    CustomerPurchaseOrderNumber : str
    IsCreditNote : bool
    CreditNoteReason : str
    Comments : str
    DeliveryInstructions : str
    InternalComments : str
    TotalDryItems : int
    TotalChillerItems : int
    DeliveryRun : str
    RunPosition : str
    ReturnedDeliveryData : str
    ConfirmedDeliveryTime : date
    ConfirmedReceivedBy : str
    LastEditedBy : int
    LastEditedWhen : date

    def __gt__(self,other):
        if self.InvoiceDate > other.InvoiceDate:
            print(True)
        else:
            print(False)
    
    def __ge__(self,other):
        if self.InvoiceDate >= other.InvoiceDate:
            print(True)
        else:
            print(False)

@dataclass
class Customers:
    CustomerID : int 
    CustomerName : str
    BillToCustomerID : int
    CustomerCategoryID : int
    BuyingGroupID : int
    PrimaryContactPersonID : int
    AlternateContactPersonID : int
    DeliveryMethodID : int
    DeliveryCityID : int
    PostalCityID : int
    CreditLimit : float
    AccountOpenedDate : date
    StandardDiscountPercentage : float
    IsStatementSent : bool
    IsOnCreditHold : bool
    PaymentDays : int
    PhoneNumber : str
    FaxNumber : str
    DeliveryRun : str
    RunPosition : str
    WebsiteURL : str
    DeliveryAddressLine1 : str
    DeliveryAddressLine2 : str
    DeliveryPostalCode : str
    DeliveryLocation : str
    PostalAddressLine1 : str
    PostalAddressLine2 : str
    PostalPostalCode : str
    LastEditedBy : int
    ValidFrom : date
    ValidTo : date