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

# ```START_UNIT``` and ```END_UNIT```
For the arguments ```START_UNIT``` and ```END_UNIT```, you can add any length conversion. The good thing about this module is that for the unit arguments, you can write any form of a unit. For example, if you would like to convert Millimeters, to Centimeters, in Canada, "Millimeter" is spelled "Millimeter", but in the United States, "Millimeter" is spelled "Millimetre" so you might be confused about which one you should write in the argument. For this module, if you want to convert from Millimeters, you can write ```mm```, ```Mm```, ```Millimeter```, ```millimetre```, ```milimetre```, etc!

<b>Currently this module only supports Length conversions, but hopefully in the future, I will add more types such as Time, Volume, etc!</b>
