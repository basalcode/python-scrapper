def printArguments(*arguments):
    print(arguments)

printArguments(1, 2, 3, "a", "b", "c", True, False)

def printKeywordArguments(**keywordArguments):
    print(keywordArguments)

printKeywordArguments(number=1, string="a", boolean=True)