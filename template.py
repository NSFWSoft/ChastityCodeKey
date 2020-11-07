import datetime
fmt = '%Y%m%d%H%M%S' 
start_datetime = datetime.datetime.strptime(start_time, fmt)
now_datetime = datetime.datetime.now()
difference = now_datetime - start_datetime
seconds_in_day = 24 * 60 * 60
diff_tuple = divmod(difference.days * seconds_in_day + difference.seconds, 60)
if diff_tuple[0] >= time_length:
    print("Here is your code: ")
    print(code)
    input()
else:
    print("Sorry you have to wait " + str(time_length - diff_tuple[0]) + " more minutes")
    input()
