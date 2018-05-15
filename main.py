from queue import Queue, PriorityQueue
from threading import Thread, Lock
import time
# class

def do_stuff(q):
    while True:
        # print(q.get()[1])
        time.sleep(0.1)
        q.task_done()


q = Queue(maxsize=0)
pq = PriorityQueue(maxsize=0)
num_threads = 5



for x in range(1000):
      pq.put((x%5,x))


for i in range(num_threads):
      worker = Thread(target=do_stuff, args=(pq,))
      worker.setDaemon(True)
      worker.start()

class task_manager:
    def __init__(self, num_threads = 1):
        self.locker_tasks = Lock()
        self.tasks = {}
        # task : func, arg_tuple, answer(None)
        self.last_id=-1
        self.queue = PriorityQueue(maxsize=0)
        self.num_threads = num_threads

    def do_stuff(self):
        while True:
            time.sleep(0.1)
            self.do_task(self.queue.get()[1]) #0: priority, 1: id
            self.queue.task_done()

    def do_task(self,id):
        """"""
        self.locker_tasks:
            f=self.tasks[id]['function']
            args=self.tasks[id]['args']
            self.tasks[id]['answer'] = f(*args)

    def add_task(self, f, args):
        self.last_id+=1
        self.locker_tasks:
            self.tasks[self.last_id] = {'function': f, 'args' : args, 'answer' : None}
        return self.last_id

    def get_result(self,id):
        while self.tasks[id] is None:
            time.sleep(0.1)
        return self.tasks[id]['answer']



def ma_fonction_qui_veut_une_reponse(p,item):
    id = waiter_team_instance.add_task(.....)
    waiter_team_instance.get_result(id)
wait_for_answer(2,5)

pq.join()



# (priority_number, data)
