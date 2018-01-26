
# coding: utf-8

# In[1]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'constants.ipynb'])

P = 6.0e+00 * 0.101325e+06
KB = 1.38064852e-23


