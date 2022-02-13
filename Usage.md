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

<b>To view all possible units, add: ```GetUnits(True)``` to your script. If you set the argument to ```True```, the script will ```print()``` all the units. Change to ```False``` if you want to return the Units</b>
