def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()

# finally block is always executed, even if there is an exception
# regardless of whether an exception occurs or not
# if used only print without finally, it will not execute if there is an exception, or if the function returns
