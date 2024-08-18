import requests

def download_image(url, save_path):
    try:
        response = requests.get(url, timeout=10)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the image
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded successfully and saved at {save_path}")
        else:
            print(f"Error: {response.status_code} - Unable to download image from {url}")
    except Exception as e:
        print(f"An error occurred: {e}")


def remove_spaces_and_slashes(input_string):
    # Remove spaces
    no_spaces = input_string.replace(" ", "")
    
    # Remove slashes
    no_slashes = no_spaces.replace("/", "")
    
    return no_slashes

def download_images_from_results(results, folder_path):
    if 'items' not in results:
        print('No result !!\nres is: {}'.format(results))
    else:
        for item in results['items']:
            print('{}:\n\t{}'.format(item['title'], item['link']))
            image_title = remove_spaces_and_slashes(item['title'])
            download_image(item['link'], f'{folder_path}/{image_title}.jpg')

