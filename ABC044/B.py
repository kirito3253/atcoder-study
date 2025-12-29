def solve(w):
    for x in w:
        if w.count(x) % 2 == 1:
            return "No"
        
    return "Yes"

def main():
    w = input()
    print(solve(w))

if __name__ == "__main__":
    main()