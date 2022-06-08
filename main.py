import settings

conf = settings.SETTINGS
version = settings.VERSION

if conf['settings']['credit']:
    print(f"Text Adventure Generator {version} by Wooferz")
