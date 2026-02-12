import time;

start = time.time();                        #declares the start of the timer

for i in range(10):                         #sets the timer length, default at 10 seconds
    time.sleep(1);                          #sets the interval delay to 1 second
    print("time left:", abs(i - 9));       #displays a message every second, abs() displays the correct time left

end = time.time();                          #declares the end of the timer

length = end - start;                       #finds the total elapsed time
length = int(length);                       #rounds the time to the nearest second

print("it took", length - 1, "seconds");    #displays total elapsed time

#IMPORTANT, to be merged with the randomization function in the complete logic file


#IGNORE, used to test timer functionality
#>==================================================

'''
for i in range(11):
    time.sleep(1);
    print("time left:", i);
'''

#>==================================================


