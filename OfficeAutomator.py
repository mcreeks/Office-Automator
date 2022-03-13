from time import sleep  # Import sleep Library
import RPi.GPIO as GPIO  # Import GPIO Library
import random

def generateEmail():
    myGenericList = ["""Dear Employer,\n
    (Insert excuse here), therefore I am unable to come into work today.\n
    Regards,\n
    Jordan""",

    '''Dear Management,\n
    I’m sorry that I can’t make it in today, (Insert excuse here). I can make myself available online later in the day.\n
    Best Wishes,\n
    Michael''',

    '''To whom it may concern, \n
    Unfortunately, I won't  be able to make it into today workshop, (Insert excuse here). \n
    Hope you understand,\n
    Samantha''']

    myGenericExcuse = ["My child got sick last night",
    "I am under the weather",
    "I have a doctors visit",
    "I have a family emergency",
    "A family member tested positive for COVID",
    "I have to take my dog to the vet",
    "My spouse is sick and I have to take care of the baby"]


    #Pull random GenericList (1-3)
    mainEmail = random.choice(myGenericList)
    mainExcuse = random.choice(myGenericExcuse)

    return(mainEmail.replace("(Insert excuse here)", mainExcuse))


GPIO.setmode(GPIO.BOARD)  # Use Physical Pin Numbering Scheme
button1 = 18  # Button 1 is connected to physical pin 16
button2 = 16  # Button 2 is connected to physical pin 12
button3 = 12
LED1 = 26  # LED 1 is connected to physical pin 22
LED2 = 24  # LED 2 is connected to physical pin 18
LED3 = 22
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Make button1 an input, Activate Pull UP Resistor
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Make button 2 an input, Activate Pull Up Resistor
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Make button 3 an input, Activate Pull Up Resistor
GPIO.setup(LED1,GPIO.OUT,)  # Make LED 1 an Output
GPIO.setup(LED2, GPIO.OUT)  # Make LED 2 an Output
GPIO.setup(LED3, GPIO.OUT)  # Make LED 3 an Output
BS1 = False  # Set Flag BS1 to indicate LED is initially off
BS2 = False  # Set Flag BS2 to indicate LED is initially off
BS3 = False  # Set Flag BS3 to indicate LED is initially off


LIST    = 1     #If LIST is 1 than complete keymap code is shown on screen
EXECUTE    = 1     #If EXECUTE is 1 than complete keymap code is send to the HID device and executed

#Variables
NULL_CHAR = chr(0)

#Functions
#Create write_report function to write HID codes to the HID Keyboard
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

