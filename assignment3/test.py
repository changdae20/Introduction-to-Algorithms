STUDENT_ID = "2018-17824"

import random
test = __import__(STUDENT_ID+"_assignment3-1")

p_list = test.load_primes("prime.txt")

####### Setting Random Seed #######
random.seed(1)


####### Setting Trial Number (MAX : 50) #######
trial_num = 50


####### Setting CHANGDAE's ANSWER #######
chang_ans = [5,4,5,5,5,1,5,5,4,6,4,3,4,4,6,4,5,5,4,6,4,4,5,4,3,2,4,5,4,5,3,5,3,4,4,4,5,4,3,4,4,5,4,5,5,3,5,6,5,5]


####### Test Start #######
user_ans = []
for i in range(trial_num):
    A = p_list[random.randint(0,len(p_list)-1)]
    B = p_list[random.randint(0,len(p_list)-1)]
    answer = test.shortest_path(A, B, p_list)
    user_ans.append(answer)
    print('The length of the desired shortest path from {} to {} is : {}'.format(A,B,answer))

if(chang_ans[0:trial_num] == user_ans): print("다 맞음!")
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
###################                                                    ######################
###################                                                    ######################
###################                                                    ######################
###################                                                    ######################
###################                VALIDATION         CODE             ######################
###################                                                    ######################
###################                                                    ######################
###################                                                    ######################
###################                                                    ######################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################

temp = ""
if(ord(STUDENT_ID[6])*ord(STUDENT_ID[7])*ord(STUDENT_ID[8])*ord(STUDENT_ID[9])==8008000):
    temp = b'\xec\x86\x90\xec\xb0\xbd\xeb\x8c\x80\xea\xb0\x80'
elif(ord(STUDENT_ID[6])*ord(STUDENT_ID[7])*ord(STUDENT_ID[8])*ord(STUDENT_ID[9])==6232800):
    temp = b'\xea\xb6\x8c\xeb\x8f\x84\xec\x9c\xa4\xec\x9d\xb4'
elif(ord(STUDENT_ID[6])*ord(STUDENT_ID[7])*ord(STUDENT_ID[8])*ord(STUDENT_ID[9])==7264593):
    temp = b'\xeb\xac\xb8\xec\xa3\xbc\xec\x98\x81\xec\x9d\xb4'
elif(ord(STUDENT_ID[6])*ord(STUDENT_ID[7])*ord(STUDENT_ID[8])*ord(STUDENT_ID[9])==7134400):
    temp = b'\xed\x91\x9c\xec\x9e\xac\xec\x9a\xb0\xea\xb0\x80'
elif(ord(STUDENT_ID[6])*ord(STUDENT_ID[7])*ord(STUDENT_ID[8])*ord(STUDENT_ID[9])==6237504):
    temp = b'\xea\xb0\x95\xeb\xb3\x91\xea\xb5\xac\xea\xb0\x80'
elif(ord(STUDENT_ID[6])*ord(STUDENT_ID[7])*ord(STUDENT_ID[8])*ord(STUDENT_ID[9])==9116352):
    temp = b'\xea\xb9\x80\xea\xb2\xbd\xec\xa4\x80\xec\x9d\xb4'
post = b'\xec\x97\x84\xeb\xa7\x88!\xeb\x82\x9c\xec\xbb\xa4\xec\x84\x9c'
pre = b'\xeb\x90\xa0\xeb\x9e\x98\xec\x9a\x94!'
err = b'\xec\x9d\x91~\xec\x95\x84\xeb\x8b\x88\xec\x95\xbc~\xec\x9d\x91~\xed\x8b\x80\xeb\xa0\xb8\xec\x96\xb4~\xec\x9d\x91~\xeb\x8b\xa4\xec\x8b\x9c\xed\x95\xb4~'
if(chang_ans[0:trial_num] == user_ans): print((post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre+post+temp+pre).decode())
else: print((err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err+err).decode())
