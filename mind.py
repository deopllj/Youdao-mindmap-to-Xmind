import json
import collections
import os
import shutil
import zipfile
nodes = {}
i= 0
def findid(id):
    for node in ydjson["nodes"]:
        if (node["id"]==id):
            return node
    return 0
def xmind(ydstruct,xstruct):
    if(ydstruct["id"]!="root"):
        if(not ydstruct["child"]):
            temp = {"id":ydstruct["id"],"title":ydstruct["topic"]}
            xstruct.append(temp)
#            return "null"
        else:
            temp = {"id":ydstruct["id"],"title":ydstruct["topic"],"children":{"attached":[]}}
            temp1 = temp["children"]["attached"]
            for children in ydstruct["child"]:
                xmind(findid(children),temp1)
            xstruct.append(temp)
    else:
        temp1 = xstruct["children"]["attached"]
        for children in ydstruct["child"]:
            xmind(findid(children),temp1)
with open ('as.mindmap','r') as ydMind:
    ydcontent = ydMind.read()
with open ('Templates\XmindJsonTemplate.json','r') as xmindtem:
    xmindjson = xmindtem.read()
ydjson = json.loads(ydcontent)
Xmind = json.loads(xmindjson, object_pairs_hook=collections.OrderedDict)
i=0
for node in ydjson["nodes"]:
    node["child"] = []
for node in ydjson["nodes"]:
    if(node["id"]!="root"):
        parentid = node ["parentid"]
        parent = findid(parentid)
        parent["child"].append(node["id"])
root = findid("root")
rootid = root["id"]
x = "xx"
rootTopic = Xmind["rootTopic"]
rootTopic["id"] = root["id"]
rootTopic["title"] = root["topic"]
xmind(findid("root"),rootTopic)
output = []
output.append(Xmind)
if(os.path.exists('Output')):
    shutil.rmtree('Output')
os.mkdir('Output')
shutil.copyfile("Templates\Mind.xmind","Output\Out.xmind")
with open('Output\content.json','w') as Output:
    Output.write(json.dumps(output))
with zipfile.ZipFile('Output\Out.xmind','a') as tar:
    tar.write('Output\content.json','content.json')
