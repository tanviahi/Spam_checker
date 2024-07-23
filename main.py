data = None

try:
  with open('keywords.txt','r')as f:
    data = f.read()

except FileNotFoundError:
  print("file not found!")

# print(data)

def span_check(sentence, spam_list):
  for word in spam_list:
    if word in sentence:
      print('marked as spam!')
      return True

  print('the given sentence is safe')
  return False

x = span_check('hey there i am playing rummy', data.split(', '))
print(x)