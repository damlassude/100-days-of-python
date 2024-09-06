def calculate_love_score(name1,name2):
    name1=name1.lower()
    name2=name2.lower()
    letter_count1=0
    letter_count2=0
    for letter in name1:
        for i in "true":
            if letter==i:
                letter_count1+=1
    
    for letter3 in name2:
        for k in "true":
            if letter3==k:
                letter_count1+=1
        
    for letter2 in name1:
        for n in "love":
            if letter2==n:
                letter_count2+=1
    
    for letter4 in name2:
        for m in "love":
            if letter4==m:
                letter_count2+=1
    
    print(str(letter_count1)+str(letter_count2))
        
        
x=input("Name 1: ")
y=input("Name 2: ")
calculate_love_score(x,y)