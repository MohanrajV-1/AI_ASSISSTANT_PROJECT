import wolframalpha

# Your Wolfram Alpha API Key
app_id = "LEQAU6-E3K83TP568"
def WolfRamAlpha(query):
    client = wolframalpha.Client(app_id)
    print("Query to WolframAlpha:", query)
    res = client.query(query)
    answer = next(res.results).text
    return answer



def Calc(query):
    if query.strip() != "":
        result = WolfRamAlpha(query)
        print("Answer:", result)
    else:
        print("Invalid Input!")
