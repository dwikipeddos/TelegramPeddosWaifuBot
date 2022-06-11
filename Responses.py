import WaifuGetter as wg

def handle_response(input):
    input  = input.lower()

    if input == "waifu":
        return wg.get_waifu_list()
    elif input == "help":
        return help()

def welcome():
    return "Welcome to Peddos Waifu Bot!"

def help():
    return "Commands: waifu, help"