dictionary = {
    'apple': '사과',
    'love': '사랑',
    'hello': '안녕'
}

def caesar_cipher_decode(target_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    results = []

    for shift in range(1, 26):
        decoded = ''
        for ch in target_text:
            if ch.isalpha():  # 알파벳만 치환
                lower = ch.lower()
                idx = alphabet.index(lower)
                new_idx = (idx - shift) % 26
                new_ch = alphabet[new_idx]
                # 원래 문자가 대문자였다면 대문자로 복원
                decoded += new_ch.upper() if ch.isupper() else new_ch
            else:
                decoded += ch
        results.append(decoded)
        print(f'[{shift:02d}] {decoded}')
        
        # dictionary에 있는 단어가 포함되어있는지 확인
        token = set(decoded.lower().split())
        is_match = token & dictionary.keys()
        if  is_match:
            return results

    return results


def main():
    try:
        # 1. password.txt 읽기
        with open('password.txt', 'r', encoding='utf-8') as f:
            target_text = f.read().strip()

        # 2. 해독 시도
        print('--- 카이사르 암호 해독 시작 ---')
        results = caesar_cipher_decode(target_text)

        # 3. 눈으로 보고 맞는 자리수 입력
        choice = input('\n몇 번째 자리수로 해독된 결과가 맞나요? (숫자 입력) : ')
        try:
            idx = int(choice)
            if 1 <= idx <= 25:
                decoded_text = results[idx - 1]
                # 4. 결과 저장
                with open('result.txt', 'w', encoding='utf-8') as f:
                    f.write(decoded_text)
                print(f'\n✅ result.txt에 결과가 저장되었습니다.')
            else:
                print('❌ 유효하지 않은 번호입니다.')
        except ValueError:
            print('❌ 숫자를 입력하세요.')

    except FileNotFoundError:
        print('❌ password.txt 파일을 찾을 수 없습니다.')
    except Exception as e:
        print(f'⚠️ 오류 발생: {e}')


if __name__ == '__main__':
    main()
