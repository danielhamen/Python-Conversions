# Format:
```python
Conversions(START_UNIT, START_VALUE, END_UNIT)
```

# Usage:
```python
C = Conversions("millimeter", 16, "in")
C.Convert()
print(C.EndValue)

>>> 0.6299212598425197

```

<b>To view all possible units, add: ```GetUnits(False)``` to your script. If you set the argument to ```False```, the script will ```print()``` all the units. Change to ```True``` if you want to return the Units</b>

```python
GetUnits(False)

>>> Inch            :       "inch"
>>> Foot            :       "foot"
>>> Yard            :       "yard"
>>> Mile            :       "mile"
>>> Nanometer       :       "nanometer"
>>> Micrometer      :       "micrometer"
>>> Millimeter      :       "millimeter"
>>> Meter           :       "meter"
>>> Centimeter      :       "centimeter"
>>> Kilometer       :       "kilometer"

# Or

units = GetUnits(True)

print(units)

>>> Inch            :       "inch"
>>> Foot            :       "foot"
>>> Yard            :       "yard"
>>> Mile            :       "mile"
>>> Nanometer       :       "nanometer"
>>> Micrometer      :       "micrometer"
>>> Millimeter      :       "millimeter"
>>> Meter           :       "meter"
>>> Centimeter      :       "centimeter"
>>> Kilometer       :       "kilometer"
```
