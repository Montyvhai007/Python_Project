# Available formatting constants are:
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
print(Fore.GREEN+Back.BLUE+"Subcribe IT FIRM BD"+Fore.BLUE+Back.GREEN+"Subcribe IT FIRM BD")
print(Style.DIM+Fore.RED+"Subcribe IT FIRM BD")
print(Style.BRIGHT+Fore.RED+"Subcribe IT FIRM BD")
