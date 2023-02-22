import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'

DEVELOPER_API_KEY = 'ulKNUNN-aAcBiGFUDBnlnIFqHQ7alAeD'


def main():

    paste_url = post_new_paste('whatever', 'silly goose')
    pass


def post_new_paste(title, body_text, expiration='10M', listed=True):
    """ Creates a new public Pastebin paste

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): How long Paste will last. (see https://pastebin.com/doc_api) Defaults to '10M'.
        listed (bool, optional): Whether paste is listed or not. Defaults to True.

    Returns:
        str : URL of the new paste. None if unsuccessful
    """



    # Create dictionary of parameter values
    params = {
        'api_dev_key' : DEVELOPER_API_KEY,
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_name' : title,
        'api_paste_expire_date' : expiration,
        'api_paste_private' : 0 if listed else 1

    }

    # Send the POST request to the PasteBin API
    print('Posting new paste to PasteBin. . . ', end='')
    resp_msg = requests.post(API_POST_URL, data=params)

    # Check if paste was created successfully
    if resp_msg.status_code == requests.codes.ok:
        print('Success')
        return resp_msg.text 
    else:
        print('Failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Error: {resp_msg.text}')
    




if __name__ == "__main__":
    main()