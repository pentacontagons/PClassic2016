def pythagorean_triples(c):
    """

    :param c: the length of the aqueduct you want to construct.
    :return: a list containing all possible configurations of the other two
             sides that are of positive integer length. Output each
             configuration as a separate element in a list in the format a b
             where a is in ascending order and b is in descending order in
             respect to the other configurations.
    """

    # TODO: implement

    listOf = []
    for b in range(1,c):
        l = (c**2-b**2)**.5
        if(-.00001<l-round(l)<.00001):
            listOf.append(int(round(b)))
            listOf.append(int(round(l)))
    return listOf


def parse_file_and_call_function():
    g = open("TrickyOUT.txt","w")
    with open("TrickyIN.txt", "r") as f:
        for line in f:
            j = list(pythagorean_triples(int(line)))
            print(j)
            g.write(str(j))
            g.write("\n")

    g.close()


if __name__ == "__main__":
    parse_file_and_call_function()