#Dictionary
values = {
' ':'write_report(NULL_CHAR*2 +chr(32)+NULL_CHAR*5)',
'a':'write_report(NULL_CHAR*2 +chr(4)+NULL_CHAR*5)',
'b':'write_report(NULL_CHAR*2 +chr(5)+NULL_CHAR*5)',
'c':'write_report(NULL_CHAR*2 +chr(6)+NULL_CHAR*5)',
'd':'write_report(NULL_CHAR*2 +chr(7)+NULL_CHAR*5)',
'e':'write_report(NULL_CHAR*2 +chr(8)+NULL_CHAR*5)',
'f':'write_report(NULL_CHAR*2 +chr(9)+NULL_CHAR*5)',
'g':'write_report(NULL_CHAR*2 +chr(10)+NULL_CHAR*5)',
'h':'write_report(NULL_CHAR*2 +chr(11)+NULL_CHAR*5)',
'i':'write_report(NULL_CHAR*2 +chr(12)+NULL_CHAR*5)',
'j':'write_report(NULL_CHAR*2 +chr(13)+NULL_CHAR*5)',
'k':'write_report(NULL_CHAR*2 +chr(14)+NULL_CHAR*5)',
'l':'write_report(NULL_CHAR*2 +chr(15)+NULL_CHAR*5)',
'm':'write_report(NULL_CHAR*2 +chr(16)+NULL_CHAR*5)',
'n':'write_report(NULL_CHAR*2 +chr(17)+NULL_CHAR*5)',
'o':'write_report(NULL_CHAR*2 +chr(18)+NULL_CHAR*5)',
'p':'write_report(NULL_CHAR*2 +chr(19)+NULL_CHAR*5)',
'q':'write_report(NULL_CHAR*2 +chr(20)+NULL_CHAR*5)',
'r':'write_report(NULL_CHAR*2 +chr(21)+NULL_CHAR*5)',
's':'write_report(NULL_CHAR*2 +chr(22)+NULL_CHAR*5)',
't':'write_report(NULL_CHAR*2 +chr(23)+NULL_CHAR*5)',
'u':'write_report(NULL_CHAR*2 +chr(24)+NULL_CHAR*5)',
'v':'write_report(NULL_CHAR*2 +chr(25)+NULL_CHAR*5)',
'w':'write_report(NULL_CHAR*2 +chr(26)+NULL_CHAR*5)',
'x':'write_report(NULL_CHAR*2 +chr(27)+NULL_CHAR*5)',
'y':'write_report(NULL_CHAR*2 +chr(28)+NULL_CHAR*5)',
'z':'write_report(NULL_CHAR*2 +chr(29)+NULL_CHAR*5)',
'A':'write_report(chr(2)+NULL_CHAR+chr(4)+NULL_CHAR*5)',
'B':'write_report(chr(2)+NULL_CHAR+chr(5)+NULL_CHAR*5)',
'C':'write_report(chr(2)+NULL_CHAR+chr(6)+NULL_CHAR*5)',
'D':'write_report(chr(2)+NULL_CHAR+chr(7)+NULL_CHAR*5)',
'E':'write_report(chr(2)+NULL_CHAR+chr(8)+NULL_CHAR*5)',
'F':'write_report(chr(2)+NULL_CHAR+chr(9)+NULL_CHAR*5)',
'G':'write_report(chr(2)+NULL_CHAR+chr(10)+NULL_CHAR*5)',
'H':'write_report(chr(2)+NULL_CHAR+chr(11)+NULL_CHAR*5)',
'I':'write_report(chr(2)+NULL_CHAR+chr(12)+NULL_CHAR*5)',
'J':'write_report(chr(2)+NULL_CHAR+chr(13)+NULL_CHAR*5)',
'K':'write_report(chr(2)+NULL_CHAR+chr(14)+NULL_CHAR*5)',
'L':'write_report(chr(2)+NULL_CHAR+chr(15)+NULL_CHAR*5)',
'M':'write_report(chr(2)+NULL_CHAR+chr(16)+NULL_CHAR*5)',
'N':'write_report(chr(2)+NULL_CHAR+chr(17)+NULL_CHAR*5)',
'O':'write_report(chr(2)+NULL_CHAR+chr(18)+NULL_CHAR*5)',
'P':'write_report(chr(2)+NULL_CHAR+chr(19)+NULL_CHAR*5)',
'Q':'write_report(chr(2)+NULL_CHAR+chr(20)+NULL_CHAR*5)',
'R':'write_report(chr(2)+NULL_CHAR+chr(21)+NULL_CHAR*5)',
'S':'write_report(chr(2)+NULL_CHAR+chr(22)+NULL_CHAR*5)',
'T':'write_report(chr(2)+NULL_CHAR+chr(23)+NULL_CHAR*5)',
'U':'write_report(chr(2)+NULL_CHAR+chr(24)+NULL_CHAR*5)',
'V':'write_report(chr(2)+NULL_CHAR+chr(25)+NULL_CHAR*5)',
'W':'write_report(chr(2)+NULL_CHAR+chr(26)+NULL_CHAR*5)',
'X':'write_report(chr(2)+NULL_CHAR+chr(27)+NULL_CHAR*5)',
'Y':'write_report(chr(2)+NULL_CHAR+chr(28)+NULL_CHAR*5)',
'Z':'write_report(chr(2)+NULL_CHAR+chr(29)+NULL_CHAR*5)',
'1':'write_report(NULL_CHAR*2 +chr(30)+NULL_CHAR*5)',
'2':'write_report(NULL_CHAR*2 +chr(31)+NULL_CHAR*5)',
'3':'write_report(NULL_CHAR*2 +chr(32)+NULL_CHAR*5)',
'4':'write_report(NULL_CHAR*2 +chr(33)+NULL_CHAR*5)',
'5':'write_report(NULL_CHAR*2 +chr(34)+NULL_CHAR*5)',
'6':'write_report(NULL_CHAR*2 +chr(35)+NULL_CHAR*5)',
'7':'write_report(NULL_CHAR*2 +chr(36)+NULL_CHAR*5)',
'8':'write_report(NULL_CHAR*2 +chr(37)+NULL_CHAR*5)',
'9':'write_report(NULL_CHAR*2 +chr(38)+NULL_CHAR*5)',
'0':'write_report(NULL_CHAR*2 +chr(39)+NULL_CHAR*5)',
'!':'write_report(chr(2)+NULL_CHAR+chr(30)+NULL_CHAR*5)',
'@':'write_report(chr(2)+NULL_CHAR+chr(31)+NULL_CHAR*5)',
'#':'write_report(chr(2)+NULL_CHAR+chr(32)+NULL_CHAR*5)',
'$':'write_report(chr(2)+NULL_CHAR+chr(33)+NULL_CHAR*5)',
'%':'write_report(chr(2)+NULL_CHAR+chr(34)+NULL_CHAR*5)',
'^':'write_report(chr(2)+NULL_CHAR+chr(35)+NULL_CHAR*5)',
'&':'write_report(chr(2)+NULL_CHAR+chr(36)+NULL_CHAR*5)',
'*':'write_report(chr(2)+NULL_CHAR+chr(37)+NULL_CHAR*5)',
'(':'write_report(chr(2)+NULL_CHAR+chr(38)+NULL_CHAR*5)',
')':'write_report(chr(2)+NULL_CHAR+chr(39)+NULL_CHAR*5)',
'ENTER':'write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5)',
'ESC':'write_report(NULL_CHAR*2 +chr(41)+NULL_CHAR*5)',
'BACKSPACE':'write_report(NULL_CHAR*2 +chr(42)+NULL_CHAR*5)',
'TAB':'write_report(NULL_CHAR*2 +chr(43)+NULL_CHAR*5)',
'SPATIE':'write_report(NULL_CHAR*2 +chr(44)+NULL_CHAR*5)',
'-':'write_report(NULL_CHAR*2 +chr(45)+NULL_CHAR*5)',
'=':'write_report(NULL_CHAR*2 +chr(46)+NULL_CHAR*5)',
'{':'write_report(NULL_CHAR*2 +chr(47)+NULL_CHAR*5)',
'}':'write_report(NULL_CHAR*2 +chr(48)+NULL_CHAR*5)',
'\\':'write_report(NULL_CHAR*2 +chr(49)+NULL_CHAR*5)',
'~':'write_report(NULL_CHAR*2 +chr(50)+NULL_CHAR*5)',
';':'write_report(NULL_CHAR*2 +chr(51)+NULL_CHAR*5)',
'':'write_report(NULL_CHAR*2 +chr(52)+NULL_CHAR*5)',
'`':'write_report(NULL_CHAR*2 +chr(53)+NULL_CHAR*5)',
',':'write_report(NULL_CHAR*2 +chr(54)+NULL_CHAR*5)',
'.':'write_report(NULL_CHAR*2 +chr(55)+NULL_CHAR*5)',
'/':'write_report(NULL_CHAR*2 +chr(56)+NULL_CHAR*5)',
'_':'write_report(chr(2)+NULL_CHAR+chr(45)+NULL_CHAR*5)',
'+':'write_report(chr(2)+NULL_CHAR+chr(46)+NULL_CHAR*5)',
'[':'write_report(chr(2)+NULL_CHAR+chr(47)+NULL_CHAR*5)',
']':'write_report(chr(2)+NULL_CHAR+chr(48)+NULL_CHAR*5)',
'|':'write_report(chr(2)+NULL_CHAR+chr(49)+NULL_CHAR*5)',
'0':'write_report(chr(2)+NULL_CHAR+chr(50)+NULL_CHAR*5)',
':':'write_report(chr(2)+NULL_CHAR+chr(51)+NULL_CHAR*5)',
'"':'write_report(chr(2)+NULL_CHAR+chr(52)+NULL_CHAR*5)',
'~':'write_report(chr(2)+NULL_CHAR+chr(53)+NULL_CHAR*5)',
'<':'write_report(chr(2)+NULL_CHAR+chr(54)+NULL_CHAR*5)',
'>':'write_report(chr(2)+NULL_CHAR+chr(55)+NULL_CHAR*5)',
'?':'write_report(chr(2)+NULL_CHAR+chr(56)+NULL_CHAR*5)',
'CAPSLOCK':'write_report(NULL_CHAR*2 +chr(57)+NULL_CHAR*5)',
'F1':'write_report(NULL_CHAR*2 +chr(58)+NULL_CHAR*5)',
'F2':'write_report(NULL_CHAR*2 +chr(59)+NULL_CHAR*5)',
'F3':'write_report(NULL_CHAR*2 +chr(60)+NULL_CHAR*5)',
'F4':'write_report(NULL_CHAR*2 +chr(61)+NULL_CHAR*5)',
'F5':'write_report(NULL_CHAR*2 +chr(62)+NULL_CHAR*5)',
'F6':'write_report(NULL_CHAR*2 +chr(63)+NULL_CHAR*5)',
'F7':'write_report(NULL_CHAR*2 +chr(64)+NULL_CHAR*5)',
'F8':'write_report(NULL_CHAR*2 +chr(65)+NULL_CHAR*5)',
'F9':'write_report(NULL_CHAR*2 +chr(66)+NULL_CHAR*5)',
'F10':'write_report(NULL_CHAR*2 +chr(67)+NULL_CHAR*5)',
'F11':'write_report(NULL_CHAR*2 +chr(68)+NULL_CHAR*5)',
'F12':'write_report(NULL_CHAR*2 +chr(69)+NULL_CHAR*5)',
'PRINT SCREEN':'write_report(NULL_CHAR*2 +chr(70)+NULL_CHAR*5)',
'SCROLL LOCK':'write_report(NULL_CHAR*2 +chr(71)+NULL_CHAR*5)',
'PAUSE':'write_report(NULL_CHAR*2 +chr(72)+NULL_CHAR*5)',
'INSERT':'write_report(NULL_CHAR*2 +chr(73)+NULL_CHAR*5)',
'HOME':'write_report(NULL_CHAR*2 +chr(74)+NULL_CHAR*5)',
'PAGEUP':'write_report(NULL_CHAR*2 +chr(75)+NULL_CHAR*5)',
'DELETE':'write_report(NULL_CHAR*2 +chr(76)+NULL_CHAR*5)',
'END':'write_report(NULL_CHAR*2 +chr(77)+NULL_CHAR*5)',
'PAGEDOWN':'write_report(NULL_CHAR*2 +chr(78)+NULL_CHAR*5)',
'}':'write_report(NULL_CHAR*2 +chr(79)+NULL_CHAR*5)',
'{':'write_report(NULL_CHAR*2 +chr(80)+NULL_CHAR*5)',
']':'write_report(chr(2)+NULL_CHAR+chr(79)+NULL_CHAR*5)',
'[':'write_report(chr(2)+NULL_CHAR+chr(80)+NULL_CHAR*5)',
'DOWN':'write_report(NULL_CHAR*2 +chr(81)+NULL_CHAR*5)',
'UP':'write_report(NULL_CHAR*2 +chr(82)+NULL_CHAR*5)',
'NUM LOCK':'write_report(NULL_CHAR*2 +chr(83)+NULL_CHAR*5)',
'Keypad SLASH (/)':'write_report(NULL_CHAR*2 +chr(84)+NULL_CHAR*5)',
'Keypad ASTERISK (*)':'write_report(NULL_CHAR*2 +chr(85)+NULL_CHAR*5)',
'Keypad MINUS (-)':'write_report(NULL_CHAR*2 +chr(86)+NULL_CHAR*5)',
'Keypad PLUS (+)':'write_report(NULL_CHAR*2 +chr(87)+NULL_CHAR*5)',
'Keypad ENTER':'write_report(NULL_CHAR*2 +chr(88)+NULL_CHAR*5)',
'Keypad 1':'write_report(NULL_CHAR*2 +chr(89)+NULL_CHAR*5)',
'Keypad 2':'write_report(NULL_CHAR*2 +chr(90)+NULL_CHAR*5)',
'Keypad 3':'write_report(NULL_CHAR*2 +chr(91)+NULL_CHAR*5)',
'Keypad 4':'write_report(NULL_CHAR*2 +chr(92)+NULL_CHAR*5)',
'Keypad END':'write_report(chr(2)+NULL_CHAR+chr(89)+NULL_CHAR*5)',
'Keypad DOWN':'write_report(chr(2)+NULL_CHAR+chr(90)+NULL_CHAR*5)',
'Keypad PAGEDOWN':'write_report(chr(2)+NULL_CHAR+chr(91)+NULL_CHAR*5)',
'Keypad LEFT':'write_report(chr(2)+NULL_CHAR+chr(92)+NULL_CHAR*5)',
'Keypad 5':'write_report(NULL_CHAR*2 +chr(93)+NULL_CHAR*5)',
'Keypad 6':'write_report(NULL_CHAR*2 +chr(94)+NULL_CHAR*5)',
'Keypad 7':'write_report(NULL_CHAR*2 +chr(95)+NULL_CHAR*5)',
'Keypad 8':'write_report(NULL_CHAR*2 +chr(96)+NULL_CHAR*5)',
'Keypad 9':'write_report(NULL_CHAR*2 +chr(97)+NULL_CHAR*5)',
'Keypad 0':'write_report(NULL_CHAR*2 +chr(98)+NULL_CHAR*5)',
'Keypad DOT (.)':'write_report(NULL_CHAR*2 +chr(99)+NULL_CHAR*5)',
'Non-US Slash \\':'write_report(NULL_CHAR*2 +chr(100)+NULL_CHAR*5)',
'Keypad RIGHT':'write_report(chr(2)+NULL_CHAR+chr(94)+NULL_CHAR*5)',
'Keypad HOME':'write_report(chr(2)+NULL_CHAR+chr(95)+NULL_CHAR*5)',
'Keypad UP':'write_report(chr(2)+NULL_CHAR+chr(96)+NULL_CHAR*5)',
'Keypad PAGEUP':'write_report(chr(2)+NULL_CHAR+chr(97)+NULL_CHAR*5)',
'Keypad INSERT':'write_report(chr(2)+NULL_CHAR+chr(98)+NULL_CHAR*5)',
'Keypad DEL':'write_report(chr(2)+NULL_CHAR+chr(99)+NULL_CHAR*5)',
'Non-US Slash |':'write_report(chr(2)+NULL_CHAR+chr(100)+NULL_CHAR*5)',
'COMPOSE / APPLICATION':'write_report(NULL_CHAR*2 +chr(101)+NULL_CHAR*5)',
'POWER':'write_report(NULL_CHAR*2 +chr(102)+NULL_CHAR*5)',
'Keypad EQUAL (=)':'write_report(NULL_CHAR*2 +chr(103)+NULL_CHAR*5)',
'F13':'write_report(NULL_CHAR*2 +chr(104)+NULL_CHAR*5)',
'F14':'write_report(NULL_CHAR*2 +chr(105)+NULL_CHAR*5)',
'F15':'write_report(NULL_CHAR*2 +chr(106)+NULL_CHAR*5)',
'F16':'write_report(NULL_CHAR*2 +chr(107)+NULL_CHAR*5)',
'F17':'write_report(NULL_CHAR*2 +chr(108)+NULL_CHAR*5)',
'F18':'write_report(NULL_CHAR*2 +chr(109)+NULL_CHAR*5)',
'F19':'write_report(NULL_CHAR*2 +chr(110)+NULL_CHAR*5)',
'F20':'write_report(NULL_CHAR*2 +chr(111)+NULL_CHAR*5)',
'F21':'write_report(NULL_CHAR*2 +chr(112)+NULL_CHAR*5)',
'F22':'write_report(NULL_CHAR*2 +chr(113)+NULL_CHAR*5)',
'F23':'write_report(NULL_CHAR*2 +chr(114)+NULL_CHAR*5)',
'F24':'write_report(NULL_CHAR*2 +chr(115)+NULL_CHAR*5)',
'EXECUTE':'write_report(NULL_CHAR*2 +chr(116)+NULL_CHAR*5)',
'HELP':'write_report(NULL_CHAR*2 +chr(117)+NULL_CHAR*5)',
'MENU':'write_report(NULL_CHAR*2 +chr(118)+NULL_CHAR*5)',
'SELECT':'write_report(NULL_CHAR*2 +chr(119)+NULL_CHAR*5)',
'STOP':'write_report(NULL_CHAR*2 +chr(120)+NULL_CHAR*5)',
'AGAIN':'write_report(NULL_CHAR*2 +chr(121)+NULL_CHAR*5)',
'UNCO':'write_report(NULL_CHAR*2 +chr(122)+NULL_CHAR*5)',
'CUT':'write_report(NULL_CHAR*2 +chr(123)+NULL_CHAR*5)',
'COPY':'write_report(NULL_CHAR*2 +chr(124)+NULL_CHAR*5)',
'PASTE':'write_report(NULL_CHAR*2 +chr(125)+NULL_CHAR*5)',
'FIND':'write_report(NULL_CHAR*2 +chr(126)+NULL_CHAR*5)',
'MUTE':'write_report(NULL_CHAR*2 +chr(127)+NULL_CHAR*5)',
'VOLUME UP':'write_report(NULL_CHAR*2 +chr(128)+NULL_CHAR*5)',
'VOLUME DOWN':'write_report(NULL_CHAR*2 +chr(129)+NULL_CHAR*5)',
'CTRL + ALT + DEL':'write_report(chr(5)+NULL_CHAR+chr(76)+NULL_CHAR*5)',
'CTRL + w':'write_report(chr(1)+NULL_CHAR+chr(26)+NULL_CHAR*5)',
'WIN + TAB':'write_report(chr(8)+NULL_CHAR+chr(43)+NULL_CHAR*5)',
'ALT + TAB':'write_report(chr(4)+NULL_CHAR+chr(43)+NULL_CHAR*5)',
'CTRL + F':'write_report(chr(1)+NULL_CHAR+chr(9)+NULL_CHAR*5)',
'CTRL + ALT +     ARROWDOWN':'write_report(chr(5)+NULL_CHAR+chr(81)+NULL_CHAR*5)',
}

