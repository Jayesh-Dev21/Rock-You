import zipfile

def try_password(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print(f"✅ Success: The password is '{password}'")
        return True
    except RuntimeError:
        return False
    except Exception as e:
        print(f"❌ Error trying '{password}': {e}")
        return False

def brute_force_zip(zip_path, rockyou_path):
    correct_password = None
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        with open(rockyou_path, 'r', encoding='latin-1') as f:
            for password in f:
                password = password.strip()
                print(f"🔍 Trying password: {password}")
                if try_password(zip_file, password):
                    correct_password = password
                    break
    return correct_password

def passwordFound(pwd):
    if pwd:
        print(f"🎉 Password found: {pwd}")
    else:
        print("❌ Password not found.")

if __name__ == "__main__":
    zip_path = "Path_to_zip"
    rockyou_path = "Path_to_Wordlist" # use custom wordlist as well
    final = brute_force_zip(zip_path, rockyou_path)
    passwordFound(final)
