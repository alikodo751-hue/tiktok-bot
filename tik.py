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
    print(f"--- Deep Stealth Attempt #{index} ---")
    did = "".join(random.choices(string.digits, k=19))
    iid = "".join(random.choices(string.digits, k=19))
    
    user = "".join(random.choices(string.ascii_lowercase, k=8))
    email = f"{user}@abbas.linkpc.net" 
    
    params = f"device_id={did}&iid={iid}&aid=1233&version_code=300904&device_platform=android&language=en&os_version=12"
    payload = f"email={hashlib.md5(email.encode()).hexdigest() if random.random() > 0.5 else email}&type=1&app_id=1233"
    
    session = requests.Session()
    
    headers = {
        "x-gorgon": generate_advance_gorgon(params, payload),
        "x-khronos": str(int(time.time())),
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro Build/TP1A.220624.021; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 TikTok/30.9.4",
        "Content-Type": "application/x-www-form-urlencoded",
        "x-tt-dm-status": "login",
        "x-tt-token": "".join(random.choices(string.ascii_letters + string.digits, k=40)),
        "accept-encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Accept": "*/*"
    }

    try:
        url = f"https://api16-normal-c-useast1a.tiktokv.com/passport/email/send_code/?{params}"
        
        jitter = random.uniform(5.0, 15.0)
        time.sleep(jitter)
        
        response = session.post(url, data=payload, headers=headers, timeout=25)
        res = response.json()
        
        if res.get("message") == "success":
            print(f"✅ REAL CODE REQUESTED FOR: {email}")
            print(f"[*] CHECK YOUR SNIPER ON abbas.linkpc.net")
        else:
            description = res.get('data', {}).get('description', 'IP Rate Limited')
            print(f"❌ STATUS: {description}")
            
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    for i in range(1, 3):
        create_account(i)
