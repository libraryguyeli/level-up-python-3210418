def is_palindrome(text: str):
  text = text.lower()
  forwards = []
  backwards = []
  for char in text:
    if char.isalpha():
      forwards.append(char)
      backwards.insert(0, char)
  for_text = "".join(forwards)
  back_text = "".join(backwards)
  if for_text == back_text:
    return True
  else:
    return False
  
if __name__ == "__main__":
  print(is_palindrome("racecar")) # True
  print(is_palindrome("Level")) # True
  print(is_palindrome("Hello world")) # False
  print(is_palindrome("Go hang a salami, I’m a lasagna hog.")) # True