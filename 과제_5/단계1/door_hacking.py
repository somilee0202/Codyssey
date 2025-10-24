# door_hacking.py
import zipfile
import itertools
import string
import time

def unlock_zip():
    zip_filename = "emergency_storage_key.zip"
    chars = string.ascii_lowercase + string.digits  # 소문자 + 숫자
    start_time = time.time()
    attempt = 0

    with zipfile.ZipFile(zip_filename) as zf:
        for pwd in itertools.product(chars, repeat=6):
            attempt += 1
            password = ''.join(pwd)
            try:
                zf.extractall(pwd=bytes(password, 'utf-8'))
                print(f"[SUCCESS] 비밀번호: {password}")
                with open("password.txt", "w") as f:
                    f.write(password)
                break
            except:
                if attempt % 100000 == 0:
                    elapsed = time.time() - start_time
                    print(f"[{attempt}회 시도, 경과 시간: {elapsed:.2f}초]")
        end_time = time.time()
        print(f"총 시도 횟수: {attempt}, 총 소요 시간: {end_time - start_time:.2f}초")

if __name__ == "__main__":
    unlock_zip()
