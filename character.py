def count_characters(s):    
    count={}
    for i in s: 
        if i in count:  
            count[i]+=1
        else:   
            count[i]=1      
        print(count)
word=input('enter your word:')
print(count_characters(word))

            