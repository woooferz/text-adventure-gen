import settings
from colorama import Fore, Back, Style, init

init(autoreset=True)

conf = settings.SETTINGS
version = settings.VERSION
version_id = settings.VERSION_ID
game_versions_id = conf['settings']['versions_supported']

if not version_id in game_versions_id:
    print(Fore.RED + "Unsupported Version Installed for that Text Adventure")
    exit(1)

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


try:
    run_scenario(conf["game"])
except KeyboardInterrupt:
    print(colour_text("\n\n[red]Exiting..."))
    exit()
except KeyError:
    print(colour_text(
        "[red]Something went wrong in the config, probably."))
