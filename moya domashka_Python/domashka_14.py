RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

my_name = "Алексей"
age = 33

order = f"Привет, меня зовут {RED}{my_name}!{RESET}\nИ мне {GREEN}{age}{RESET} года)\nИ я учусь на курсе {YELLOW}Python{RESET},\nВ самой крутой it Школе {BLUE}Академия ТОП!{RESET}\nИ у нас самый клевый и общительный Ментор {RED}Владимир!{RESET}\n\n\tЯ очень хочу научиться языку {GREEN}Python!{RESET}\n\tИ писать {YELLOW}свои{RESET} программы на {BLUE}нем){RESET}\n\n\t\t{RED}PS:{RESET} символов в этом тексте:"

print(order,f"{len(order)}")

