# compliment = dict()
# compliment["T"] = "A"
# compliment["A"] = "T"
# compliment["C"] = "G"
# compliment["G"] = "C"

compliment = {
    "T": "A",
    "A": "T",
    "C": "G",
    "G": "C"
}



for base in sequence:
    result += compliment[base]



select base:
    case "T":
        result += "A"
    case "A":
        result += "T"
