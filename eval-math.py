def main():
    while 1:
        try:
            a=input(">")
            b=input(">")
            operator=input(">")
            if operator in ["+","-",'*','/','%','//','**']:
                result=eval(f"{a}{operator}{b}")
                print(result)
            else:
                print("Error")
            confirm=input("yes/no?").lower()
            if confirm=="no":
                break
        except Exception as e:
            print(e)
if __name__=="__main__":
    main()

