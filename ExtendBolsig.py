
# coding: utf-8

# In[3]:


import pandas as pd
import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'Extend_Bolsig.ipynb'])
#import sys
#sys.path.append('C:/Users/mtmr_member/Desktop/Scripts')
from constants import *

class extendBolsig:
    
    def __init__(self, T, fout_common):
        self.T = T
        self.fout_common = fout_common
        self.n_tot = P / (KB * T)
        
    def read_fra(self, str1):
        df_ = pd.read_table(self.fout_common+'(U)_'+str1+'.dat', 
                            delim_whitespace=True, skiprows=3, 
                            names=['Temperature', 'Density'], 
                            index_col='Temperature', engine='python')
        fra_ = df_['Density'][self.T] / self.n_tot
        return fra_, df_['Density'][self.T]
    
    def set_fra(self):
        self.fra_sf6, self.den_sf6 = self.read_fra('sf6')
        self.fra_sf5, self.den_sf5 = self.read_fra('sf5')
        self.fra_sf4, self.den_sf4 = self.read_fra('sf4')
        self.fra_sf3, self.den_sf3 = self.read_fra('sf3')
        self.fra_sf2, self.den_sf2 = self.read_fra('sf2')
        self.fra_sf, self.den_sf = self.read_fra('sf')
        self.fra_s2, self.den_s2 = self.read_fra('s2')
        self.fra_s, self.den_s = self.read_fra('s')
        self.fra_f2, self.den_f2 = self.read_fra('f2')
        self.fra_f, self.den_f = self.read_fra('f')
        self.fra_ssf2, self.den_ssf2 = self.read_fra('ssf2')
        self.fra_fssf, self.den_fssf = self.read_fra('fssf')
        self.fra_c, self.den_c = self.read_fra('c')
        self.fra_c2, self.den_c2 = self.read_fra('c2')
        self.fra_c3, self.den_c3 = self.read_fra('c3')
        self.fra_c4, self.den_c4 = self.read_fra('c4')
        self.fra_c5, self.den_c5 = self.read_fra('c5')
        self.fra_cf, self.den_cf = self.read_fra('cf')
        self.fra_cf2, self.den_cf2 = self.read_fra('cf2')
        self.fra_cf3, self.den_cf3 = self.read_fra('cf3')
        self.fra_cf4, self.den_cf4 = self.read_fra('cf4')
        self.fra_c2f2, self.den_c2f2 = self.read_fra('c2f2')
        self.fra_c2f4, self.den_c2f4 = self.read_fra('c2f4')
        self.fra_c2f6, self.den_c2f6 = self.read_fra('c2f6')
        self.fra_cs, self.den_cs = self.read_fra('cs')
        self.fra_cs2, self.den_cs2 = self.read_fra('cs2')
        self.fra_n, self.den_n = self.read_fra('n')
        self.fra_n2, self.den_n2 = self.read_fra('n2')
        self.fra_b, self.den_b = self.read_fra('b')
        self.fra_bf, self.den_bf = self.read_fra('bf')
        self.fra_bf2, self.den_bf2 = self.read_fra('bf2')
        self.fra_bf3, self.den_bf3 = self.read_fra('bf3')
        self.fra_nf, self.den_nf = self.read_fra('nf')
        self.fra_ns, self.den_ns = self.read_fra('ns')
        self.fra_cn, self.den_cn = self.read_fra('cn')
        self.fra_c2n, self.den_c2n = self.read_fra('c2n')
        self.fra_c2n2, self.den_c2n2 = self.read_fra('c2n2')
        self.fra_c4n2, self.den_c4n2 = self.read_fra('c4n2')
        self.fra_fcn, self.den_fcn = self.read_fra('fcn')

        self.fra_ele, self.den_ele = self.read_fra('e')

    def write_fra(self):
        fra_header = ['Species', 'Fraction']
        fra_list = [
            ['sf6', self.fra_sf6],
            ['sf5', self.fra_sf5],
            ['sf4', self.fra_sf4],
            ['sf3', self.fra_sf3],   
            ['sf2', self.fra_sf2],
            ['sf', self.fra_sf],
            ['s2', self.fra_s2],
            ['s', self.fra_s],
            ['f2', self.fra_f2],
            ['f', self.fra_f],
            ['ssf2', self.fra_ssf2],
            ['fssf', self.fra_fssf], 
            ['c', self.fra_c],
            ['c2', self.fra_c2],
            ['c3', self.fra_c3],
            ['c4', self.fra_c4],
            ['c5', self.fra_c5],
            ['cf', self.fra_cf],
            ['cf2', self.fra_cf2], 
            ['cf3', self.fra_cf3],
            ['cf4', self.fra_cf4],
            ['c2f2', self.fra_c2f2],
            ['c2f4', self.fra_c2f4],
            ['c2f6', self.fra_c2f6],
            ['cs', self.fra_cs],
            ['cs2', self.fra_cs2],
            ['n', self.fra_n],
            ['n2', self.fra_n2],
            ['b', self.fra_b],
            ['bf', self.fra_bf],
            ['bf2', self.fra_bf2],
            ['bf3', self.fra_bf3],
            ['nf', self.fra_nf],
            ['ns', self.fra_ns],
            ['cn', self.fra_cn],
            ['c2n', self.fra_c2n],
            ['c2n2', self.fra_c2n2],
            ['c4n2', self.fra_c4n2],
            ['fcn', self.fra_fcn],
            [' ', ' '],
            ['Ionization degree', self.fra_ele],
            ['Plaama density', self.den_ele]
        ]
    
        fra_df = pd.DataFrame(fra_list, columns=fra_header)
        fra_df.to_csv(self.fout_common+'_Fraction_' + str(int(self.T)) + 'K.csv')
    
    
    def read_k(self):
        self.df_k = pd.read_table(self.fout_common+'_Rate_coefficient_'+str(int(self.T))+'K.dat', 
                             delim_whitespace=True, skiprows=66, 
                             engine='python',
                             names=['R#', 'E/N', 'Energy', 
                                    'k_sf6_i', 'k_sf6_a', 'k_sf6_da1', 'k_sf6_da2', 'k_sf6_da3', 'k_sf6_da4', 
                                    'k_sf5_i', 'k_sf5_a', 
                                    'k_sf4_i', 'k_sf4_a',
                                    'k_sf3_i', 'k_sf3_a', 
                                    'k_sf2_i', 
                                    'k_sf_i', 
                                    'k_s2_i', 
                                    'k_s_i', 
                                    'k_f2_i', 'k_f2_da', 
                                    'k_f_i1', 'k_f_i2', 'k_f_i3', 'k_f_a', 
                                    'k_ssf2_i', 'k_ssf2_a', 
                                    'k_fssf_i', 'k_fssf_a',
                                    'k_c_i', 
                                    'k_c2_i', 
                                    'k_c3_i', 
                                    'k_cf_i', 'k_cf_da', 
                                    'k_cf2_i', 'k_cf2_da',
                                    'k_cf3_i', 
                                    'k_cf4_da1', 'k_cf4_da2', 'k_cf4_i1', 'k_cf4_i2', 'k_cf4_i3', 'k_cf4_i4', 'k_cf4_i5', 'k_cf4_i6', 'k_cf4_i7', 
                                    'k_c2f2_i', 'k_c2f2_da', 
                                    'k_c2f4_i1', 'k_c2f4_i2', 'k_c2f4_i3', 
                                    'k_c2f6_i1', 'k_c2f6_i2', 'k_c2f6_i3', 'k_c2f6_i4', 'k_c2f6_da1', 'k_c2f6_da2', 
                                    'k_cs_i',
                                    'k_cs2_i',
                                    'k_n_i',
                                    'k_n2_i',
                                    'k_b_i',
                                    'k_bf_i',
                                    'k_bf2_i',
                                    'k_bf3_i', 'k_bf3_da',
                                    'k_cn_i'
 
                                   ]
                             )
    
    def set_tau(self):
        self.df_tau = pd.DataFrame({'E/N': self.df_k['E/N'],
                                    'tau_sf6_i': self.df_k['k_sf6_i']*self.fra_sf6,
                                    'tau_sf6_a': self.df_k['k_sf6_a']*self.fra_sf6,
                                    'tau_sf6_da1': self.df_k['k_sf6_da1']*self.fra_sf6,
                                    'tau_sf6_da2': self.df_k['k_sf6_da2']*self.fra_sf6,
                                    'tau_sf6_da3': self.df_k['k_sf6_da3']*self.fra_sf6,
                                    'tau_sf6_da4': self.df_k['k_sf6_da4']*self.fra_sf6,
                                    'tau_sf5_i': self.df_k['k_sf5_i']*self.fra_sf5,
                                    'tau_sf5_a': self.df_k['k_sf5_a']*self.fra_sf5,
                                    'tau_sf4_i': self.df_k['k_sf4_i']*self.fra_sf4,
                                    'tau_sf4_a': self.df_k['k_sf4_a']*self.fra_sf4,
                                    'tau_sf3_i': self.df_k['k_sf3_i']*self.fra_sf3,
                                    'tau_sf3_a': self.df_k['k_sf3_a']*self.fra_sf3,
                                    'tau_sf2_i': self.df_k['k_sf2_i']*self.fra_sf2,
                                    'tau_sf_i': self.df_k['k_sf_i']*self.fra_sf,
                                    'tau_s2_i': self.df_k['k_s2_i']*self.fra_s2,
                                    'tau_s_i': self.df_k['k_s_i']*self.fra_s,
                                    'tau_f2_i': self.df_k['k_f2_i']*self.fra_f2,
                                    'tau_f2_da': self.df_k['k_f2_da']*self.fra_f2,
                                    'tau_f_i1': self.df_k['k_f_i1']*self.fra_f,
                                    'tau_f_i2': self.df_k['k_f_i2']*self.fra_f,
                                    'tau_f_i3': self.df_k['k_f_i3']*self.fra_f,
                                    'tau_f_a': self.df_k['k_f_a']*self.fra_f,
                                    'tau_ssf2_i': self.df_k['k_ssf2_i']*self.fra_ssf2,
                                    'tau_ssf2_a': self.df_k['k_ssf2_a']*self.fra_ssf2,
                                    'tau_fssf_i': self.df_k['k_fssf_i']*self.fra_fssf,
                                    'tau_fssf_a': self.df_k['k_fssf_a']*self.fra_fssf,
                                    'tau_c_i': self.df_k['k_c_i']*self.fra_c,
                                    'tau_c2_i': self.df_k['k_c2_i']*self.fra_c2,
                                    'tau_c3_i': self.df_k['k_c3_i']*self.fra_c3,
                                    'tau_cf_i': self.df_k['k_cf_i']*self.fra_cf,
                                    'tau_cf_da': self.df_k['k_cf_da']*self.fra_cf,
                                    'tau_cf2_i': self.df_k['k_cf2_i']*self.fra_cf2,
                                    'tau_cf2_da': self.df_k['k_cf2_da']*self.fra_cf2,
                                    'tau_cf3_i': self.df_k['k_cf3_i']*self.fra_cf3,
                                    'tau_cf4_da1': self.df_k['k_cf4_da1']*self.fra_cf4,
                                    'tau_cf4_da2': self.df_k['k_cf4_da2']*self.fra_cf4,
                                    'tau_cf4_i1': self.df_k['k_cf4_i1']*self.fra_cf4,
                                    'tau_cf4_i2': self.df_k['k_cf4_i2']*self.fra_cf4,
                                    'tau_cf4_i3': self.df_k['k_cf4_i3']*self.fra_cf4,
                                    'tau_cf4_i4': self.df_k['k_cf4_i4']*self.fra_cf4,
                                    'tau_cf4_i5': self.df_k['k_cf4_i5']*self.fra_cf4,
                                    'tau_cf4_i6': self.df_k['k_cf4_i6']*self.fra_cf4,
                                    'tau_cf4_i7': self.df_k['k_cf4_i7']*self.fra_cf4,
                                    'tau_c2f2_i': self.df_k['k_c2f2_i']*self.fra_c2f2,
                                    'tau_c2f2_da': self.df_k['k_c2f2_da']*self.fra_c2f2,
                                    'tau_c2f4_i1': self.df_k['k_c2f4_i1']*self.fra_c2f4,
                                    'tau_c2f4_i2': self.df_k['k_c2f4_i2']*self.fra_c2f4,
                                    'tau_c2f4_i3': self.df_k['k_c2f4_i3']*self.fra_c2f4,
                                    'tau_c2f6_i1': self.df_k['k_c2f6_i1']*self.fra_c2f6,
                                    'tau_c2f6_i2': self.df_k['k_c2f6_i2']*self.fra_c2f6,
                                    'tau_c2f6_i3': self.df_k['k_c2f6_i3']*self.fra_c2f6,
                                    'tau_c2f6_i4': self.df_k['k_c2f6_i4']*self.fra_c2f6,
                                    'tau_c2f6_da1': self.df_k['k_c2f6_da1']*self.fra_c2f6,
                                    'tau_c2f6_da2': self.df_k['k_c2f6_da2']*self.fra_c2f6,
                                    'tau_cs_i': self.df_k['k_cs_i']*self.fra_cs,
                                    'tau_cs2_i': self.df_k['k_cs2_i']*self.fra_cs2,
                                    'tau_n_i': self.df_k['k_n_i']*self.fra_n,
                                    'tau_n2_i': self.df_k['k_n2_i']*self.fra_n2,
                                    'tau_b_i': self.df_k['k_b_i']*self.fra_b,
                                    'tau_bf_i': self.df_k['k_bf_i']*self.fra_bf,
                                    'tau_bf2_i': self.df_k['k_bf2_i']*self.fra_bf2,
                                    'tau_bf3_i': self.df_k['k_bf3_i']*self.fra_bf3,
                                    'tau_bf3_da': self.df_k['k_bf3_da']*self.fra_bf3,
                                    'tau_cn_i': self.df_k['k_cn_i']*self.fra_cn               
                                   },
                                   columns = ['E/N', 
                                              'tau_sf6_i', 'tau_sf6_a', 'tau_sf6_da1', 'tau_sf6_da2', 'tau_sf6_da3', 'tau_sf6_da4',
                                              'tau_sf5_i', 'tau_sf5_a', 
                                              'tau_sf4_i', 'tau_sf4_a', 
                                              'tau_sf3_i', 'tau_sf3_a', 
                                              'tau_sf2_i', 
                                              'tau_sf_i',
                                              'tau_s2_i',
                                              'tau_s_i',
                                              'tau_f2_i', 'tau_f2_da', 
                                              'tau_f_i1', 'tau_f_i2', 'tau_f_i3', 'tau_f_a', 
                                              'tau_ssf2_i', 'tau_ssf2_a', 
                                              'tau_fssf_i', 'tau_fssf_a', 
                                              'tau_c_i', 
                                              'tau_c2_i', 
                                              'tau_c3_i', 
                                              'tau_cf_i', 'tau_cf_da', 
                                              'tau_cf2_i', 'tau_cf2_da', 
                                              'tau_cf3_i', 
                                              'tau_cf4_da1', 'tau_cf4_da2', 'tau_cf4_i1', 'tau_cf4_i2', 'tau_cf4_i3', 'tau_cf4_i4', 'tau_cf4_i5', 'tau_cf4_i6', 'tau_cf4_i7', 
                                              'tau_c2f2_i', 'tau_c2f2_da', 
                                              'tau_c2f4_i1', 'tau_c2f4_i2', 'tau_c2f4_i3',
                                              'tau_c2f6_i1', 'tau_c2f6_i2', 'tau_c2f6_i3', 'tau_c2f6_i4', 'tau_c2f6_da1', 'tau_c2f6_da2',
                                              'tau_cs_i', 
                                              'tau_cs2_i', 
                                              'tau_n_i', 
                                              'tau_n2_i', 
                                              'tau_b_i', 
                                              'tau_bf_i', 
                                              'tau_bf2_i', 
                                              'tau_bf3_i', 'tau_bf3_da',
                                              'tau_cn_i']
                                  )
        
    def write_tau(self):
        self.df_tau.to_csv(self.fout_common+'_Collision_frequency_'+str(int(self.T))+'K.csv')
        self.df_tau.to_csv(self.fout_common+'_Collision_frequency_'+str(int(self.T))+'K.dat', sep='\t')
        
    def set_muE(self):
        self.df_tran = pd.read_table(self.fout_common+'_Transport_coefficient_'+str(int(self.T))+'K.dat', 
                                     delim_whitespace=True, skiprows=22, 
                                     engine='python', header=None)
        
        self.df_muE = pd.DataFrame({ 'E/N': self.df_tran[1],
                                     'mu*N': self.df_tran[3],
                                     'mu*E': self.df_tran[1]*self.df_tran[3]*1.0e-21
                                   },
                                   columns = ['E/N', 'mu*N', 'mu*E']
                                  )
        
    
    def set_alpha_eta(self):
        self.df_alpha_eta = pd.DataFrame({'E/N': self.df_k['E/N'],
                                          'alpha_sf6_i': self.df_k['k_sf6_i']/self.df_muE['mu*E'],
                                          'eta_sf6_a': self.df_k['k_sf6_a']/self.df_muE['mu*E'],
                                          'eta_sf6_da1': self.df_k['k_sf6_da1']/self.df_muE['mu*E'],
                                          'eta_sf6_da2': self.df_k['k_sf6_da2']/self.df_muE['mu*E'],
                                          'eta_sf6_da3': self.df_k['k_sf6_da3']/self.df_muE['mu*E'],
                                          'eta_sf6_da4': self.df_k['k_sf6_da4']/self.df_muE['mu*E'],
                                          'alpha_sf5_i': self.df_k['k_sf5_i']/self.df_muE['mu*E'],
                                          'eta_sf5_a': self.df_k['k_sf5_a']/self.df_muE['mu*E'],
                                          'alpha_sf4_i': self.df_k['k_sf4_i']/self.df_muE['mu*E'],
                                          'eta_sf4_a': self.df_k['k_sf4_a']/self.df_muE['mu*E'],
                                          'alpha_sf3_i': self.df_k['k_sf3_i']/self.df_muE['mu*E'],
                                          'eta_sf3_a': self.df_k['k_sf3_a']/self.df_muE['mu*E'],
                                          'alpha_sf2_i': self.df_k['k_sf2_i']/self.df_muE['mu*E'],
                                          'alpha_sf_i': self.df_k['k_sf_i']/self.df_muE['mu*E'],
                                          'alpha_s2_i': self.df_k['k_s2_i']/self.df_muE['mu*E'],
                                          'alpha_s_i': self.df_k['k_s_i']/self.df_muE['mu*E'],
                                          'alpha_f2_i': self.df_k['k_f2_i']/self.df_muE['mu*E'],
                                          'eta_f2_da': self.df_k['k_f2_da']/self.df_muE['mu*E'],
                                          'alpha_f_i1': self.df_k['k_f_i1']/self.df_muE['mu*E'],
                                          'alpha_f_i2': self.df_k['k_f_i2']/self.df_muE['mu*E'],
                                          'alpha_f_i3': self.df_k['k_f_i3']/self.df_muE['mu*E'],
                                          'eta_f_a': self.df_k['k_f_a']/self.df_muE['mu*E'],
                                          'alpha_ssf2_i': self.df_k['k_ssf2_i']/self.df_muE['mu*E'],
                                          'eta_ssf2_a': self.df_k['k_ssf2_a']/self.df_muE['mu*E'],
                                          'alpha_fssf_i': self.df_k['k_fssf_i']/self.df_muE['mu*E'],
                                          'eta_fssf_a': self.df_k['k_fssf_a']/self.df_muE['mu*E'],
                                          'alpha_c_i': self.df_k['k_c_i']/self.df_muE['mu*E'],
                                          'alpha_c2_i': self.df_k['k_c2_i']/self.df_muE['mu*E'],
                                          'alpha_c3_i': self.df_k['k_c3_i']/self.df_muE['mu*E'],
                                          'alpha_cf_i': self.df_k['k_cf_i']/self.df_muE['mu*E'],
                                          'eta_cf_da': self.df_k['k_cf_da']/self.df_muE['mu*E'],
                                          'alpha_cf2_i': self.df_k['k_cf2_i']/self.df_muE['mu*E'],
                                          'eta_cf2_da': self.df_k['k_cf2_da']/self.df_muE['mu*E'],
                                          'alpha_cf3_i': self.df_k['k_cf3_i']/self.df_muE['mu*E'],
                                          'eta_cf4_da1': self.df_k['k_cf4_da1']/self.df_muE['mu*E'],
                                          'eta_cf4_da2': self.df_k['k_cf4_da2']/self.df_muE['mu*E'],
                                          'alpha_cf4_i1': self.df_k['k_cf4_i1']/self.df_muE['mu*E'],
                                          'alpha_cf4_i2': self.df_k['k_cf4_i2']/self.df_muE['mu*E'],
                                          'alpha_cf4_i3': self.df_k['k_cf4_i3']/self.df_muE['mu*E'],
                                          'alpha_cf4_i4': self.df_k['k_cf4_i4']/self.df_muE['mu*E'],
                                          'alpha_cf4_i5': self.df_k['k_cf4_i5']/self.df_muE['mu*E'],
                                          'alpha_cf4_i6': self.df_k['k_cf4_i6']/self.df_muE['mu*E'],
                                          'alpha_cf4_i7': self.df_k['k_cf4_i7']/self.df_muE['mu*E'],
                                          'alpha_c2f2_i': self.df_k['k_c2f2_i']/self.df_muE['mu*E'],
                                          'eta_c2f2_da': self.df_k['k_c2f2_da']/self.df_muE['mu*E'],
                                          'alpha_c2f4_i1': self.df_k['k_c2f4_i1']/self.df_muE['mu*E'],
                                          'alpha_c2f4_i2': self.df_k['k_c2f4_i2']/self.df_muE['mu*E'],
                                          'alpha_c2f4_i3': self.df_k['k_c2f4_i3']/self.df_muE['mu*E'],
                                          'alpha_c2f6_i1': self.df_k['k_c2f6_i1']/self.df_muE['mu*E'],
                                          'alpha_c2f6_i2': self.df_k['k_c2f6_i2']/self.df_muE['mu*E'],
                                          'alpha_c2f6_i3': self.df_k['k_c2f6_i3']/self.df_muE['mu*E'],
                                          'alpha_c2f6_i4': self.df_k['k_c2f6_i4']/self.df_muE['mu*E'],
                                          'eta_c2f6_da1': self.df_k['k_c2f6_da1']/self.df_muE['mu*E'],
                                          'eta_c2f6_da2': self.df_k['k_c2f6_da2']/self.df_muE['mu*E'],
                                          'alpha_cs_i': self.df_k['k_cs_i']/self.df_muE['mu*E'],
                                          'alpha_cs2_i': self.df_k['k_cs2_i']/self.df_muE['mu*E'],
                                          'alpha_n_i': self.df_k['k_n_i']/self.df_muE['mu*E'],
                                          'alpha_n2_i': self.df_k['k_n2_i']/self.df_muE['mu*E'],
                                          'alpha_b_i': self.df_k['k_b_i']/self.df_muE['mu*E'],
                                          'alpha_bf_i': self.df_k['k_bf_i']/self.df_muE['mu*E'],
                                          'alpha_bf2_i': self.df_k['k_bf2_i']/self.df_muE['mu*E'],
                                          'alpha_bf3_i': self.df_k['k_bf3_i']/self.df_muE['mu*E'],
                                          'eta_bf3_da': self.df_k['k_bf3_da']/self.df_muE['mu*E'],
                                          'alpha_cn_i': self.df_k['k_cn_i']/self.df_muE['mu*E']              
                                         },
                                         columns = ['E/N', 
                                                    'alpha_sf6_i', 'eta_sf6_a', 'eta_sf6_da1', 'eta_sf6_da2', 'eta_sf6_da3', 'eta_sf6_da4',
                                                    'alpha_sf5_i', 'eta_sf5_a', 
                                                    'alpha_sf4_i', 'eta_sf4_a', 
                                                    'alpha_sf3_i', 'eta_sf3_a', 
                                                    'alpha_sf2_i', 
                                                    'alpha_sf_i',
                                                    'alpha_s2_i',
                                                    'alpha_s_i',
                                                    'alpha_f2_i', 'eta_f2_da', 
                                                    'alpha_f_i1', 'alpha_f_i2', 'alpha_f_i3', 'eta_f_a', 
                                                    'alpha_ssf2_i', 'eta_ssf2_a', 
                                                    'alpha_fssf_i', 'eta_fssf_a', 
                                                    'alpha_c_i', 
                                                    'alpha_c2_i', 
                                                    'alpha_c3_i', 
                                                    'alpha_cf_i', 'eta_cf_da', 
                                                    'alpha_cf2_i', 'eta_cf2_da', 
                                                    'alpha_cf3_i', 
                                                    'eta_cf4_da1', 'eta_cf4_da2', 'alpha_cf4_i1', 'alpha_cf4_i2', 'alpha_cf4_i3', 'alpha_cf4_i4', 'alpha_cf4_i5', 'alpha_cf4_i6', 'alpha_cf4_i7', 
                                                    'alpha_c2f2_i', 'eta_c2f2_da', 
                                                    'alpha_c2f4_i1', 'alpha_c2f4_i2', 'alpha_c2f4_i3',
                                                    'alpha_c2f6_i1', 'alpha_c2f6_i2', 'alpha_c2f6_i3', 'alpha_c2f6_i4', 'eta_c2f6_da1', 'eta_c2f6_da2',
                                                    'alpha_cs_i', 
                                                    'alpha_cs2_i', 
                                                    'alpha_n_i', 
                                                    'alpha_n2_i', 
                                                    'alpha_b_i', 
                                                    'alpha_bf_i', 
                                                    'alpha_bf2_i', 
                                                    'alpha_bf3_i', 'eta_bf3_da',
                                                    'alpha_cn_i']
                                          )
        
    def write_alpha_eta(self):
        self.df_alpha_eta.to_csv(self.fout_common+'_Ionization_and_Attachment_'+str(int(self.T))+'K.csv')
        self.df_alpha_eta.to_csv(self.fout_common+'_Ionization_and_Attachment_'+str(int(self.T))+'K.dat', sep='\t')

    def set_total_alpha_eta(self):
        self.df_total_alpha_eta = pd.DataFrame({'E/N': self.df_alpha_eta['E/N'],
                                                'Total alpha': 
                                                self.df_alpha_eta['alpha_sf6_i']*self.fra_sf6+
                                                self.df_alpha_eta['alpha_sf5_i']*self.fra_sf5+
                                                self.df_alpha_eta['alpha_sf4_i']*self.fra_sf4+
                                                self.df_alpha_eta['alpha_sf3_i']*self.fra_sf3+
                                                self.df_alpha_eta['alpha_sf2_i']*self.fra_sf2+
                                                self.df_alpha_eta['alpha_sf_i']*self.fra_sf+
                                                self.df_alpha_eta['alpha_s2_i']*self.fra_s2+
                                                self.df_alpha_eta['alpha_s_i']*self.fra_s+
                                                self.df_alpha_eta['alpha_f2_i']*self.fra_f2+
                                                self.df_alpha_eta['alpha_f_i1']*self.fra_f+
                                                self.df_alpha_eta['alpha_f_i2']*self.fra_f+
                                                self.df_alpha_eta['alpha_f_i3']*self.fra_f+
                                                self.df_alpha_eta['alpha_ssf2_i']*self.fra_ssf2+
                                                self.df_alpha_eta['alpha_fssf_i']*self.fra_fssf+
                                                self.df_alpha_eta['alpha_c_i']*self.fra_c+
                                                self.df_alpha_eta['alpha_c2_i']*self.fra_c2+
                                                self.df_alpha_eta['alpha_c3_i']*self.fra_c3+
                                                self.df_alpha_eta['alpha_cf_i']*self.fra_cf+
                                                self.df_alpha_eta['alpha_cf2_i']*self.fra_cf2+
                                                self.df_alpha_eta['alpha_cf3_i']*self.fra_cf3+
                                                self.df_alpha_eta['alpha_cf4_i1']*self.fra_cf4+
                                                self.df_alpha_eta['alpha_cf4_i2']*self.fra_cf4+
                                                self.df_alpha_eta['alpha_cf4_i3']*self.fra_cf4+
                                                self.df_alpha_eta['alpha_cf4_i4']*self.fra_cf4+
                                                self.df_alpha_eta['alpha_cf4_i5']*self.fra_cf4+
                                                self.df_alpha_eta['alpha_cf4_i6']*self.fra_cf4+
                                                self.df_alpha_eta['alpha_cf4_i7']*self.fra_cf4+
                                                self.df_alpha_eta['alpha_c2f2_i']*self.fra_c2f2+
                                                self.df_alpha_eta['alpha_c2f4_i1']*self.fra_c2f4+
                                                self.df_alpha_eta['alpha_c2f4_i2']*self.fra_c2f4+
                                                self.df_alpha_eta['alpha_c2f4_i3']*self.fra_c2f4+
                                                self.df_alpha_eta['alpha_c2f6_i1']*self.fra_c2f6+
                                                self.df_alpha_eta['alpha_c2f6_i2']*self.fra_c2f6+
                                                self.df_alpha_eta['alpha_c2f6_i3']*self.fra_c2f6+
                                                self.df_alpha_eta['alpha_c2f6_i4']*self.fra_c2f6+
                                                self.df_alpha_eta['alpha_cs_i']*self.fra_cs+
                                                self.df_alpha_eta['alpha_cs2_i']*self.fra_cs2+
                                                self.df_alpha_eta['alpha_n_i']*self.fra_n+
                                                self.df_alpha_eta['alpha_n2_i']*self.fra_n2+
                                                self.df_alpha_eta['alpha_b_i']*self.fra_b+
                                                self.df_alpha_eta['alpha_bf_i']*self.fra_bf+
                                                self.df_alpha_eta['alpha_bf2_i']*self.fra_bf2+
                                                self.df_alpha_eta['alpha_bf3_i']*self.fra_bf3+
                                                self.df_alpha_eta['alpha_cn_i']*self.fra_cn,
                                                'Total eta': 
                                                self.df_alpha_eta['eta_sf6_a']*self.fra_sf6+
                                                self.df_alpha_eta['eta_sf6_da1']*self.fra_sf6+
                                                self.df_alpha_eta['eta_sf6_da2']*self.fra_sf6+
                                                self.df_alpha_eta['eta_sf6_da3']*self.fra_sf6+
                                                self.df_alpha_eta['eta_sf6_da4']*self.fra_sf6+
                                                self.df_alpha_eta['eta_sf5_a']*self.fra_sf5+
                                                self.df_alpha_eta['eta_sf4_a']*self.fra_sf4+
                                                self.df_alpha_eta['eta_sf3_a']*self.fra_sf3+
                                                self.df_alpha_eta['eta_f2_da']*self.fra_f2+
                                                self.df_alpha_eta['eta_f_a']*self.fra_f+
                                                self.df_alpha_eta['eta_ssf2_a']*self.fra_ssf2+
                                                self.df_alpha_eta['eta_fssf_a']*self.fra_fssf+
                                                self.df_alpha_eta['eta_cf_da']*self.fra_cf+
                                                self.df_alpha_eta['eta_cf2_da']*self.fra_cf2+
                                                self.df_alpha_eta['eta_cf4_da1']*self.fra_cf4+
                                                self.df_alpha_eta['eta_cf4_da2']*self.fra_cf4+
                                                self.df_alpha_eta['eta_c2f2_da']*self.fra_c2f2+
                                                self.df_alpha_eta['eta_c2f6_da1']*self.fra_c2f6+
                                                self.df_alpha_eta['eta_c2f6_da2']*self.fra_c2f6+
                                                self.df_alpha_eta['eta_bf3_da']*self.fra_bf3
                                               },
                                               columns = ['E/N', 'Total alpha', 'Total eta']
                                              )
        
        self.df_total_alpha_eta_2 = pd.DataFrame({'E/N': self.df_total_alpha_eta['E/N'],
                                                 'Total alpha': self.df_total_alpha_eta['Total alpha'],
                                                 'Total eta': self.df_total_alpha_eta['Total eta'],
                                                 'Total effective': self.df_total_alpha_eta['Total alpha']-self.df_total_alpha_eta['Total eta']
                                                 },
                                                 columns = ['E/N', 'Total alpha', 'Total eta', 'Total effective']
                                                )
                                                 
    
    def write_total_alpha_eta(self):
        self.df_total_alpha_eta_2.to_csv(self.fout_common+'_Total_alpha_eta_'+str(int(self.T))+'K.csv')
        self.df_total_alpha_eta_2.to_csv(self.fout_common+'_Total_alpha_eta_'+str(int(self.T))+'K.dat', sep='\t')

        
    def cal_Ecr(self):
        for i in range(len(self.df_total_alpha_eta_2['E/N'])):
            if self.df_total_alpha_eta_2['Total effective'][i] >= 0:
                Ecr_Td = self.df_total_alpha_eta_2['E/N'][i]
                Ecr_Vm = Ecr_Td * self.n_tot * 1.0e-21
                break
        return Ecr_Td, Ecr_Vm
    
if __name__ == '__main__':
    print('Yes!')

