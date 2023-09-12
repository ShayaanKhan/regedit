import winreg

# Fixed key path
key_path = r"SOFTWARE\\TempOrg\\TempKey"

def create_registry_key(value_name, value_data):
    try:
        # Open the registry key for writing
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        
        # Set a value (optional)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
        print("Registry key created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if key:
            # Close the registry key if it was opened
            winreg.CloseKey(key)

def delete_registry_key():
    try:
        # Open the registry key for deletion
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
        print("Registry key deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def modify_registry_value(value_name, new_value_data):
    try:
        # Open the registry key for modification
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        # Modify the value
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_value_data)
        print("Registry value modified successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if key:
            # Close the registry key if it was opened
            winreg.CloseKey(key)

# User menu
while True:
    print("\nOptions:")
    print("1. Create Registry Key")
    print("2. Delete Registry Key")
    print("3. Modify Registry Value")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        value_name = input("Enter the value name: ")
        value_data = input("Enter the value data: ")
        create_registry_key(value_name, value_data)
    elif choice == '2':
        delete_registry_key()
    elif choice == '3':
        value_name = input("Enter the value name to modify: ")
        new_value_data = input("Enter the new value data: ")
        modify_registry_value(value_name, new_value_data)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")
