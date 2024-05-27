# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", "r") as letter:
	letter_format = letter.read()
with open("./Input/Names/invited_names.txt", "r") as invites:
	for names in invites.readlines():
		names = names.strip()
		new_letter = letter_format.replace("[name]", f"{names}")
		with open(f"./Output/ReadyToSend/Letter to {names}.txt", "w") as file:
			file.write(new_letter)
