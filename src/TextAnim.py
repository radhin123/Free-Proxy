import time
import itertools
import threading
import sys

done = False
 
def animate():
    for c in itertools.cycle(['Starting', 'sTarting', 'stArting', 'staRting', 'starTing','startIng', 'startiNg', 'StartinG']):
        if done:
            break
        sys.stdout.write('\r ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('')

t = threading.Thread(target=animate)
t.start()

 
time.sleep(1)
done = True

print("")
print("░██████╗████████╗░█████╗░██████╗░████████╗██╗███╗░░██╗░██████╗░")
print("██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░")
print("╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░██║██╔██╗██║██║░░██╗░")
print("░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██║██║╚████║██║░░╚██╗")
print("██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝")
print("╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░")
