import sys
from datetime import datetime

# DEFAULTS

callsign = 'OP'
park = 'PARK'
qso_date = 'YYYYMMDD'
mode = 'CW' # or SSB or ?
band = '20M'
isPotaPark = False

def header_row():
    date = datetime.now()
    print('ParkLog by K0EMT %s<ProgramID:7>PARKLOG<EOH>' % (date))

def parse_entry(entry):
    if entry.rstrip():
        if (entry[0] == '!'):
            command_processor(entry)
        else:
            entry_processor(entry)

def command_processor(entry):
    command_entry = entry.rstrip().split(",")
    command = command_entry[0][1:]
    command_arguments = command_entry[1:]

    commands = {
        'OP': setOp,
        'PARK': setPark,
        'DATE': setQsoDate,
        'MODE': setMode,
        'BAND': setBand,
    }

    func = commands.get(command, lambda _: "Invalid command")
    func(command_arguments)

# NOTE: there is no argument validation in the setFunctions(x)

def setOp(arguments):
    global callsign 
    callsign = arguments[0]

def setPark(arguments):
    global park
    if ('-' in arguments[0]):
        park = arguments[0]
    else:
        park = 'K-' + arguments[0]

def setQsoDate(arguments):
    global qso_date 
    qso_date = arguments[0]

def setMode(arguments):
    global mode 
    mode = arguments[0]

def setBand(arguments):
    global band 
    band = arguments[0]

def entry_processor(entry):
    entry_values = entry.rstrip().split(",")

    print('%s%s%s%s%s%s%s%s%s%s%s%s<eor>' % (
        format_callsign(), 
        format_park(),
        format_call(entry_values),
        format_qso_date(),
        format_time_on(entry_values),
        format_band(),
        format_mode(),
        format_report_sent(entry_values),
        format_report_received(entry_values),
        format_state(entry_values),
        format_comment(entry_values),
        format_park_to_park(entry_values)
    ))

def format_callsign():
    return '<STATION_CALLSIGN:%s>%s<OPERATOR:%s>%s' % (len(callsign), callsign, len(callsign), callsign )

def format_park():
    return '<MY_SIG:4>POTA<MY_SIG_INFO:%s>%s' % (len(park), park)

def format_qso_date():
    return '<QSO_DATE:%s>%s' % (len(qso_date), qso_date)

def format_band():
    return '<BAND:%s>%s' % (len(band), band)

def format_mode():
    return '<MODE:%s>%s' % (len(mode), mode)

def format_time_on(entry):
    return '<TIME_ON:%s>%s' % (len(entry[0]), entry[0])

def format_call(entry):
    return '<CALL:%s>%s' % (len(entry[1]), entry[1])

def format_report_sent(entry):
    if len(entry) >= 3 and len(entry[2]) > 0:
        return '<RST_SENT:%s>%s' % (len(entry[2]), entry[2])
    else:    
        return ''

def format_report_received(entry):
    if len(entry) >= 4 and len(entry[3]) > 0:
        return '<RST_RCVD:%s>%s' % (len(entry[3]), entry[3])
    else:    
        return ''

def format_state(entry):
    if len(entry) >= 5 and len(entry[4]) > 0:
        return '<STATE:%s>%s' % (len(entry[4]), entry[4])
    else:    
        return ''

def format_comment(entry):
    if len(entry) >= 6 and len(entry[5]) > 0:
        return '<COMMENT:%s>%s' % (len(entry[5]), entry[5])
    else:    
        return ''

def format_park_to_park(entry):
    park_to_park = ''
    if len(entry) >= 7 and len(entry[6]) > 0:
        hunted_park = entry[6].strip()
        if ('-' in hunted_park):
            park_to_park = '<SIG:4>POTA<SIG_INFO:%s>%s' % (len(hunted_park), hunted_park)
        else:
            hunted_park_extrapolated = 'K-%s' % (hunted_park) # no dash, prefix with K
            park_to_park = '<SIG:4>POTA<SIG_INFO:%s>%s' % (len(hunted_park_extrapolated), hunted_park_extrapolated)
        
    return park_to_park

def output_filename():
    return '%s@%s %s.adi' % (callsign, park, qso_date)

def mcu():
    if (len(sys.argv) < 2) or ((len(sys.argv) == 2) and ('--filename' in sys.argv) ):
        print ("usage: %s <source file name> [--filename]" % sys.argv[0])
        exit(-1)

    header_row()

    sourceFileName = sys.argv[1]
    sourceFile = open(sourceFileName, "r")

    for entry in sourceFile:
        parse_entry(entry)

    sourceFile.close()

    if '--filename' in sys.argv:
        # preferred output file name yourcall@reference YYYMMDD.adi
        print ('\npython %s %s > "%s"' % (sys.argv[0], sys.argv[1], output_filename()))

mcu()