emailDict = {
'\n':'write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5)',
'a':'write_report(NULL_CHAR*2 +chr(4)+NULL_CHAR*5)',
'b':'write_report(NULL_CHAR*2 +chr(5)+NULL_CHAR*5)',
'c':'write_report(NULL_CHAR*2 +chr(6)+NULL_CHAR*5)',
'd':'write_report(NULL_CHAR*2 +chr(7)+NULL_CHAR*5)',
'e':'write_report(NULL_CHAR*2 +chr(8)+NULL_CHAR*5)',
'f':'write_report(NULL_CHAR*2 +chr(9)+NULL_CHAR*5)',
'g':'write_report(NULL_CHAR*2 +chr(10)+NULL_CHAR*5)',
'h':'write_report(NULL_CHAR*2 +chr(11)+NULL_CHAR*5)',
'i':'write_report(NULL_CHAR*2 +chr(12)+NULL_CHAR*5)',
'j':'write_report(NULL_CHAR*2 +chr(13)+NULL_CHAR*5)',
'k':'write_report(NULL_CHAR*2 +chr(14)+NULL_CHAR*5)',
'l':'write_report(NULL_CHAR*2 +chr(15)+NULL_CHAR*5)',
'm':'write_report(NULL_CHAR*2 +chr(16)+NULL_CHAR*5)',
'n':'write_report(NULL_CHAR*2 +chr(17)+NULL_CHAR*5)',
'o':'write_report(NULL_CHAR*2 +chr(18)+NULL_CHAR*5)',
'p':'write_report(NULL_CHAR*2 +chr(19)+NULL_CHAR*5)',
'q':'write_report(NULL_CHAR*2 +chr(20)+NULL_CHAR*5)',
'r':'write_report(NULL_CHAR*2 +chr(21)+NULL_CHAR*5)',
's':'write_report(NULL_CHAR*2 +chr(22)+NULL_CHAR*5)',
't':'write_report(NULL_CHAR*2 +chr(23)+NULL_CHAR*5)',
'u':'write_report(NULL_CHAR*2 +chr(24)+NULL_CHAR*5)',
'v':'write_report(NULL_CHAR*2 +chr(25)+NULL_CHAR*5)',
'w':'write_report(NULL_CHAR*2 +chr(26)+NULL_CHAR*5)',
'x':'write_report(NULL_CHAR*2 +chr(27)+NULL_CHAR*5)',
'y':'write_report(NULL_CHAR*2 +chr(28)+NULL_CHAR*5)',
'z':'write_report(NULL_CHAR*2 +chr(29)+NULL_CHAR*5)',
'A':'write_report(chr(2)+NULL_CHAR+chr(4)+NULL_CHAR*5)',
'B':'write_report(chr(2)+NULL_CHAR+chr(5)+NULL_CHAR*5)',
'C':'write_report(chr(2)+NULL_CHAR+chr(6)+NULL_CHAR*5)',
'D':'write_report(chr(2)+NULL_CHAR+chr(7)+NULL_CHAR*5)',
'E':'write_report(chr(2)+NULL_CHAR+chr(8)+NULL_CHAR*5)',
'F':'write_report(chr(2)+NULL_CHAR+chr(9)+NULL_CHAR*5)',
'G':'write_report(chr(2)+NULL_CHAR+chr(10)+NULL_CHAR*5)',
'H':'write_report(chr(2)+NULL_CHAR+chr(11)+NULL_CHAR*5)',
'I':'write_report(chr(2)+NULL_CHAR+chr(12)+NULL_CHAR*5)',
'J':'write_report(chr(2)+NULL_CHAR+chr(13)+NULL_CHAR*5)',
'K':'write_report(chr(2)+NULL_CHAR+chr(14)+NULL_CHAR*5)',
'L':'write_report(chr(2)+NULL_CHAR+chr(15)+NULL_CHAR*5)',
'M':'write_report(chr(2)+NULL_CHAR+chr(16)+NULL_CHAR*5)',
'N':'write_report(chr(2)+NULL_CHAR+chr(17)+NULL_CHAR*5)',
'O':'write_report(chr(2)+NULL_CHAR+chr(18)+NULL_CHAR*5)',
'P':'write_report(chr(2)+NULL_CHAR+chr(19)+NULL_CHAR*5)',
'Q':'write_report(chr(2)+NULL_CHAR+chr(20)+NULL_CHAR*5)',
'R':'write_report(chr(2)+NULL_CHAR+chr(21)+NULL_CHAR*5)',
'S':'write_report(chr(2)+NULL_CHAR+chr(22)+NULL_CHAR*5)',
'T':'write_report(chr(2)+NULL_CHAR+chr(23)+NULL_CHAR*5)',
'U':'write_report(chr(2)+NULL_CHAR+chr(24)+NULL_CHAR*5)',
'V':'write_report(chr(2)+NULL_CHAR+chr(25)+NULL_CHAR*5)',
'W':'write_report(chr(2)+NULL_CHAR+chr(26)+NULL_CHAR*5)',
'X':'write_report(chr(2)+NULL_CHAR+chr(27)+NULL_CHAR*5)',
'Y':'write_report(chr(2)+NULL_CHAR+chr(28)+NULL_CHAR*5)',
'Z':'write_report(chr(2)+NULL_CHAR+chr(29)+NULL_CHAR*5)',
'1':'write_report(NULL_CHAR*2 +chr(30)+NULL_CHAR*5)',
'2':'write_report(NULL_CHAR*2 +chr(31)+NULL_CHAR*5)',
'3':'write_report(NULL_CHAR*2 +chr(32)+NULL_CHAR*5)',
'4':'write_report(NULL_CHAR*2 +chr(33)+NULL_CHAR*5)',
'5':'write_report(NULL_CHAR*2 +chr(34)+NULL_CHAR*5)',
'6':'write_report(NULL_CHAR*2 +chr(35)+NULL_CHAR*5)',
'7':'write_report(NULL_CHAR*2 +chr(36)+NULL_CHAR*5)',
'8':'write_report(NULL_CHAR*2 +chr(37)+NULL_CHAR*5)',
'9':'write_report(NULL_CHAR*2 +chr(38)+NULL_CHAR*5)',
'0':'write_report(NULL_CHAR*2 +chr(39)+NULL_CHAR*5)',
'!':'write_report(chr(2)+NULL_CHAR+chr(30)+NULL_CHAR*5)',
'@':'write_report(chr(2)+NULL_CHAR+chr(31)+NULL_CHAR*5)',
'#':'write_report(chr(2)+NULL_CHAR+chr(32)+NULL_CHAR*5)',
'$':'write_report(chr(2)+NULL_CHAR+chr(33)+NULL_CHAR*5)',
'%':'write_report(chr(2)+NULL_CHAR+chr(34)+NULL_CHAR*5)',
'^':'write_report(chr(2)+NULL_CHAR+chr(35)+NULL_CHAR*5)',
'&':'write_report(chr(2)+NULL_CHAR+chr(36)+NULL_CHAR*5)',
'*':'write_report(chr(2)+NULL_CHAR+chr(37)+NULL_CHAR*5)',
'(':'write_report(chr(2)+NULL_CHAR+chr(38)+NULL_CHAR*5)',
')':'write_report(chr(2)+NULL_CHAR+chr(39)+NULL_CHAR*5)',
'ENTER':'write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5)',
'ESC':'write_report(NULL_CHAR*2 +chr(41)+NULL_CHAR*5)',
'BACKSPACE':'write_report(NULL_CHAR*2 +chr(42)+NULL_CHAR*5)',
'TAB':'write_report(NULL_CHAR*2 +chr(43)+NULL_CHAR*5)',
' ':'write_report(NULL_CHAR*2 +chr(44)+NULL_CHAR*5)',
'-':'write_report(NULL_CHAR*2 +chr(45)+NULL_CHAR*5)',
'=':'write_report(NULL_CHAR*2 +chr(46)+NULL_CHAR*5)',
'{':'write_report(NULL_CHAR*2 +chr(47)+NULL_CHAR*5)',
'}':'write_report(NULL_CHAR*2 +chr(48)+NULL_CHAR*5)',
'\\':'write_report(NULL_CHAR*2 +chr(49)+NULL_CHAR*5)',
'~':'write_report(NULL_CHAR*2 +chr(50)+NULL_CHAR*5)',
';':'write_report(NULL_CHAR*2 +chr(51)+NULL_CHAR*5)',
'':'write_report(NULL_CHAR*2 +chr(52)+NULL_CHAR*5)',
'`':'write_report(NULL_CHAR*2 +chr(53)+NULL_CHAR*5)',
',':'write_report(NULL_CHAR*2 +chr(54)+NULL_CHAR*5)',
'.':'write_report(NULL_CHAR*2 +chr(55)+NULL_CHAR*5)',
'/':'write_report(NULL_CHAR*2 +chr(56)+NULL_CHAR*5)',
'_':'write_report(chr(2)+NULL_CHAR+chr(45)+NULL_CHAR*5)',
'+':'write_report(chr(2)+NULL_CHAR+chr(46)+NULL_CHAR*5)',
'[':'write_report(chr(2)+NULL_CHAR+chr(47)+NULL_CHAR*5)',
']':'write_report(chr(2)+NULL_CHAR+chr(48)+NULL_CHAR*5)',
'|':'write_report(chr(2)+NULL_CHAR+chr(49)+NULL_CHAR*5)',
'0':'write_report(chr(2)+NULL_CHAR+chr(50)+NULL_CHAR*5)',
':':'write_report(chr(2)+NULL_CHAR+chr(51)+NULL_CHAR*5)',
'"':'write_report(chr(2)+NULL_CHAR+chr(52)+NULL_CHAR*5)',
'~':'write_report(chr(2)+NULL_CHAR+chr(53)+NULL_CHAR*5)',
'<':'write_report(chr(2)+NULL_CHAR+chr(54)+NULL_CHAR*5)',
'>':'write_report(chr(2)+NULL_CHAR+chr(55)+NULL_CHAR*5)',
'?':'write_report(chr(2)+NULL_CHAR+chr(56)+NULL_CHAR*5)',
'CAPSLOCK':'write_report(NULL_CHAR*2 +chr(57)+NULL_CHAR*5)',
'F1':'write_report(NULL_CHAR*2 +chr(58)+NULL_CHAR*5)',
'F2':'write_report(NULL_CHAR*2 +chr(59)+NULL_CHAR*5)',
'F3':'write_report(NULL_CHAR*2 +chr(60)+NULL_CHAR*5)',
'F4':'write_report(NULL_CHAR*2 +chr(61)+NULL_CHAR*5)',
'F5':'write_report(NULL_CHAR*2 +chr(62)+NULL_CHAR*5)',
'F6':'write_report(NULL_CHAR*2 +chr(63)+NULL_CHAR*5)',
'F7':'write_report(NULL_CHAR*2 +chr(64)+NULL_CHAR*5)',
'F8':'write_report(NULL_CHAR*2 +chr(65)+NULL_CHAR*5)',
'F9':'write_report(NULL_CHAR*2 +chr(66)+NULL_CHAR*5)',
'F10':'write_report(NULL_CHAR*2 +chr(67)+NULL_CHAR*5)',
'F11':'write_report(NULL_CHAR*2 +chr(68)+NULL_CHAR*5)',
'F12':'write_report(NULL_CHAR*2 +chr(69)+NULL_CHAR*5)',
'PRINT SCREEN':'write_report(NULL_CHAR*2 +chr(70)+NULL_CHAR*5)',
'SCROLL LOCK':'write_report(NULL_CHAR*2 +chr(71)+NULL_CHAR*5)',
'PAUSE':'write_report(NULL_CHAR*2 +chr(72)+NULL_CHAR*5)',
'INSERT':'write_report(NULL_CHAR*2 +chr(73)+NULL_CHAR*5)',
'HOME':'write_report(NULL_CHAR*2 +chr(74)+NULL_CHAR*5)',
'PAGEUP':'write_report(NULL_CHAR*2 +chr(75)+NULL_CHAR*5)',
'DELETE':'write_report(NULL_CHAR*2 +chr(76)+NULL_CHAR*5)',
'END':'write_report(NULL_CHAR*2 +chr(77)+NULL_CHAR*5)',
'PAGEDOWN':'write_report(NULL_CHAR*2 +chr(78)+NULL_CHAR*5)',
'}':'write_report(NULL_CHAR*2 +chr(79)+NULL_CHAR*5)',
'{':'write_report(NULL_CHAR*2 +chr(80)+NULL_CHAR*5)',
']':'write_report(chr(2)+NULL_CHAR+chr(79)+NULL_CHAR*5)',
'[':'write_report(chr(2)+NULL_CHAR+chr(80)+NULL_CHAR*5)',
'DOWN':'write_report(NULL_CHAR*2 +chr(81)+NULL_CHAR*5)',
'UP':'write_report(NULL_CHAR*2 +chr(82)+NULL_CHAR*5)',
'NUM LOCK':'write_report(NULL_CHAR*2 +chr(83)+NULL_CHAR*5)',
'Keypad SLASH (/)':'write_report(NULL_CHAR*2 +chr(84)+NULL_CHAR*5)',
'Keypad ASTERISK (*)':'write_report(NULL_CHAR*2 +chr(85)+NULL_CHAR*5)',
'Keypad MINUS (-)':'write_report(NULL_CHAR*2 +chr(86)+NULL_CHAR*5)',
'Keypad PLUS (+)':'write_report(NULL_CHAR*2 +chr(87)+NULL_CHAR*5)',
'Keypad ENTER':'write_report(NULL_CHAR*2 +chr(88)+NULL_CHAR*5)',
'Keypad 1':'write_report(NULL_CHAR*2 +chr(89)+NULL_CHAR*5)',
'Keypad 2':'write_report(NULL_CHAR*2 +chr(90)+NULL_CHAR*5)',
'Keypad 3':'write_report(NULL_CHAR*2 +chr(91)+NULL_CHAR*5)',
'Keypad 4':'write_report(NULL_CHAR*2 +chr(92)+NULL_CHAR*5)',
'Keypad END':'write_report(chr(2)+NULL_CHAR+chr(89)+NULL_CHAR*5)',
'Keypad DOWN':'write_report(chr(2)+NULL_CHAR+chr(90)+NULL_CHAR*5)',
'Keypad PAGEDOWN':'write_report(chr(2)+NULL_CHAR+chr(91)+NULL_CHAR*5)',
'Keypad LEFT':'write_report(chr(2)+NULL_CHAR+chr(92)+NULL_CHAR*5)',
'Keypad 5':'write_report(NULL_CHAR*2 +chr(93)+NULL_CHAR*5)',
'Keypad 6':'write_report(NULL_CHAR*2 +chr(94)+NULL_CHAR*5)',
'Keypad 7':'write_report(NULL_CHAR*2 +chr(95)+NULL_CHAR*5)',
'Keypad 8':'write_report(NULL_CHAR*2 +chr(96)+NULL_CHAR*5)',
'Keypad 9':'write_report(NULL_CHAR*2 +chr(97)+NULL_CHAR*5)',
'Keypad 0':'write_report(NULL_CHAR*2 +chr(98)+NULL_CHAR*5)',
'Keypad DOT (.)':'write_report(NULL_CHAR*2 +chr(99)+NULL_CHAR*5)',
'Non-US Slash \\':'write_report(NULL_CHAR*2 +chr(100)+NULL_CHAR*5)',
'Keypad RIGHT':'write_report(chr(2)+NULL_CHAR+chr(94)+NULL_CHAR*5)',
'Keypad HOME':'write_report(chr(2)+NULL_CHAR+chr(95)+NULL_CHAR*5)',
'Keypad UP':'write_report(chr(2)+NULL_CHAR+chr(96)+NULL_CHAR*5)',
'Keypad PAGEUP':'write_report(chr(2)+NULL_CHAR+chr(97)+NULL_CHAR*5)',
'Keypad INSERT':'write_report(chr(2)+NULL_CHAR+chr(98)+NULL_CHAR*5)',
'Keypad DEL':'write_report(chr(2)+NULL_CHAR+chr(99)+NULL_CHAR*5)',
'Non-US Slash |':'write_report(chr(2)+NULL_CHAR+chr(100)+NULL_CHAR*5)',
'COMPOSE / APPLICATION':'write_report(NULL_CHAR*2 +chr(101)+NULL_CHAR*5)',
'POWER':'write_report(NULL_CHAR*2 +chr(102)+NULL_CHAR*5)',
'Keypad EQUAL (=)':'write_report(NULL_CHAR*2 +chr(103)+NULL_CHAR*5)',
'F13':'write_report(NULL_CHAR*2 +chr(104)+NULL_CHAR*5)',
'F14':'write_report(NULL_CHAR*2 +chr(105)+NULL_CHAR*5)',
'F15':'write_report(NULL_CHAR*2 +chr(106)+NULL_CHAR*5)',
'F16':'write_report(NULL_CHAR*2 +chr(107)+NULL_CHAR*5)',
'F17':'write_report(NULL_CHAR*2 +chr(108)+NULL_CHAR*5)',
'F18':'write_report(NULL_CHAR*2 +chr(109)+NULL_CHAR*5)',
'F19':'write_report(NULL_CHAR*2 +chr(110)+NULL_CHAR*5)',
'F20':'write_report(NULL_CHAR*2 +chr(111)+NULL_CHAR*5)',
'F21':'write_report(NULL_CHAR*2 +chr(112)+NULL_CHAR*5)',
'F22':'write_report(NULL_CHAR*2 +chr(113)+NULL_CHAR*5)',
'F23':'write_report(NULL_CHAR*2 +chr(114)+NULL_CHAR*5)',
'F24':'write_report(NULL_CHAR*2 +chr(115)+NULL_CHAR*5)',
'EXECUTE':'write_report(NULL_CHAR*2 +chr(116)+NULL_CHAR*5)',
'HELP':'write_report(NULL_CHAR*2 +chr(117)+NULL_CHAR*5)',
'MENU':'write_report(NULL_CHAR*2 +chr(118)+NULL_CHAR*5)',
'SELECT':'write_report(NULL_CHAR*2 +chr(119)+NULL_CHAR*5)',
'STOP':'write_report(NULL_CHAR*2 +chr(120)+NULL_CHAR*5)',
'AGAIN':'write_report(NULL_CHAR*2 +chr(121)+NULL_CHAR*5)',
'UNCO':'write_report(NULL_CHAR*2 +chr(122)+NULL_CHAR*5)',
'CUT':'write_report(NULL_CHAR*2 +chr(123)+NULL_CHAR*5)',
'COPY':'write_report(NULL_CHAR*2 +chr(124)+NULL_CHAR*5)',
'PASTE':'write_report(NULL_CHAR*2 +chr(125)+NULL_CHAR*5)',
'FIND':'write_report(NULL_CHAR*2 +chr(126)+NULL_CHAR*5)',
'MUTE':'write_report(NULL_CHAR*2 +chr(127)+NULL_CHAR*5)',
'VOLUME UP':'write_report(NULL_CHAR*2 +chr(128)+NULL_CHAR*5)',
'VOLUME DOWN':'write_report(NULL_CHAR*2 +chr(129)+NULL_CHAR*5)',
'CTRL + ALT + DEL':'write_report(chr(5)+NULL_CHAR+chr(76)+NULL_CHAR*5)',
'CTRL + w':'write_report(chr(1)+NULL_CHAR+chr(26)+NULL_CHAR*5)',
'WIN + TAB':'write_report(chr(8)+NULL_CHAR+chr(43)+NULL_CHAR*5)',
'ALT + TAB':'write_report(chr(4)+NULL_CHAR+chr(43)+NULL_CHAR*5)',
'CTRL + F':'write_report(chr(1)+NULL_CHAR+chr(9)+NULL_CHAR*5)',
'CTRL + ALT +     ARROWDOWN':'write_report(chr(5)+NULL_CHAR+chr(81)+NULL_CHAR*5)',
}

