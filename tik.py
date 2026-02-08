import requests
import time
import random
import string
import hashlib

def generate_advance_gorgon(url_params, data):
    def md5(s): return hashlib.md5(s.encode()).hexdigest()
    str_to_hash = f"{md5(url_params)}{md5(data)}"
    return "0408" + md5(str_to_hash)[:28]

def create_account(index):
    print(f"[*] Starting attempt ({index})...")
    did = "".join(random.choices(string.digits, k=19))
    iid = "".join(random.choices(string.digits, k=19))
    email = f"user_{''.join(random.choices(string.ascii_lowercase, k=7))}@abbas.linkpc.net"
    password = "Abbas" + "".join(random.choices(string.digits, k=5))
    
    params = f"device_id={did}&iid={iid}&aid=1233&version_code=200204&device_platform=android"
    payload = f"email={email}&type=1&app_id=1233"
    
    headers = {
        "x-gorgon": generate_advance_gorgon(params, payload),
        "x-khronos": str(int(time.time())),
        "User-Agent": "com.zhiliaoapp.musically/2022403040 (Linux; U; Android 12)",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        url = f"https://api16-normal-c-useast1a.tiktokv.com/passport/email/send_code/?{params}"
        response = requests.post(url, data=payload, headers=headers, timeout=20)
        res = response.json()
        
        if res.get("message") == "success":
            result = f"Email: {email} | Pass: {password} | DID: {did}"
            print(f"✅ Success: {result}")
            with open("accounts_created.txt", "a") as f:
                f.write(result + "\n")
        else:
            print(f"❌ Failed: {res.get('data', {}).get('description', 'Unknown Error')}")
            
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    for i in range(1, 4):
        create_account(i)
        time.sleep(5)
