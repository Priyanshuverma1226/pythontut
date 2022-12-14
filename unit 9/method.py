class car:
    name=""
    ex_room_price=0
    third_party_price=0
    taxes=0
    def on_road_price(self):
        on_road=self.ex_room_price+self.third_party_price+self.taxes
        return on_road
car1=car()
# print(type(car1))
car1.name="Alto"
car1.ex_room_price=500000
car1.third_party_price=50000
car1.taxes=20000
print(f'Car 1 Name : {car1.name}')
# print(car1.ex_room_price)
# print(car1.third_party_price)
# print(car1.taxes)
print("Car 1 Price :",car1.on_road_price())
car2=car()
car2.name="Wagon R"
car2.ex_room_price=600000
car2.third_party_price=60000
car2.taxes=20000
print(f"Car 2 Name : {car2.name}")
print("Car 2 Price ",car2.on_road_price())

