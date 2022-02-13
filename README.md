# Python-Conversions
A quick way to convert units in Python. For in-depth information on how to use this module, please read ```Usage.md```.

With this module, you can use the following units:
- Inch            :       ```inch```
- Foot            :       ```foot```
- Yard            :       ```yard```
- Mile            :       ```mile```
- Nanometer       :       ```nanometer```
- Micrometer      :       ```micrometer```
- Millimeter      :       ```millimeter```
- Meter           :       ```meter```
- Centimeter      :       ```centimeter```
- Kilometer       :       ```kilometer```

## Quick example:
> ```python
> C = Conversions("millimeter", 14.43, "inches")
> C.Convert()
> C.Summarize()
> 
> EndValue = C.EndValue
> Summary = C.Summary
> 
> print(EndValue)
> print(Summary)
> 
> # Output:
> >>> 0.5681102362204724
> >>> 14.43 millimeters is 0.5681102362204724 inch
> ```

## How to use the quick conversion program:
> Run ```Program/Program.exe```
