def mktable(data, hdr):
    """Try rendering a table with tabulate if existing, or self.
    """
    import tabulate
    return tabulate.tabulate(data, headers=hdr, tablefmt="grid")




def pr():
    input("Press RET to continue")


def sps():
    print("\n"*10)


def cl():
    print("\n"*100)



def list_single(items, topic):
    seli=0
    while True:
        sps()
        print("%s:" % topic)
        for i in range(0, len(items)):
            s = "    "
            if seli == i:
                s = "  * "
            print(s + items[i])
        print()
        x = input("(ret:next c|#:confirm q:abort) ")

        if x == "":
            seli+=1
            seli%=len(items)

        if x == "c" or x == "#":
            print("select:%d,%s" % (seli, items[seli]))
            return seli

        if x == "q":
            print("abort")
            return None

def list_multi(items, topic):
    seli=0
    toggles = [0] * len(items)
    print(toggles)
    while True:
        sps()
        print("%s:" % topic)
        for i in range(0, len(items)):
            s = "    "
            if seli == i:
                s = "  * "
            mi = "  [ ] "
            if toggles[i]==1:
                mi = "  [x] "
            print(s + mi + items[i])
        print()
        x = input("(SPC:toggle+move ret:move -:move-up 0:move-top e:move-end c|#:confirm a:all n:none q:abort) ")

        if x == "0":
            seli=0

        if x == "-":
            seli=seli-1
            if seli < 0:
                seli = len(items)-1

        if x == "e":
            seli=len(items)-1

        if x == "":
            seli+=1
            seli%=len(items)

        if x == "a":
            toggles = [1] * len(items)

        if x == "n":
            toggles = [0] * len(items)

        if x == "c" or x == "#":
            print("confirm")
            res = []
            for i in range(0, len(items)):
                if toggles[i]==1:
                    res.append(i)
            return res

        if x == " ":
            toggles[seli] = 1 - toggles[seli]
            seli+=1
            seli%=len(items)

        if x == "q":
            print("abort")
            return None



def msg(lines=""):
    sps()
    if lines == None:
        lines=""
    for line in lines.split("\n"):
        print(line)
    print()
    x = input("(ret:continue) ")



def yesno(q):
    x = list_single(["yes", "no"], q)
    return x == 0
