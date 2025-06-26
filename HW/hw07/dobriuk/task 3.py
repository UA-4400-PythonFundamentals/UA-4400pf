def char_count(text: str) -> dict[str, int]:
    result = {}
    for ch in text:
        result[ch] = result.get(ch, 0) + 1
    return result

def main():
    user_text = input("Input text:  ")
    result = char_count(user_text)
    print(result)

if __name__ == "__main__":
    main()