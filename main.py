
# coding: utf-8

# In[11]:


#coding: utf-8
import numpy as np
import pandas as pd
#import sys
#sys.path.append('C:/Users/mtmr_member/Desktop/Scripts')
import Extend_Bolsig
import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'main.ipynb'])

print('温度[K]は？')
T = input('>> ')
#T = 3000
T = float(T)

print('PTFE，BN 混合率は？(例: 040010)')
fout_change = input('>> ')
#fout_change = '040010'

f_dir = 'C:/Users/mtmr_member/Desktop/06sf6c2f4bn(m)' + fout_change + '/'
fout_common = f_dir + '06sf6c2f4bn(m)' + fout_change

eB = Extend_Bolsig.extendBolsig(T, fout_common)

#順番注意
eB.set_fra()
eB.write_fra()
eB.read_k()
eB.set_tau()
eB.write_tau()
eB.set_muE()
eB.set_alpha_eta()
eB.write_alpha_eta()
eB.set_total_alpha_eta()
eB.write_total_alpha_eta()

Ecr_Td, Ecr_Vm = eB.cal_Ecr()
print('Ecr(Td) : {0:9.5e}'.format(Ecr_Td))
print('Ecr(V/m): {0:9.5e}'.format(Ecr_Vm))
print('Done!')

