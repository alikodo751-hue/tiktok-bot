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
    
    # سنغير النطاق قليلاً أو نستخدم تركيبة مختلفة تماماً
    user = "".join(random.choices(string.ascii_lowercase, k=8))
    email = f"{user}@outlook.com" 
    
    params = f"device_id={did}&iid={iid}&aid=1233&version_code=300904&device_platform=android&language=en&os_version=12"
    payload = f"email={email}&type=1&app_id=1233"
    
    headers = {
        "x-gorgon": generate_advance_gorgon(params, payload),
        "x-khronos": str(int(time.time())),
        "User-Agent": "com.zhiliaoapp.musically/300904 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/TP1A.220624.021)",
        "Content-Type": "application/x-www-form-urlencoded",
        "x-tt-dm-status": "login",
        "accept-encoding": "gzip, deflate"
    }

    try:
        url = f"https://api16-normal-c-useast1a.tiktokv.com/passport/email/send_code/?{params}"
        time.sleep(random.randint(3, 7)) # تأخير واقعي
        
        response = requests.post(url, data=payload, headers=headers, timeout=20)
        res = response.json()
        
        if res.get("message") == "success":
            print(f"✅ REAL CODE SENT TO: {email}")
        else:
            print(f"❌ STATUS: {res.get('data', {}).get('description', 'Filter Blocked')}")
            
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    for i in range(1, 3):
        create_account(i)
