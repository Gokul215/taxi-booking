class customer:
    id=1
    def __init__(self,pickuppoint,droppoint,pickuptime) -> None:
        self.customerid=customer.id
        customer.id+=1
        self.pickuppoint=pickuppoint
        self.droppoint=droppoint
        self.pickuptime=pickuptime
        self.droptime=0
        self.amount=0
        