class Taxi:
    id=1
    def __init__(self) -> None:
        self.taxiid=Taxi.id
        Taxi.id+=1
        self.currentSpot='A'
        self.freeTime=6
        self.totalEarnings=0
        self.tripdetails=[]
    
    def printdetails(self):
        print(f"Taxi id- {self.taxiid} Total earnings -{self.totalEarnings}")
        print("TaxiID    CustomerID    From    To    PickupTime    DropTime    Amount")
        for trip in self.tripdetails:
            print(f"{self.taxiid}           {trip.customerid}              {trip.pickuppoint}    {trip.droppoint}       {trip.pickuptime}         {trip.droptime}            {trip.amount}")
        print("--------------------------------------------------------------------------------------")
        