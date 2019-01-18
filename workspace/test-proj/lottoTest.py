import random
import simplejson as json

full = list(range(1, 46))

for _ in range(0,5):
    random.shuffle(full)
    result = json.dumps({"lotto": full[0:5]})
    print(result)
    #ㅀㅇㅎㅎ