user_input = "liveuamap.com"
gas_prices = "getupside.com/locations/va/fairfax/"
top_news = "bing.com/news/search%3Fq=Top Stories%26FORM=NSBABR"


while 1:  # Create an infinite Loop
    if GPIO.input(button1) == 0:  # Look for button 1 press
        print("Button 1 Was Pressed:")
        if BS1 == False:  # If the LED is off
            GPIO.output(LED1, True)  # turn it on
            BS1 = True  # Set Flag to show LED1 is now On
            sleep(0.5)  # Delay
            #Create an empty list which we will fill later
            translated_list = []
            for letter in user_input:
                if letter in values:
                    translated_list.append(values[letter])
            if LIST == 1:
                print ("\n")
                print ("\n")
                print ("This is the translated command:")
                print ("________________________________")
                print("\n".join(translated_list))
            if EXECUTE == 1:
                exec("\n".join(translated_list))
                write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5) #auto enter afterwards
                write_report(NULL_CHAR * 8)#release keys
                write_report(chr(1)+NULL_CHAR+chr(23)+NULL_CHAR*5) #new tab
                write_report(NULL_CHAR * 8)#release keys
            link_list=[]
            for letter in gas_prices:
                if letter in values:
                    link_list.append(values[letter])
            if LIST == 1:
                print ("\n")
                print ("\n")
                print ("This is the translated command:")
                print ("________________________________")
                print("\n".join(link_list))
            if EXECUTE == 1:
                exec("\n".join(link_list))
                write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5) #auto enter afterwards
                write_report(NULL_CHAR * 8)#release keys
                write_report(chr(1)+NULL_CHAR+chr(23)+NULL_CHAR*5) #new tab
                write_report(NULL_CHAR * 8)#release keys
            new_list=[]
            for letter in top_news:
                if letter in values:
                    new_list.append(values[letter])
            if LIST == 1:
                print ("\n")
                print ("\n")
                print ("This is the translated command:")
                print ("________________________________")
                print("\n".join(new_list))
            if EXECUTE == 1:
                exec("\n".join(new_list))
                write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5) #auto enter afterwards
                write_report(NULL_CHAR * 8)#release keys
                write_report(chr(1)+NULL_CHAR+chr(23)+NULL_CHAR*5) #new tab
                write_report(NULL_CHAR * 8)#release keys

        else:  # If the LED is on
            GPIO.output(LED1, False)  # Turn LED off
            BS1 = False  # Set Flag to show LED1 is now Off
            sleep(0.5)
    if GPIO.input(button2) == 0:  # Repeat above for LED 2 and button 2
        print("Button 2 Was Pressed:")
        if BS2 == False:
            GPIO.output(LED2, True)
            BS2 = True
            sleep(0.5)
            user_input = generateEmail()
            #Create an empty list which we will fill later
            translated_list = []
            for letter in user_input:
                if letter in emailDict:
                    translated_list.append(emailDict[letter])
            if LIST == 1:
                print ("\n")
                print ("\n")
                print ("This is the translated command:")
                print ("________________________________")
                print("\n".join(translated_list))
            if EXECUTE == 1:
                exec("\n".join(translated_list))
                write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5) #auto enter afterwards
                write_report(NULL_CHAR * 8)#release keys
        else:
            GPIO.output(LED2, False)
            BS2 = False
            sleep(0.5)
    if GPIO.input(button3) == 0:  # Repeat above for LED 3 and button 3
        print("Button 3 Was Pressed:")
        if BS3 == False:  # If the LED is off
            GPIO.output(LED3, True)  # turn it on
            BS3 = True  # Set Flag to show LED1 is now On
            sleep(0.5)  # Delay
            write_report(chr(8)+NULL_CHAR+chr(21)+NULL_CHAR*5)
        user_input = "excel.exe"
        #Create an empty list which we will fill later
        translated_list = []
        for letter in user_input:
            if letter in values:
                translated_list.append(values[letter])
        if LIST == 1:
            print ("\n")
            print ("\n")
            print ("This is the translated command:")
            print ("________________________________")
            print("\n".join(translated_list))
        if EXECUTE == 1:
            exec("\n".join(translated_list))
            write_report(NULL_CHAR*2 +chr(40)+NULL_CHAR*5) #auto enter afterwards
            write_report(NULL_CHAR * 8)#release keys
        else:
            GPIO.output(LED3, False)
            BS3 = False
            sleep(0.5)
