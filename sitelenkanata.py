import tkinter as tk

characters_dict = {
    'e': 'ᐁ',
    'a': 'ᐊ',
    'o': 'ᐅ',
    'i': 'ᐃ',
    'u': 'ᐆ',
    'n' : 'ᓐ',
    'pe': 'ᐯ',
    'pa': 'ᐸ',
    'po': 'ᐳ',
    'pi': 'ᐱ',
    'pu': 'ᐴ',
    'te': 'ᑌ',
    'ta': 'ᑕ',
    'to': 'ᑐ',
    'ti': 'ᑎ',
    'tu': 'ᑑ',
    'ke': 'ᑫ',
    'ki': 'ᑭ',
    'ko': 'ᑯ',
    'ka': 'ᑲ',
    'ku': 'ᑰ',
    'me': 'ᒣ',
    'mi': 'ᒥ',
    'mo': 'ᒧ',
    'ma': 'ᒪ',
    'mu': 'ᒨ',
    'ne': 'ᓀ',
    'ni': 'ᓂ',
    'no': 'ᓄ',
    'na': 'ᓇ',
    'nu': 'ᓅ',
    'le': 'ᓓ',
    'li': 'ᓕ',
    'lo': 'ᓗ',
    'la': 'ᓚ',
    'lu': 'ᓘ',
    'se': 'ᓭ',
    'si': 'ᓯ',
    'so': 'ᓱ',
    'sa': 'ᓴ',
    'su': 'ᓲ',
    'je': 'ᔦ',
    'ji': 'ᔨ',
    'jo': 'ᔪ',
    'ja': 'ᔭ',
    'ju': 'ᔫ',
    'we': 'ᕓ',
    'wa': 'ᕙ',
    'wo': 'ᕗ',
    'wi': 'ᕕ',
    'wu': 'ᕘ'
}

def replace_latin_with_indigenous(paragraph, characters_dict):
    result = ''
    i = 0
    while i < len(paragraph):
        # Check for pairs of Latin characters
        current_pair = paragraph[i:i+2].lower()
        if current_pair in characters_dict:
            # Replace with the corresponding indigenous character
            result += characters_dict[current_pair]
            i += 2  # Skip the next character in the pair
        else:
            # If not a pair, check for single Latin characters
            if paragraph[i].lower() in characters_dict:
                result += characters_dict[paragraph[i].lower()]
            else:
                result += paragraph[i]
            i += 1
    return result
    
def replace_indigenous_with_latin(text, characters_dict):
    result = ''
    i = 0
    while i < len(text):
        # Check for pairs of indigenous characters
        current_pair = text[i:i+2]
        if current_pair in characters_dict.values():
            # Replace with the corresponding Latin character
            latin_char = next(key for key, value in characters_dict.items() if value == current_pair)
            result += latin_char
            i += 2  # Skip the next character in the pair
        else:
            # If not a pair, check for single indigenous characters
            if text[i] in characters_dict.values():
                latin_char = next(key for key, value in characters_dict.items() if value == text[i])
                result += latin_char
            else:
                result += text[i]
            i += 1
    return result

def update_output():
    input_text = input_entry.get("1.0", "end-1c")
    use_first_function = use_first_function_var.get()

    if use_first_function:
        output_text = replace_latin_with_indigenous(input_text, characters_dict)
    else:
        output_text = replace_indigenous_with_latin(input_text, characters_dict)

    output_text_widget.delete("1.0", "end")
    output_text_widget.insert("1.0", output_text)

# Create the main window
root = tk.Tk()
root.title("ilo sitelen Kanata")

# Input
input_label = tk.Label(root, text="sitelen:")
input_label.pack()

input_entry = tk.Text(root, height=5, width=40)
input_entry.pack(expand=True, fill=tk.BOTH)  # Expands both horizontally and vertically

# Checkbox for function selection
use_first_function_var = tk.BooleanVar()
use_first_function_checkbox = tk.Checkbutton(root, text="kepeken e sitelen Kanata", variable=use_first_function_var)
use_first_function_checkbox.pack()

# Output
output_label = tk.Label(root, text="sitelen sin:")
output_label.pack()

output_text_widget = tk.Text(root, height=5, width=40)
output_text_widget.pack(expand=True, fill=tk.BOTH)  # Expands both horizontally and vertically

# Button to trigger transformation
transform_button = tk.Button(root, text="open", command=update_output)
transform_button.pack()

# Start the Tkinter event loop
root.mainloop()