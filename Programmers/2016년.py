import sys
a,b = map(int, sys.stdin.readline().rstrip().split())
days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
count = 0
for i in range(a-1):
    count += months[i]
count += b
#SUN,MON,TUE,WED,THU,FRI,SAT
if count % 7 == 1:
    print("FRI")
elif count % 7 == 2:
    print("SAT")
elif count % 7 == 3:
    print("SUN")
elif count % 7 == 4:
    print("MON")
elif count % 7 == 5:
    print("TUE")
elif count % 7 == 6:
    print("WED")
elif count % 7 == 0:
    print("THU")