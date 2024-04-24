seconds = int(input("Choose time, in seconds: "))
minute = seconds // 60
seconds_rem = seconds % 60       
print(str(minute) + "Min " + str(seconds_rem) + "Sec")