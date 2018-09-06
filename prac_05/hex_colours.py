
HEX_COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
               "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

hex_name = input("Enter hex name: ")
while hex_name != "":
    if hex_name in HEX_COLOURS:
        print("{:<3} is {}".format(hex_name, HEX_COLOURS[hex_name]))
    else:
        print("Invalid hex code")
    hex_name = input("Enter hex name: ")

