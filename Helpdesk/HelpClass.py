'''
Created on 2020/12/01

@author: Masaya Misaizu
'''
import redis
import uuid
import secrets
import string
from pip._internal.cli.cmdoptions import retries
from _datetime import datetime
from time import strftime

class HClass:
    
    def __init__(self):
        redis_host = "192.168.0.137"
        redis_port = 6379
        redis_password = "student"
        self.r = redis.StrictRedis(host=redis_host, port=redis_port,
                                   password=redis_password, decode_responses=True)
        
    def setEmp(self,email):
        self.r.sadd('set_employees',email)
        
    def remEmp(self,email):
        self.r.srem('set_employees',email)
        
    def listEmp(self):
        return self.r.smembers('set_employees')
        
    def setManager(self,email):
        if self.r.sismember('set_employees', email):
            self.r.set('e_manager',email)
    
    def getManager(self):
        return self.r.get('e_manager')
        

    def newTask(self,email,task_name):
        id=self.r.incr('id')
        priority = 0
        record_time=datetime.now().strftime("%Y%m%d%H%M%S")
#         self.r.hset('new_task_id'+str(id),str(id),task_name,record_time,priority,email)
        self.r.hmset('new_task_id'+str(id), 
            {'id':str(id),
             'task_name':task_name,
             'record_time':record_time,
             'priority':priority,
             'assigned_employee':email,
             'assigner_employee':email,
             'manager':email})
        return id

    def getTask(self,id):
        return self.r.hgetall('new_task_id'+id)    
        
        
    def changePri(self,email,id,priority):
        if email == self.r.get('e_manager'):
            self.r.hset('new_task_id'+id, 'priority', priority)
            
    def assignTask(self,id,assigned,assigner):
        self.hset('new_task_id'+id,'assigned_employee',assigned)
        self.hset('new_task_id'+id,'assigner_employee',assigner)
    