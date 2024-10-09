class Solution:
    def areSentencesSimilar(self, sen1: str, sen2: str) -> bool:
        if sen1 == sen2:return True
        st = [True]
        sen1 , sen2 = sen1.split(),sen2.split()
        n , m = len(sen1) , len(sen2)
        fP , sP =  0 , 0
        while fP < len(sen1) and sP < len(sen2):
            if sen1[fP] == sen2[sP]:
                if st[-1] != True:
                    st.append(True)
                sP , fP = sP + 1, fP + 1
            else:
                if st[-1] != False:
                    st.append(False)
                if len(sen1) > len(sen2):
                    fP += 1
                else:
                    sP += 1
        if sP < len(sen2) or fP < len(sen1):
            st.append(False)
        st1 = [True]
        f , s = len(sen1) - 1, len(sen2) - 1
        while f > -1 and s > -1:
            if sen1[f] == sen2[s]:
                if st1[-1] != True:
                    st1.append(True)
                s , f = s - 1, f - 1
            else:
                if st1[-1] != False:
                    st1.append(False)
                if len(sen1) > len(sen2):
                    f -= 1
                else:
                    s -= 1
        if f > -1 or s > -1:st1.append(False)
        count1 , count2 = 0 , 0
        for bol in st:
            if not bol:
                count1 += 1
                if count1 == 2:
                    break
        for bol in st1:
            if not bol:
                count2 += 1
                if count2 == 2:
                    break
        print(count1,count2, (n,m))
        return (count1 < 2 and n != m ) or (count2 < 2 and n != m)

            
                
            
            
