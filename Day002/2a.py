"""Obsłuż wyjątek DivideByZero"""

suma = 3000
counter = 0
result = int()

try:
  result = suma // counter
except ZeroDivisionError:
  print("Dzielenie przez zero.")