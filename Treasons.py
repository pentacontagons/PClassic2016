def anagram_tester(word_list):
    """
    
    :param word_list: list of words
    :return: largest set of words that are all anagrams in alphabetical order
    
    """

    sList = word_list[0:]
    for i in range(0,len(sList)):
        sList[i] = sorted(''.join(sList[i]))
    sList = sorted(sList)
    longest = 1
    current = 1
    best = ""
    for i in range(1,len(sList)):
        if(sList[i] == sList[i-1]):
            current+=1
        else:
            if(current>longest):
                best = sList[i-1]
                longest = current
                current = 1
    if(current>longest):
        longest = current
        best = sList[-1]

    listOf = []
    for i in range(0,len(word_list)):
        if(sorted(word_list[i]) == sorted(best)):
            listOf.append(word_list[i])

    listOf.sort()
    return listOf


def parse_file_and_call_function():
    g = open("TreasonsOUT.txt","w")
    with open("TreasonsIN.txt", "r") as f:
        line = f.readline()
        test_cases = line.split('|')
        for test_case in test_cases:
            test_case = [s for s in test_case.split(' ') if len(s.strip()) > 0]
            if len(test_case) > 0:
                ans = anagram_tester(test_case)
                g.write('[{}]'.format(', '.join(ans)))
                g.write("\n")
                print '[{}]'.format(', '.join(ans))
    g.close()


if __name__ == "__main__":
    parse_file_and_call_function()
