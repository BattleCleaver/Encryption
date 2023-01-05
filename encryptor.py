import os
import base64

def encrypt_image(filetype_path,dest_folder):
    # Read the image file in binary
    with open(filetype_path, 'rb') as image_file:
        image_content = image_file.read()

    # Encrypt the image file
    encrypted_content = base64.b64encode(image_content)

    # Get the image file name
    image_name = os.path.basename(filetype_path)

    # Create the destination path for the encrypted image
    dest_path = os.path.join(dest_folder, image_name)
    
    # Write the encrypted image to the destination path
    with open(dest_path, 'wb') as image_file:
        image_file.write(encrypted_content)

    # Delete the original image file
    os.remove(filetype_path)

def decrypt_image(filetype_path, dest_folder):
    # Read the encrypted image file in binary
    with open(filetype_path, 'rb') as image_file:
        encrypted_content = image_file.read()

    # Decrypt the image file
    decrypted_content = base64.b64decode(encrypted_content)

    # Get the image file name
    image_name = os.path.basename(filetype_path)

    # Create the destination path for the decrypted image
    dest_path = os.path.join(dest_folder, image_name)

    
    # Write the decrypted image to the destination path
    with open(dest_path, 'wb') as image_file:
        image_file.write(decrypted_content)

    # Delete the encrypted image file
    os.remove(filetype_path)

def read_password(video_directory):
    # Read the password from the password file
    password_file_path = os.path.join(video_directory, 'password.txt')
    with open(password_file_path, 'r') as password_file:
        password = password_file.read().strip()
    return password

def main():
    # Get the path to the desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #I've decided to retrieve my images/videos that i stored on desktop.
    # Get the path to the Steam dumps folder
    steam_path = os.path.expandvars('%ProgramFiles(x86)%\\Steam') 
    dumps_path = os.path.join(steam_path, 'dumps') # this is where the encrypted files go
    
    # Get the paths of all image files on the desktop
    image_paths = [os.path.join(desktop_path, f) for f in os.listdir(desktop_path) if f.endswith('.jpeg') or f.endswith('.gif') or f.endswith('.jpg') or f.endswith('.mp4')]

    # Read the password from the password file
    video_directory = 'C:\\Users\\amali\\Videos' # this is the password.txt location in your directory of choice
    password = read_password(video_directory) # write the password inside the .txt file.

    # Prompt the user for the password
    user = input("Password: ")
    
    if user == password:
        print(f"\nImages/Videos Found in Desktop: {len(image_paths)}")            

        print("\n--------------------")
        print("| COMMAND |   KEY  |")
        print("--------------------")
        print("| Decrypt |    D   |")
        print("| Encrypt |    E   |")
        print("| EXIT    |    q!  |")
        print("--------------------")
        
        while True:
            command = input('\nCommand to Execute (D/E/q!): ')
            if command == 'q!':
                break

            elif command == 'E':
                # Encrypt all image files on the desktop
                for image_path in image_paths:
                    encrypt_image(image_path, dumps_path)
                print('Encryption complete.')
            
            elif command == 'D':
                # Get the paths of all image files in the Steam dumps folder
                encrypted_image_paths = [os.path.join(dumps_path, f) for f in os.listdir(dumps_path) if f.endswith('.jpeg') or f.endswith('.gif') or f.endswith('.jpg') or f.endswith('.mp4')]

                # Decrypt all image files in the Steam dumps folder
                for image_path in encrypted_image_paths:
                    decrypt_image(image_path, desktop_path)
                print('Decryption complete.')
            else:
                print('Invalid command.')

    else:
        print('Incorrect password.')

if __name__ == '__main__':
    main()

           
