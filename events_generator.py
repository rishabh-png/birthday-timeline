# generate_events.py

def generate_events(captions_file="captions.txt"):
    events = []

    with open(captions_file, "r", encoding="utf-8") as f:
        captions = [line.strip() for line in f if line.strip()]

    for i, caption in enumerate(captions, start=1):
        event = {
            "caption": caption,
            "image": f"images/image{i}.jpeg"
        }
        events.append(event)

    print("const events=[")
    for e in events:
        print("{")
        print(f'caption:"{e["caption"]}",')
        print(f'image:"{e["image"]}"')
        print("},")
    print("];")


if __name__ == "__main__":
    generate_events()
