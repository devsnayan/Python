ap = 80
a = 70
b = 60
c = 50
d = 40
e = 33

def fun_marking(subject, mark):
  if mark >= ap:
    print(f'Your subjet is {subject} & LPA is {mark} and you got A+')

  elif mark >= a:
    print(f'Your subjet is {subject} & LPA is {mark} and you got A')

  elif mark >= b:
    print(f'Your subjet is {subject} & LPA is {mark} and you got B')

  elif mark >= c:
    print(f'Your subjet is {subject} & LPA is {mark} and you got C')

  elif mark >= d:
    print(f'Your subjet is {subject} & LPA is {mark} and you got D')

  elif mark >= e:
    print(f'Your subjet is {subject} & LPA is {mark} and you got E')

  else:
    print(f'Your subjet is {subject} & LPA is {mark} and you got F')

bangla = fun_marking(subject = "Bangla", mark =  int(input("Bangla: ")))
english = fun_marking(subject = "English", mark =  int(input("English: ")))
math = fun_marking(subject = "Math", mark =  int(input("Math: ")))