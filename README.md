# Field Log Utilities

These tools have been a good exploration and proof of concept for me.  I was able to come up with something that was easier/more flexible than a full blown logging application.  These *Python3* scripts allow me to get POTA and SOTA activator logs created.

## Park Log for POTA

usage:

```bash
python Source/parklog.py source_file_name [--filename]
```

`--filename` will output a line you can cut-n-paste to generate your output file with the correct name

Examples:

```bash
python Source/parklog.py FieldLogs/20190629_graham_cave_1759.csv --filename

python Source/parklog.py FieldLogs/20190629_graham_cave_1759.csv > "K0EMT@K-1759 20190629.adi"
```

## SOTA Log

usage:

```bash
python csv2sota.py source_file_name
```

Example:

```bash
python Source/csv2sota.py FieldLogs/20190426_W9.IL-002.csv > 20190426_W9-IL-002-gen.csv
```

## Sample Files

While the data files are not spreadsheet data, they do contain comma separated values in a very literal sense.
I also find that if I use the `csv` extension, my editor gives me some syntax highlighting that is very helpful.

*Do not edit or view these files with an application like Excel or Numbers*

The current default band / mode is 20M CW for POTA.  No K- prefix needed for US program parks.

### POTA

```csv
!OP,K0EMT
!PARK,1782
!DATE,20190420
!MODE,CW
!BAND,20M
2103,KF7WNS
2132,WD7Y
2134,K9ZTV
!MODE,SSB
2259,K9WBZ
!MODE,CW
2325,VA7UNX
!BAND,40M
```

### SOTA

```csv
2019/04/26,W9/IL-002,K0EMT
1955,14.060,CW,K0RS
1958,14.060,CW,NG6R
2016,10.116,CW,K3TCU
2018,10.116,CW,N3EJ
2022,10.116,CW,W5ODS
2029,7.042,CW,W0MNA
2030,7.042,CW,W0ERI
2030,7.042,CW,KG3W
2033,7.042,CW,K5KJ
2035,7.042,CW,KI5WA
2038,7.042,CW,WN4AT
2039,7.042,CW,N0EVH
2041,7.042,CW,WG0AT
2044,7.042,CW,WF4I
2107,7.031,CW,KW4JM,W4C/CM-117,S2S MTR3B-LCD EFHW
```

## This code needs work

### Code

- there is no error handling
- input validation
- there are no tests
- refactor global variables to a dictionary?

### Features

- create a version of the SOTA code that works from the short input format
- add an option for just normal portable / field ops, with no SOTA or POTA
- rethink input format, maybe something with more contextual parsing?
- add a QRG command for specifying frequency
- add a fuzzy time feature.  If time is missing on an entry interpolate it based on surrounding entries that do have time specified.

### Architecture

- develop code in such a way that it can be used by CLI or web page (think lambdas or web services)
- potentially make a node or JavaScript version?
- think about separation of model and view (export)
- implement views for POTA, SOTA, General, and HTML (something the user can print and put in their logbook)

## Resources

[POTA Logging Information](https://parksontheair.com)

[SOTA Activator CSV Information](http://www.sotadata.org.uk/ActivatorCSVInfo.htm)

### SOTA V2 Format

```text
<V2> <My Callsign><My Summit> <Date> <Time> <Band> <Mode> <Their Callsign><Their Summit> <Notes or Comments>
```
