
# python wifi_passwords_windows.py


import subprocess

def get_saved_wifi_profiles():
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    profiles = []
    for line in result.stdout.split("\n"):
        if "All User Profile" in line:
            profile = line.split(":")[1].strip()
            profiles.append(profile)
    return profiles

def get_wifi_password(profile):
    result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if "Key Content" in line:
            return line.split(":")[1].strip()
    return None

def main():
    profiles = get_saved_wifi_profiles()
    for profile in profiles:
        password = get_wifi_password(profile)
        print(f"Profile: {profile}")
        print(f"Password: {password if password else 'N/A'}")
        print("-" * 30)

if __name__ == "__main__":
    main()
