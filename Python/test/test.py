def moda():
    words=["1","2","3"]
    print(words)
    for w in words[:]:
        print(w)
        if int(w) > 2:
            words.insert(0,w)
    print(words)
    for x in range(3,10,2):
        print(x)
if __name__ == "__main__":
    moda()
