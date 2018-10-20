import math
'''num=input("Length of a the longest sequence: " #521
N= input("Total amount in the database: ") #67,061
n= input("Length of a given sequence: ") #231
sigma= input("test of sigma") #.322
Lamdba= input("test of lambda")
'''
insert_var_name=0.00
e_value=2*pow(math.e,-57)
N=67061
n=231
n1=211 
gap=2.0/211
min_num= math.log(e_value)
lambda1=.322
lambda2=.267
sigma=43.6
alpha1=.792
alpha2=1.90
a1=min_num*alpha1
a2=min_num*alpha2*gap
dista=a1**2 - a2**2
sigmaa=math.sqrt(abs(dista))
max_num= gap*lambda2*min_num 
replay_min_num= min_num*lambda1
dist1=max_num**2-replay_min_num**2
sigmax=math.sqrt(abs(dist1))
'''
print(min_num)
print(max_num)
'''
print(sigmax)
print(sigmaa)
print(sigmax*sigmaa*2/231)
#print(sigma*neonnum)
e_value1=1*pow(math.e,-57)
'''
n1=215
gaps=2.0/211
min_num1= e_value1*N/n1
re_min_num= min_num1*lambda1*alpha1
man_num=gaps*lambda2*alpha2*e_value
dist2=man_num-re_min_num
newnum= math.sqrt(dist1**2+dist2**2)
#print(newnum)
insert_new_var=(newnum*sigma)
#print(insert_new_var)
new_nums = math.sqrt(((dist2)**2)+((dist2)**2))
if (new_nums < newnum):
    insert_var_name=new_nums*sigma
#    print(insert_var_name)
else:
    print("there is no number")
another_variable= insert_var_name - insert_new_var
print(math.log(abs(another_variable)))
'''
