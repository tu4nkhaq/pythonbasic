def converter():
    C=int(input("Nhap do C can chuyen:"))
    if C:
        CtoF=9*C/5+32
        print(f"C degree to F: {CtoF} ")
    else:
        print("plese enter repeat that")
def main():
    converter()
if __name__=="__main__":
    main()
