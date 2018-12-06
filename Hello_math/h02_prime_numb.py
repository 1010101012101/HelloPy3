import numpy as np


"""
prim = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
        101,103,107,109,113,
prims = [
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        [211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
        [307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]
        [401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
        [503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599]
        [601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691]
        [701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797]
        [809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887]
        [907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        ]

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


1.求小于2x3的质数：(3)
            准质数：()
            
2x3=6 ==>  1,(2x3),5
                6x0=0-----------0
                6x0+1=1
                6x0+5=5
                                                小于2x3质数：3     

2.求小于2x3x5的质数： 10
            准质数：5x(4-2) + 2 -1 
2x3=6 ==>  1,(2x3),5
                6x0=0-----------0
                6x0+1=1
                6x0+5=5
                6x1=6-----------1
                6x1+1=7
                6x1+5=11
                6x2=12-----------2
                6x2+1=13
                6x2+5=17
                6x3=18-----------3
                6x3+1=19
                6x3+5=23
                6x4=24-----------4
                6x4+1=25  (5x5)
                6x4+5=29
                6x5=30=2x3x5-----------5

2.求小于2x3x5x7的质数：  46
                准质数：7x8-1
2x3x5=30  ==>   1,(2x3x5),7,11,13,17,19,23,29   
                                                当前阶乘数：3
                                                小于2x3质数：3
                                                小于2x3x5=30的质数：10
                                                4x3-1
                30x0=0-----------0
                30x0+1=1
                30x0+7=7
                30x0+11=11
                30x0+13=13
                30x0+17=17
                30x0+19=19
                30x0+23=23
                30x0+29=29
                30x1=30-----------1
                30x1+1=31
                30x1+7=37
                30x1+11=41
                30x1+13=43
                30x1+17=47
                30x1+19=49  (7x7)
                30x1+23=53
                30x1+29=59
                30x2=60------------2
                30x2+1=61
                30x2+7=67
                30x2+11=71
                30x2+13=73
                30x2+17=77  (7x11)
                30x2+19=79
                30x2+23=83
                30x2+29=89
                30x3=90------------3
                30x3+1 = 91 (7x13)
                30x3+7=97
                30x3+11=101
                30x3+13=103
                30x3+17=107
                30x3+19=109
                30x3+23=113
                30x3+29=119 (7x17)
                30x4=120------------4
                30x4+1=121  (11x11)
                30x4+7=127
                30x4+11=131
                30x4+13=133  (7x19)
                30x4+17=137
                30x4+19=139
                30x4+23=143  (11x13)
                30x4+29=149
                30x5=150------------5
                30x5+1=151
                30x5+7=157
                30x5+11=161  (7x23)
                30x5+13=163
                30x5+17=167
                30x5+19=169  (13x13)
                30x5+23=173
                30x5+29=179
                30x6=130------------6
                30x6+1=181
                30x6+7=187  (11x17)
                30x6+11=191
                30x6+13=193
                30x6+17=197
                30x6+19=199
                30x6+23=203  (7x29)
                30x6+29=209  (11x19)
                30x7=210=2x3x5x7------------7

求小于2x3x5x7x11质数：343   
2x3x5x7=210  ==>    1,(2x3x5x7),11,13,17,19,23,29,|31,37,41,43,47,(49=7x7),53,59,|61,67,71,73,(77=7x11),79,83,89,
                    |(91=7x13),97,101,103,107,109,113,(119=7x17),|(121=11x11),127,131,(133=7x19),137,139,(143=11x13),
                    149,|151,157,(161=7x23),163,167,(169=13x13),173,179,|181,(187=11x17),191,193,197,199,(203=7x29),
                    (209=11x19)
                    
                    小于2x3x5x7 准质数：48    7*(7+1)=48
                                质数：36
                    小于2x3x5x7质数：46
                210*1=210------------1
                210*1+1=211
                210*1+11=221 (13x17)
                210*1+13=223
                210*1+17=227
                210*1+19=229
                210*1+23=233
                210*1+29=239
                210*1+31=241
                210*1+37=247
                210*1+41=251
                210*1+47=257
                210*1+(49)=259 (7*37)
                210*1+53=263
                210*1+59=269
                210*1+61=271
                210*1+67=273
                210*1+71=281
                210*1+73=283
                210*1+79=289 (17*17)
                210*1+83=293 
                210*1+89=299 (13*23)
                210*1+97=307
                210*1+101=311
                210*1+103=313
                210*1+107=317
                210*1+109=319  (11*29)
                210*1+113=323  (17*19)
                210*1+119=329   (7*47)
                210*1+(121)=331 ========
                210*1+127=337
                210*1+131=341    (11*31)
                210*1+(133)=343  (7*7*7)
                210*1+137
                210*1+139
                210*1+149
                210*1+151
                210*1+157
                210*1+163
                210*1+167
                210*1+173
                210*1+179
                210*1+181
                210*1+191
                210*1+193
                210*1+197
                210*1+199
                210*2=420------------
                

求小于2x3x5x7x11x13质数：3248
2x3x5x7x11 = 2310    猜测：2x3x5x7~2x3x5x7x11之间的准质数：(11-1)*(48+7-4)=120个
                    小于2x3x5x7x11质数：343
                    小于2x3x5x7x11准质数：11*46
            
11, 7, 5, 3, 2, 1
          1  0  0       -------2
       1  0  0  0        ------6
    1  0  0  0  0        ------30
G, F, E, D, C, B, A
         210, 30, 6, 2, 1
                        1   1
                     1  0   2
                     1  1   3
                  1  0  1   7
               1, 1, 0, 1 ------
"""

def approximate(m):
    for i in range(2,m):
        if m/i == 0:
            print(m)
            break


def prim_num(max, min = 2):
    prims=[]
    for i in range(min, max):
        is_prim = True
        for j in range(2, i):
            #print("i=",i,"j=",j,"i%%j=",i%j)
            if i%j == 0:
                is_prim = False
                break
        if is_prim == True:
            prims.append(i)

    print(prims)
    return prims

def diff_neighbor(max=210, min=2):
    prims = prim_num(max, min)
    litt_prim = 0
    d = []
    for big_prim in prims:
        if litt_prim == 0:
            litt_prim = big_prim
            continue
        d.append(big_prim - litt_prim)
        print(big_prim,"-", litt_prim,"=",big_prim - litt_prim )
        litt_prim = big_prim

    return d


def diff_neighbor_test():
    print(diff_neighbor())


def prim_num_test():
    prim_num(100)
    prim_num(200, 100)
    prim_num(300, 200)
    prim_num(400, 300)
    prim_num(500, 400)
    prim_num(600, 500)
    prim_num(700, 600)
    # prim_num(800, 700)
    # prim_num(900, 800)
    # prim_num(1000, 900)
    #prims=prim_num(2*3*5*7*11*13)
    #print(len(prims))

if __name__ == "__main__":
    prim_num_test()
    approximate(209)
    #diff_neighbor_test()
