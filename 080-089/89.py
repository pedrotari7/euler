romanNumeralMap = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
value = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}


def toRoman(n):
    result = ""
    for numeral in romanNumeralMap:
        while n >= value[numeral]:
            result += numeral
            n -= value[numeral]
    return result

def get_fake_num(num):

  risk = [key for key in value.keys() if len(key)==2]
  goods = [key for key in value.keys() if len(key)==1]

  total = 0

  for ele in risk:
    if num.count(ele)!=0:
      total += value[ele]
      num = num.replace(ele,'')

  for ele in goods:
    if num.count(ele)!=0:
      total+=value[ele]*num.count(ele)
      num = num.replace(ele,'')

  return total

with open('p089_roman.txt','r') as f:
  nums = f.read().split('\n')

result = 0

for num in nums:
  total = 0
  aux = get_fake_num(num)
  fake_num = toRoman(aux)

  result += len(num)-len(fake_num)

print result




