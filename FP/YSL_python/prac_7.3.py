from YSL_io import *

circular = "Circular regarding Swachh Bharat Mission: PM requests all citizens of India to take part in this mission and share your comments!"
with open("prac_7.3_text1", "w") as f:
    f.write(circular)

with open("prac_7.3_text1", "r") as f:
    circular = f.read()
    printGRN(circular)

cmnts = [
    "We want government to arrange for more dustbins in rural areas",
    "More public toilets should be made",
    "Penalties on spitting or throwing waste here and there should be increased"
]

circular_2 = ''

for line in circular.split("\n"):
        circular_2 += f"{line}\n"

circular_2 += f"\n{len(cmnts)} Public Suggestions : \n\n"
for i, c in enumerate(cmnts):
    circular_2 += f"{i+1}. {c}\n"

with open("prac_7.3_text2", "w") as f:
    f.write(circular_2)
