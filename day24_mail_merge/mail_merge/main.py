PLACEHOLDER = "[name]"
OUT_FILE = "./Output/ReadyToSend/letter_for_"

with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("./Input/Letters/starting_letter.txt") as f:
    contents = f.read()
    for name in names:
        s_name = name.strip()
        n_letter = contents.replace(PLACEHOLDER, s_name)
        with open(f"{OUT_FILE}{s_name}.txt", mode="w") as nf:
            nf.write(n_letter)