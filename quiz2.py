Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str('42')
'42'
str(42)
'42'

#problem 6
int("Sunshine")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Sunshine")
ValueError: invalid literal for int() with base 10: 'Sunshine'

#answer: It has an error because 'sunshine' is a string, and cannot be convert to integer. 