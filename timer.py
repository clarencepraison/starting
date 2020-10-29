import time
start=input("Start Workout (y/n):")
if start=="y":
    timeLoop=True
def clock(exercise):
    sec=0
    Min=0
    print(" Begin " + exercise + "Workout" )
    while True:
        sec+=1
        print(str(Min) + " Mins " + str(sec) + " Sec")
        time.sleep(1)
        if sec == 3:
          break
clock(" chest ")
def set_01():
    sec=0
    Min=0
    print(" Rest ")
    while True:
         sec+=1
         print(str(Min) + " Mins " + str(sec) + " Sec")
         time.sleep(1)
         if sec == 2:
           break
def close():
    print("Get Hydrated")
set_01()
clock(" shoulder ")
set_01()
clock(" biceps ")
set_01()
close()