import requests
import schedule
import time

### IMPORTANT
### Adding time.sleep in between all possible function calls makes sure there is no concurrency issues 
### System has not been stress tested yet so better to remain on safe side


r = requests.get('https://lab1.owainpill.de')
print(requests.get('https://lab1.owainpill.de'))

### On a printer rotate we want to repeatedly take pictures so that silicone velocity can be calculated
def job1():
    time.sleep(1)
    print(requests.get('https://lab1.owainpill.de/rotateprinter'))
    time.sleep(2)
    counter=0
    while counter < 30: 
        print(counter)
        print(requests.get('https://lab1.owainpill.de/takepicture'))
        counter+=1
        time.sleep(5)

def job2():
    time.sleep(2)
    print(requests.get('https://lab1.owainpill.de/toggleheater'))
    time.sleep(1)

        

schedule.every(22).minutes.do(job1)#job to rotate printer and then trigger taking photos - do every 20/25 minuts
# could also do at random intervals instead
#schedule.every(3).seconds.do(job2)#job to rotate printer and then trigger taking photos - do every 20/25 minuts
#schedule.every(3).seconds.do(job2)#job to rotate printer and then trigger taking photos - do every 20/25 minuts


#toggle the heater every once in a while - random to keep it interesting
schedule.every(20).to(35).minutes.do(job2)

while 1:
    schedule.run_pending()
    print(str(schedule.idle_seconds())+' time to next')
    time.sleep(1)

