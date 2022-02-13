def Start():
    print("Welcome to Daniel Hamen's Python Converter!\n\nTo start, please Read and Accept the Terms and Conditions/License (Type \"?\" to read the Terms and Conditions/License). Type:\n\"Y\" to Accept\n\"N\" to Decline\n\"?\" to view Terms and Conditions/License")

    Accept = str(input("\n\n>>> ")).lower()

    if Accept == "y":
        pass

    elif Accept == "?":
        TermsAndConditions = open(r"lib\TermsAndCondition.txt", "r")
        print(str(TermsAndConditions.read()))
        TermsAndConditions.close()

        print(str("_"*50) + "\n\nAlso understand that this should not be used for big commercial projects as like most other scripts, there are bugs. If you do choose to use this for commercial projects, please use at your own risk!\n\n\nIf you do not want to read all the GNU License info, here is a summary by GitHub.com:")
        print("""
Permissions:
  - Commercial use
  - Modification
  - Distribution
  - Patent use
  - Private use

Limitations:
  - Liability
  - Warranty

Conditions:
  - License and copyright notice
  - State changes
  - Disclose source
  - Same license
        """)

        Accept_ = str(input("Do you accept (Y/N)?: ")).lower()

        if Accept_ == "y":
            pass
        else:
            print("\n\nYou must accept the terms and conditions before starting!\n\nPress any key to exit...")

            Exit = input()
            exit()
        pass
    else:
        print("\n\nYou must accept the terms and conditions before starting!\n\nPress any key to exit...")

        Exit = input()
        exit()
    
    try:
        import os
        from Convert import Conversions
        from Convert import GetUnits
        from lib.ConversionEquations import Equations
        from lib.ConversionTypes import Types
        from lib.ConversionVariants import Variants
        from lib.Errors import ConversionTypeError
        from lib.Errors import NotConvertedError
    except Exception as Except:
        print("Error while importing. Please read \"Log.txt\" to view the Error, or add a New Issue on GitHub in this Repository.")
        Log = open("Math\Log.txt", "w")
        Log.write(str(Except))
        Log.close()
        Exit = input("\n\nPress any key to continue...")
        exit()

    os.system("cls")

    InputStartValue = input("What is the start value: ")
    try:
        float(InputStartValue)
    except:
        print("Error while converting \"InputStartValue\" to float. Please read \"Log.txt\" to view the Error, or add a New Issue on GitHub in this Repository.")
        Log = open(r"Log.txt", "w")
        Log.write(str(Except))
        Log.close()
        Exit = input("\n\nPress any key to continue...")
        exit()

    InputStartUnit = str(input("What is the start unit (To view all units, type \"?\"): "))
    if str(InputStartUnit) == "?":
        print("\nUnits:")
        GetUnits(False)
        InputStartUnit = str(input("Enter the start unit: "))

    InputEndUnit = str(input(f"What would you like to convert {InputStartValue} {InputStartUnit}(s) to (End-Unit): "))

    C = Conversions(InputStartUnit, InputStartValue, InputEndUnit)
    C.Convert()
    C.Summarize()
    print(C.Summary)

    print("\n\nType:\n\t\"0\" to re-start the script\n\t\"1\" to exit the script")
    Portal = input(">>> ")

    if str(Portal) == "0":
        os.system("cls")
        Start()

    else:
        exit()

if __name__ == '__main__':
    Start()
