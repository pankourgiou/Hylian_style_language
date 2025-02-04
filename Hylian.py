def convert_to_hylian(text):
    """Convert regular text to Hylian-inspired symbols."""
    char_map = create_hylian_char_map()
    return ''.join(char_map.get(char, char) for char in text)

def main():
    print("=== ⤌⤂⤃ ⤂⤤⤝⤁⟊⤆ ⤌⤃⤥⤌ ⤇⤭⤆⤴⤃⤰⤌⤃⤰ ===")
    print("\nSpeak, traveler of Hyrule...")
    try:
        while True:
            user_input = input("\nEnter text to convert (Ctrl+C to exit):\n> ")
            hylian_text = convert_to_hylian(user_input)
            print("\nHylian Script:")
            print(hylian_text)
            print("－" * 50)
            
            # Also show a more decorative version
            print("\nDecorative Border:")
            border = "⟰" * (len(hylian_text) + 4)
            print(f"╔{border}╗")
            print(f"║ {hylian_text} ║")
            print(f"╚{border}╝")
            print("－" * 50)
    except KeyboardInterrupt:
        print("\n\nFarewell, brave soul... ⤌⤂⤃ ⤌⤁⤫⤃ ⤂⤊⤱ ⤇⤭⤫⤃...")

if __name__ == "__main__":
    main()
