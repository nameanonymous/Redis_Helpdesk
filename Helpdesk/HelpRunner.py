'''
Created on 2020/12/01

@author: Masaya Misaizu
'''
from HelpClass import HClass


hc=HClass()

hc.setEmp('masaya@misaizu')

print(hc.listEmp())

hc.setManager('masaya@misaizu')

print(hc.getManager())

hc.newTask('masaya@misaizu', 'GoodMorning')

print(hc.getTask('1'))

hc.changePri('masaya@misaizu', '1', 2)

hc.assignTask('1', 'kiyoko@misaizu','shizuru@0123')

print(hc.getTask('1'))
