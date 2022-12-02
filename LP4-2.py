def main():
  weight = int(input("Enter Package weight in killograms: "))
  length = int(input("Enter Package length in centimeters: "))
  width = int(input("Enter Package width in centimeters: "))
  height = int(input("Enter Package height in centimeters: "))
  total = length * width * height 
  
  if weight >= 32 and total < 100000:
    print("Too Heavy")
  if weight < 32 and total > 100000:
    print("Too Large")
  if weight >= 32 and total > 100000:
    print("Too Heavy and Too Large")
  if weight < 32 and total < 100000:
    print(weight)
    print(total)
  pass


if __name__=="__main__":
  main()