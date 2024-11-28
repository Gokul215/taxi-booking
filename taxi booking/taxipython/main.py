from customer import customer
from Taxi import Taxi

class main:
    taxilist=[]
    def getfreetaxi(self,pickuppoint,pickuptime):
        freetaxis=[]
        for taxi in m.taxilist:
            if taxi.freeTime<=pickuptime and abs(self.getlocationtonumber(pickuppoint) - self.getlocationtonumber(taxi.currentSpot)) <= pickuptime-taxi.freeTime:
                freetaxis.append(taxi)
        return freetaxis
    
    def getlocationtonumber(self,location):
        locations={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
        return locations[location]
    def booktaxi(self,freetaxis,customer):
        minnearesttaxi=999
        for taxi in freetaxis:
            # int distanceBetweenCustomerAndTaxi = Math.abs((t.currentSpot - '0') - (pickupPoint - '0')) * 15;
            distanceBetweenCustomerAndTaxi=abs(self.getlocationtonumber(taxi.currentSpot )- self.getlocationtonumber(customer.pickuppoint) )*15
            if distanceBetweenCustomerAndTaxi < minnearesttaxi :
                bookedtaxi=taxi
                minnearesttaxi=distanceBetweenCustomerAndTaxi
                
        distancebetweenpickupanddrop=abs(self.getlocationtonumber(customer.pickuppoint) -self.getlocationtonumber(customer.droppoint)) *15
        bookedtaxi.totalEarnings+=(distancebetweenpickupanddrop-5)*10+100
        customer.amount=(distancebetweenpickupanddrop-5)*10+100
        bookedtaxi.currentSpot=customer.droppoint
        bookedtaxi.freeTime=customer.pickuptime+abs(self.getlocationtonumber(customer.pickuppoint) -self.getlocationtonumber(customer.droppoint))
        customer.droptime=bookedtaxi.freeTime
        bookedtaxi.tripdetails.append(customer)
        
        print(f"Taxi  {bookedtaxi.taxiid}  booked")

        
            
            
        
    
taxis=4
m=main()
for i in range(taxis):
    taxi=Taxi()
    m.taxilist.append(taxi)
while True:
        
    print("0. Book Taxi \n1. Print Taxi details")
    choice =int(input("enter your choice: "))
    match choice:
        case 0:
           
            pickuppoint=input("enter the pickup point(A-F):").upper()
            droppoint=input("enter the drop point: ").upper()
            pickuptime=int(input("enter the pickup time: "))
        
        
            if pickuppoint<'A' or pickuppoint >'F' or droppoint <'A' or droppoint>'F':
                print("invslid location")
                break
            customers=customer(pickuppoint,droppoint,pickuptime)
            freetaxi=m.getfreetaxi(pickuppoint,pickuptime)
            if freetaxi:
                freetaxi.sort(key=lambda freetaxi:freetaxi.totalEarnings)
                # print(freetaxi[0].taxiid)
                
                m.booktaxi(freetaxi,customers)
            else:
                print("no taxi available")
                
        case 1:
            for t in main.taxilist:
                t.printdetails()
        case _:
            break