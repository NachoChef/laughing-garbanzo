import matplotlib.pyplot as plt
import urllib.request
import json

def  check(w:str, i:tuple, p:tuple, c:int):
    #checks a given string against two lists and makes sure it isn't a number, will return true if good
    if w not in i and not any(x for x in p if x in w) and not w.isdigit() and w.isalpha():
        if len(w) > c:
            return True
    return False

def  processURL(u:str, c:int):
    opener = urllib.request.FancyURLopener({})
    file = opener.open(u)
    segment = str(file.read())

    words = {}
    for line in segment.split():
        for word in line.split():
            if check(word.lower(), irrelevant, punctuation, c):
                if word.lower() not in words:
                    words[word.lower()] = 1
                else:
                    words[word.lower()] += 1
    words2 = {}
    for key in words:
        if words[key] > c:
            words2[key] = words[key]
    return words2

def  processTop(d:dict):
    top = "according"
    for i in d.keys():
        if d[i] > d[top]:
            top = i
    return top

def  write(d:dict, f:str):
    with open(f, 'w') as file:
        json.dump(d, file)

def  read(f:str):
    with open(f, 'r') as file:
        try:
            entries  = json.load(file)
        except ValueError:
            entries = {}
    return entries


#some words to ignore
irrelevant = ('aboard','about','above','across','after','against','along','amid','among','around','as','at'\
                ,'before','behind','below','beneath','beside','besides','between','beyond','but','by','concerning'\
                ,'considering','despite','down','during','except','excepting','excluding','following','for','from'\
                ,'in','inside','like','minus','of','off','on','onto','opposite','outside','over','past','per','plus'\
                ,'regarding','round','save','since','than','through','to','toward','towards','under','underneath'\
                ,'unlike','until','up','upon','versus','via','with','within','without','his','her','i','they',\
                'he','she','that','there','a','the','was','him','and','is','we','you','your')
#skipping punctuation
punctuation = ('"', "'", '.', ',', '-',':','@','$', '=')
'''
#remove words with less than CULL occurrences
cull = 3
dict1 = processURL("http://www.cnn.com/2016/12/02/politics/donald-trump-taiwan/index.html", cull)
dict2 = processURL("http://www.cnn.com/2016/11/30/politics/supreme-court-detained-immigrants/index.html", cull)
dict3 = processURL("http://www.cnn.com/2016/11/27/politics/bernie-sanders-electoral-college/index.html", cull)
dict4 = processURL("http://www.cnn.com/2016/11/23/politics/nikki-haley-picked-for-un-ambassador/index.html", cull)
dict5 = processURL("http://www.cnn.com/2016/11/22/politics/reid-wilson-party-people-podcast/index.html", cull)

result = {**dict1, **dict2, **dict3, **dict4, **dict5}
write(result, "try1.json")
words = sorted(list(result.keys()))
print("Total length: ", len(words))
print("Top word: ", processTop(result))

plt.bar(range(len(result)), result.values(), align='center')
plt.xticks(range(len(result)), result.keys())
plt.show()
'''

res1 = read("try1.json")
for w in sorted(res1, key=res1.get, reverse=True):
  print (w, " :: ", res1[w])

