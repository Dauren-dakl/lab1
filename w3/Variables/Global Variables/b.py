# Если вы используете globalключевое слово, переменная принадлежит глобальной области видимости:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)