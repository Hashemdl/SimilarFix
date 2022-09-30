import os
from tqdm import tqdm
from time import sleep
from colorama import init as colorinit
from colorama import Fore


# --------- colors -----------

colorinit(autoreset=True)
CYAN = Fore.CYAN
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
LBLUE = Fore.LIGHTBLUE_EX
RESET = Fore.RESET


# ====== path project =======
path =  os.getcwd()
result_file = "results.txt"
# ===========================

# Empty list for Save lists
all_lines = []
#--------------------------

def header():
    ''' Script Banner '''

    ls = " "*10 # Left Space
    logo = f'''

    {ls}▄██████████████▄▐█▄▄▄▄█▌
    {ls}███████████████▌▀▀██▀▀
    {ls}████▄████████████▄▄█▌
    {ls}▄▄▄▄▄██████████████▀

    '''
    title = ls + "Similar Fix Txt V0.1"
    print(f"{CYAN}{logo}{RESET}{LBLUE}{title}\n")


def GetTextFiles() -> list:
    ''' Get All text in Root Project '''
    files = os.listdir(path)

    # don't count res file
    check = lambda x : not x == result_file

    txts = [x for x in files if x.endswith(".txt") and check(x)]
    return txts


def ReadTxt(file:str) -> list:
    ''' text readlines '''
    with open(file, "r") as file_txt:

        lines = [str(x).strip() for x in file_txt.readlines()]

    return lines


def Save(val:set) -> None:
    ''' Create New Txt Files '''
    with open(result_file, "a") as res:
        for x in tqdm(val, colour="GREEN"):
            res.write(f"{x}\n")


if __name__ == "__main__":

    # ------- Change Console title and Size -------
    os.system("title SimilarFix")
    os.system("mode con cols=50 lines=20")
    # end -------------------------------


    # ------ About Script ---------
    header()
    # ----------------------------

    files = GetTextFiles()
    show_files_count = f"{RED if len(files) == 0 else GREEN}{len(files)}{RESET}"
    print(f" > [Total Files Found : {show_files_count} ]\n")

    if len(files) != 0:
        for x in tqdm(files, colour="YELLOW"):
            result = ReadTxt(x)
            all_lines.append(result)

        all_res = set().union(*all_lines)
        print(f"{YELLOW} > Total lines Found : {len(all_res)} \n")


        Save(all_res)
        print(f"{GREEN} > DONE :) \n")

    else:
        print(f" >{RED} TXT File Not Found ! :(")
        sleep(2)
    

    # --------------- about me --------------------
    print(f" > Dev With {RED}♥{RESET} BY : @PYTKM")
    sleep(2)