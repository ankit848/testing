import requests
import random

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to submit form data
def submit_form(_token,firstname,lastname,username,email,country,mobile_code,country_code,mobile,password,password_confirmation):
    url = 'https://10.alabbd.xyz/user/register'
    data = {
        '_token':token,
      'firstname':fname,
      'lastname':'lnamer,
      'username':username,
      'email':email,
      'country':country,
      'mobile_code':mobile_code,
      'country_code':country_code,
      'mobile':mobile,
      'password':password,
     'password_confirmation':cpass
      
    }
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Origin": "https://10.alabbd.xyz/",
        "Referer": "https://10.alabbd.xyz/user/register",  # Corrected referer URL
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    response = requests.post(url, data=data, headers=headers)
    print(fname)
    print(username)
    print(email)
    print(mobile)
    print(password)
    if 'https://10.alabbd.xyz/user/dashboard' in response.url:
        print("Form submitted successfully.")
    else:
        print("Form submission failed.")

# Main function
def main():
    usponsor = 'MPL2408484'
    upass = '1234567890'
    uconpass = '1234567890'

    for _ in range(55):  # Loop 3 times
        uname = 'Radhey Radhey'
        umobile = '9800005678'
        umobile = int(umobile)  # Convert umobile back to an integer
        umobile += random.randint(100, 999)  # Add a random 3-digit number to umobile
        uemail = f'dinesh{generate_random_numbers()}p{generate_random_numbers()}@gmail.com'
            
        submit_form(usponsor, uname, umobile, uemail, upass, uconpass)

if __name__ == "__main__":
    main()
