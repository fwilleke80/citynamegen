import argparse
import random
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("count", nargs="?", type=int, default=15, help="Provide any whole number to generate this many city names")
    args = parser.parse_args()

    # Load data
    with open('citynamegen_data.json') as jsonFile:
        data = json.load(jsonFile)

    if args.count > 1:
        print(data["strings"]["generating"] % args.count)

    # Generate name(s)
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