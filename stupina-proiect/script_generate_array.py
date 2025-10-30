# script_generate_array.py
# Rulează-l în același folder cu comentarii.txt

input_file = "comentarii.txt"
output_file = "comentarii_array.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# separăm comentariile după linia "0"
blocuri = text.split("\n0\n")

# pregătim array JS
js_array = "const comentarii = [\n"

for bloc in blocuri:
    bloc_curat = bloc.strip()
    if bloc_curat:  # ignorăm blocurile goale
        # înlocuim backticks dacă există în text
        bloc_curat = bloc_curat.replace("`", "'")
        js_array += f"`{bloc_curat}`,\n"

js_array += "];\n"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(js_array)

print(f"Array JS generat în {output_file}.")
