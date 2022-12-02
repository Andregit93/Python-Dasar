#Nama : Andre Sevtian
#NIM : 210741048


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "Andre "+ bcolors.OKGREEN + "Sevtian")

a = "Andre"
b = a[::-1]
c = " Sevtian"
d = c[::-1]

print(bcolors.OKGREEN + d + bcolors.WARNING+b)