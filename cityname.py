import datetime
import argparse
import random
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("count", nargs="?", type=int, default=15, help="Provide any whole number to generate this many city names")
    parser.add_argument("-s", "--seed", type=int, default=datetime.datetime.now(), help="Provide a random seed value here, to get reproducible results")
    parser.add_argument("--stats", action="store_true", help="Print statistics about the cityname data")
    args = parser.parse_args()

    # Load data
    with open('citynamegen_data.json') as jsonFile:
        data = json.load(jsonFile)

    # Print stats
    if args.stats == True:
        numPrefixes = len(data["prefixes"])
        numSuffixes = len(data["suffixes"])
        numParts1 = len(data["parts"][0])
        numParts2 = len(data["parts"][1])
        partsProduct = len(data["parts"][0]) * len(data["parts"][1])
        partsDoubleProduct = partsProduct * 2
        partsSuffixProduct = partsProduct * numSuffixes
        partsSuffixPrefixProduct = partsSuffixProduct * numPrefixes

        print("citynamegen_data statistics")
        print("---------------------------\n")
        print("Prefixes :", numPrefixes)
        print("Suffixes :", numSuffixes)
        print("1st parts:", numParts1)
        print("2nd parts:", numParts2)
        print("")
        print("Max. combinations of parts:", partsProduct)
        print("Max. combinations of parts and suffixes:", partsSuffixProduct)
        print("Max. combinations of parts, suffixes, and prefixes:", partsSuffixPrefixProduct)
        print("Max. combinations of parts, double names, suffixes, and prefixes:", partsDoubleProduct * numSuffixes * numPrefixes)
        print("")
        print("Probability of prefixes:", "%.2f" % ((1.0 - data["settings"]["prefixThreshold"]) * 100.0), "%")
        print("Probability of suffixes:", "%.2f" % ((1.0 - data["settings"]["suffixThreshold"]) * 100.0), "%")
        print("Probability of double names:", "%.2f" % ((1.0 - data["settings"]["doubleThreshold"]) * 100.0), "%")
        print("")

        return

    # Seed random generator
    random.seed(args.seed)

    # Generate name(s)
    if args.count > 1:
        print(data["strings"]["generating"] % args.count)
    print("")
    for _ in range(args.count):
        # Possibly add prefix
        result = ""
        if random.uniform(0.0, 1.0) > data["settings"]["prefixThreshold"]:
            result = random.choice(data["prefixes"]) + " "

        # Add city name
        result = result + random.choice(data["parts"][0]) + random.choice(data["parts"][1])

        # Possibly add double city name
        if random.uniform(0.0, 1.0) > data["settings"]["doubleThreshold"]:
            result = result + "-" + random.choice(data["parts"][0]) + random.choice(data["parts"][1])

        # Possibly add suffix
        if random.uniform(0.0, 1.0) > data["settings"]["suffixThreshold"]:
            result = result + " " + random.choice(data["suffixes"])

        # Output
        print(result)
    print("")

if __name__ == "__main__":
    main()