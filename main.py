import settings
from colorama import Fore, Back, Style, init

init(autoreset=True)

conf = settings.SETTINGS
version = settings.VERSION

if conf['settings']['credit']:
    print(f"Text Adventure Generator {version} by Wooferz")
try:
    conf['settings']['title']
    conf['settings']['author']
except KeyError:
    pass
else:
    print(conf['settings']['title'], "by", conf['settings']['author'])


def colour_text(text):
    text = text.replace("[red]", Fore.RED).replace("[blue]", Fore.BLUE).replace(
        "[green]", Fore.GREEN).replace("[yellow]", Fore.YELLOW).replace("[reset]", Fore.RESET + Back.RESET + Style.RESET_ALL)
    return text


def space():
    print("\n")


def run_scenario(scenario):
    space()
    print(colour_text(scenario['text']))
    space()
    try:
        scenario['children']
    except KeyError:
        exit()

    a = 1
    for i in scenario['children']:
        print(colour_text(f"{a}. {i['option_text']}"))
        a += 1
    space()
    while True:
        inp = input("Selct option:\n")
        try:
            int(inp)
        except ValueError:
            print("Invalid Option")
        else:
            inp = int(inp)
            if inp > 0 and inp < a:
                break
            else:
                print("Invalid Option")
    run_scenario(scenario['children'][int(inp)-1])


run_scenario(conf["game"])
