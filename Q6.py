def display_data(data):
    print("first 3 : ",data[:3:])
    print("last 3 : ", data[-3::])
    print("",data[1:6:])
    print(" ", data[::-1])

data = [10,20,30,40,50,60,70,80,90,100]
display_data(data)