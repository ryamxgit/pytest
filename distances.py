distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = convert(float(distances[spacecraft]))
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    except KeyError:
        print(f"{spacecraft} don't exists in our DB")
        return
    print(f"{spacecraft} is {au:,.1f} meters away")

def convert(distance):
    return distance * 149597870700

main()