from poke_api import get_poke_info 
from pastebin_api import post_new_paste
import sys

def main():

    search_term = get_search_term()
    poke_info = get_poke_info(search_term)
    if poke_info:
        title, body_text = get_paste_content(poke_info, search_term)
        paste_url = post_new_paste(title, body_text, '1M')
        print(f'URL of Poke info: {paste_url}')
    return


def get_search_term():

    num_params = len(sys.argv) -1
    if num_params > 0:
        return sys.argv[1]
    else:
        print('Error: Missing search term')
        sys.exit(1)



def get_paste_content(poke_info, search_term): 

    # Prints the name of the pokemon whether the name or number was provided
    title = f"{poke_info.get('name').capitalize()}'s Abilities"

    divider = ''
    body_text = ''

    ability_portion = poke_info['abilities']
    ability_section = [a['ability'] for a in ability_portion]
    ability = [n['name'] for n in ability_section]
    for name in ability:
        body_text += f'-{name}' + '\n'
        body_text += divider + '\n'

    return title, body_text



if __name__ == "__main__":
    main()