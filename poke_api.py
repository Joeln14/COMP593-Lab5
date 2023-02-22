import requests 

poke_info_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():

    info = get_poke_info(' PikaCHU   ')
    pass


def get_poke_info(poke_name_or_num):
    """ Fetches information about pokemon from the PokeAPI

    Args:
        poke_name_or_num (str): name or number of any pokemon

    Returns:
        dictionary : all information about requested pokemon 
    """

    # Convert parameter to lower case and remove leading or trailing whitespace
    poke_name = poke_name_or_num.lower()
    final_poke_search = poke_name.strip()

    # Send a get request for pokemon information 
    print(f'Getting information for {final_poke_search.capitalize()} . . . ', end='')
    resp_msg = requests.get(f'{poke_info_URL}{final_poke_search}')

    # Check whether the request was successful 
    if resp_msg.ok:
        print('Success')
        info_dict = resp_msg.json()
        return info_dict

    else:
        print('Failure')
        print(f'Responce code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Error: {resp_msg.text}')





if __name__ == "__main__":
    main()