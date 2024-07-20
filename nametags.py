import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
        
    for name in sys.argv[1:]:
        print_tag(name)



def print_tag(name):
    print("=" * (len(name) + 8))
    print(f">>> {name}")
    print("=" * (len(name)+8))

main()