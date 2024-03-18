import datetime
import time
from Table import time_for_lessons, TimeTable, r

def now_lesson():
    tm = time.time()

    kol = 0
    k = 0
    
    now_weekday = datetime.datetime.now().weekday()

    if now_weekday in [1, 5]:
        k = 1
    elif now_weekday in [6]:
        k = 2
    elif now_weekday in [7]:
        k = 3

    ok = 0

    for i in time_for_lessons[k]:
        kol += 1
        if tm >= i[0] and tm < i[1]:
            ok = kol+1

    if ok == 0:
        return r
    else:
        return TimeTable[now_weekday][ok]

if __name__ == '__main__':
    print(now_lesson())
