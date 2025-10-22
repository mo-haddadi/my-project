#  شمارش تعداد حروف یک کلمه و تعداد تکرار هر حرف

word = input("Enter the word:")
print("total number of letters:", len(word))
print('the number of frequency of every letter:')
printed = ''
for i in word:
    if i not in printed:
        print(i , ':', word.count(i))
        printed = printed + i
      
      
      
      
      
      
    