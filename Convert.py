class ConversionTypeError(Exception):
    pass

class NotConvertedError(Exception):
    pass

Equations = {
	"length": {
		"inch": {
			"foot": "/12",
			"yard": "/36",
			"mile": "/63360",
			"nanometer": "*2.54e+7",
			"micrometer": "*25400",
			"millimeter": "*25.4",
			"centimeter": "*2.54",
			"meter": "/39.37",
			"kilometer": "/39370"
		},

		"foot": {
			"inch": "*12",
			"yard": "/3",
			"mile": "/5280",
			"nanometer": "*3.048e+8",
			"micrometer": "*304800",
			"millimeter": "*305",
			"centimeter": "*30.48",
			"meter": "/3.281",
			"kilometer": "/3281"
		},

		"yard": {
			"inch": "*36",
			"foot": "*3",
			"mile": "/1760",
			"nanometer": "*9.144e+8",
			"micrometer": "*914400",
			"millimeter": "*914",
			"centimeter": "*91.44",
			"meter": "/1.094",
			"kilometer": "/1094"
		},

		"mile": {
			"inch": "*63360",
			"foot": "*5280",
			"yard": "*1760",
			"nanometer": "*1.609e+12",
			"micrometer": "*1.609e+9",
			"millimeter": "*1.609e+6",
			"centimeter": "*160934",
			"meter": "*1609",
			"kilometer": "*1.609"
		},

		"nanometer": {
			"inch": "/2.54e+7",
			"foot": "/3.048e+8",
			"yard": "/9.144e+8",
			"mile": "/1.609e+12",
			"micrometer": "/1000",
			"millimeter": "/1e+6",
			"centimeter": "/1e+7",
			"meter": "/1e+9",
			"kilometer": "/1e+12"
		},

		"micrometer": {
			"inch": "/25400",
			"foot": "/304800",
			"yard": "/914400",
			"mile": "/1.609e+9",
			"nanometer": "*1000",
			"millimeter": "/1000",
			"centimeter": "/10000",
			"meter": "/1e+6",
			"kilometer": "1e+9"
		},

		"millimeter": {
			"inch": "/25.4",
			"foot": "/305",
			"yard": "/914",
			"mile": "/1.609e+6",
			"nanometer": "*1e+6",
			"micrometer": "*1000",
			"centimeter": "/10",
			"meter": "/1000",
			"kilometer": "/1e+6"
		},

		"centimeter": {
			"inch": "/2.54",
			"foot": "/30.48",
			"yard": "/91.44",
			"mile": "/160934",
			"nanometer": "*1e+7",
			"micrometer": "*100000",
			"millimeter": "*10",
			"meter": "/100",
			"kilometer": "/100000"
		},

		"meter": {
			"inch": "*39.37",
			"foot": "*3.281",
			"yard": "*1.094",
			"mile": "/1609",
			"nanometer": "*1e+9",
			"micrometer": "*1e+6",
			"millimeter": "*1000",
			"centimeter": "*100",
			"kilometer": "/1000"
		},

		"kilometer": {
			"inch": "*39470",
			"foot": "*3281",
			"yard": "*1094",
			"mile": "/1.609",
			"nanometer": "*1e+12",
			"micrometer": "*1e+9",
			"millimeter": "*1e+6",
			"centimeter": "*100000",
			"kilometer": "*1000"
		}
	}
}

Types = {
	"inch": "length",
	"foot": "length",
	"yard": "length",
	"mile": "length",
	"nanometer": "length",
	"micrometer": "length",
	"millimeter": "length",
    "meter" : "length",
	"centimeter": "length",
	"kilometer": "length",
}

Variants = {
    "in": "inch",
    "inch": "inch",
    "inches": "inch",
    "ft ": "foot",
    "foot": "foot",
    "feet": "foot",
    "yd": "yard",
    "yard": "yard",
    "yards": "yard",
    "mi": "mile",
    "mile": "mile",
    "miles": "mile",
    "nm": "nanometer",
    "nanometer": "nanometer",
    "nanometre": "nanometer",
    "nanometers": "nanometer",
    "nanometres": "nanometer",
    "um": "micrometer",
    "micrometer": "micrometer",
    "micrometre": "micrometer",
    "micrometers": "micrometer",
    "micrometres": "micrometer",
    "mm": "millimeter",
    "millimeter": "millimeter",
    "millimetre": "millimeter",
    "milimeter": "millimeter",
    "milimetre": "millimeter",
    "millimeters": "millimeter",
    "milimeters": "millimeter",
    "millimetres": "millimeter",
    "milimetres": "millimeter",
    "cm": "centimeter",
    "centimeter": "centimeter",
    "centimetre": "centimeter",
    "centimeters": "centimeter",
    "centimetres": "centimeter",
    "km": "kilometer",
    "kilometre": "kilometer",
    "kilometer": "kilometer",
    "kilometers": "kilometer",
    "kilometres": "kilometer",
    "meters" : "meter",
    "meter" : "meter",
    "metre" : "meter"
}

class Conversions:
    def __init__(self, StartUnit, StartValue, EndUnit):
        self.StartUnit = StartUnit
        self.StartValue = StartValue
        self.EndUnit = EndUnit
        self.EndValue = None
        self.Type = ""
        self.Summary = ""

    def FixStrings(self):
        ReplaceVariables = [self.StartUnit, self.EndUnit]
        ReplaceVariableNames = ["self.StartUnit", "self.EndUnit"]
        IterIndex = 0
        for Var in ReplaceVariables:
            Var = Variants.get(str(Var))
            exec(f"{str(ReplaceVariableNames[IterIndex])} = \"{str(Var)}\"")
            IterIndex += 1

    def SetType(self):
        StartType = Types.get(self.StartUnit)
        EndType = Types.get(self.EndUnit)

        if StartType != EndType:
            raise ConversionTypeError(f"StartUnit: \"{str(self.StartUnit)}\" is: \"{StartType}\",\nEndUnit: \"{str(self.EndUnit)}\" is: \"{EndType}\"\nPlease ensure that these types are the same as {StartType} and {EndType} cannot be converted!")
        else:
            self.Type = str(StartType)

    def Convert(self):
        self.FixStrings()
        self.SetType()
        ConvertEquation = Equations.get(str(self.Type)).get(str(self.StartUnit)).get(str(self.EndUnit))

        ANS = f"{str(self.StartValue)}{str(ConvertEquation)}"
        ANS = eval(ANS)

        self.EndValue = ANS

    def Summarize(self):
        global StartSuffix
        global EndSuffix
        StartSuffix = ""
        EndSuffix = ""

        if self.EndValue is None:
            File = str(__file__).split('\\')[-1]
            raise NotConvertedError(f"\n\nPlease write: \"self.Convert()\" in:\n\"{File}\" before using \"self.Summarize()\"")

        if float(self.StartValue) > 1:
            StartSuffix = "s"

        if float(self.EndValue) > 1:
            EndSuffix = "s"

        String = f"{self.StartValue} {self.StartUnit}{StartSuffix} is {self.EndValue} {self.EndUnit}{EndSuffix}"

        self.Summary = String
