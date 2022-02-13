from lib.__init__ import *

def GetUnits(Return=False):
    """
    Returns a list of Units that can be used

    args:
        ```Return``` ```(bool)```: When ```False```, the script will ```print()``` the units, otherwise it will return it
    """

    LengthUnits = ["inch","foot","yard","mile","nanometer","micrometer","millimeter","meter","centimeter","kilometer"]
    Units = [LengthUnits]
    Titles = {
        "LengthUnits" : "Length: "
    }

    ReturnString = ""

    for i in range(0, len(Units)):
        for r in range(0, len(Units[i])):
            String = ((Units[i])[r])
            if len(String) < 6:
                String = (str(String).title()) + "\t\t:\t\"" + String + "\"\n"
            else:
                String = (str(String).title()) + "\t:\t\"" + String + "\"\n"
            ReturnString += String

    if Return is False:
        print(ReturnString)
    elif Return is True:
        return ReturnString

class Conversions:
    def __init__(self, StartUnit, StartValue, EndUnit):
        """
        Use the ```GetUnits()``` function (Not method) to view all units

        Arguments:
            ```StartUnit``` ```(str)```: The start Unit of the conversion

            ```StartValue``` ```(float | int)```: The start value of the conversion

            ```EndUnit``` ```(str)```: The end Unit of the conversion
        """

        self.StartUnit = str(StartUnit).lower()
        self.StartValue = StartValue
        self.EndUnit = str(EndUnit).lower()
        self.EndValue = None
        self.Type = ""
        self.Summary = ""

    def FixStrings(self):
        """
        Replaces words like "Milimetres" to the word "millimeter" for better results
        """

        ReplaceVariables = [self.StartUnit, self.EndUnit]
        ReplaceVariableNames = ["self.StartUnit", "self.EndUnit"]
        IterIndex = 0
        for Var in ReplaceVariables:
            Var = Variants.get(str(Var))
            exec(f"{str(ReplaceVariableNames[IterIndex])} = \"{str(Var)}\"")
            IterIndex += 1

    def SetType(self):
        """
        Sets the self.Type variable to the correct type of conversion (Eg. Length, etc) (Currently the script only supports Length, but hopefully in the future, it will have more!)
        """

        # Get the type for both "StartType" and "EndType", then assign
        StartType = Types.get(self.StartUnit)
        EndType = Types.get(self.EndUnit)

        # Checks that "StartType" and "EndType" have the same type to avoid cross-type conversions
        if StartType != EndType:
            raise ConversionTypeError(f"\n\nStartUnit: \"{str(self.StartUnit)}\" is: \"{StartType}\",\nEndUnit: \"{str(self.EndUnit)}\" is: \"{EndType}\"\nPlease ensure that these types are the same as {StartType} and {EndType} cannot be converted!")
        else:
            self.Type = str(StartType)

    def Convert(self):
        """
        Actually converts self.StartValue with self.SelfUnit to self.EndValue with self.EndUnit
        """

        # Run mandatory methods before starting
        self.FixStrings()
        self.SetType()

        # Create "ANS" based on the equation needed for converting
        ConvertEquation = Equations.get(str(self.Type)).get(str(self.StartUnit)).get(str(self.EndUnit))
        ANS = f"{str(self.StartValue)}{str(ConvertEquation)}"
        ANS = eval(ANS)
        self.EndValue = ANS

    def Summarize(self):
        """
        Creates a readable summary after converting (Please use ```self.Convert()``` before using)
        """

        # Create variables and convert local variables, to global variables
        global StartSuffix
        global EndSuffix
        StartSuffix = ""
        EndSuffix = ""

        # Makes sure that User has already used self.Convert(), and raise an error if necessary
        if self.EndValue is None:
            File = str(__file__).split('\\')[-1]
            raise NotConvertedError(f"\n\nPlease write: \"self.Convert()\" in:\n\"{File}\" before using \"self.Summarize()\"")

        # Add an "s" at the end of the Unit if necessary (Eg. "Millimeters", or "Centimeters" ("s" at the suffix))
        if float(self.StartValue) > 1:
            StartSuffix = "s"
        if float(self.EndValue) > 1:
            EndSuffix = "s"

        # Make the summary string
        String = f"{self.StartValue} {self.StartUnit}{StartSuffix} is {self.EndValue} {self.EndUnit}{EndSuffix}"
        self.Summary = String
