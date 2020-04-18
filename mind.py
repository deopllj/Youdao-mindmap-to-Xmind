import json
import collections
import os
import shutil
import zipfile
#Find the node id in .mindmap file, due to the node in the .mindmap file is unidirectional
def findid(id):
    for node in ydjson["nodes"]:
        if (node["id"]==id):
            return node
    return 0
#Recursively build a node tree
def xmind(ydstruct,xstruct):
    if(ydstruct["id"]!="root"):
        if(not ydstruct["child"]):
            temp = {"id":ydstruct["id"],"title":ydstruct["topic"]}
            xstruct.append(temp)
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
#Transfer the .mindmap file into a dict
with open ('input.mindmap','r', encoding='UTF-8') as ydMind:
    ydcontent = ydMind.read()
#Load the "content.json" in Xmind file, which includes basic config and style in xmind file
with open ('Templates\XmindJsonTemplate.json','r') as xmindtem:
    xmindjson = xmindtem.read()
ydjson = json.loads(ydcontent)
#Xmind is the final "content.json" file's dict pattern
Xmind = json.loads(xmindjson, object_pairs_hook=collections.OrderedDict)
for node in ydjson["nodes"]:
    node["child"] = []
for node in ydjson["nodes"]:
    if(node["id"]!="root"):
        parentid = node ["parentid"]
        parent = findid(parentid)
        parent["child"].append(node["id"])
root = findid("root")
#configure the Xmind file
rootid = root["id"]
rootTopic = Xmind["rootTopic"]
rootTopic["id"] = root["id"]
rootTopic["title"] = root["topic"]
xmind(findid("root"),rootTopic)
output = []
output.append(Xmind)
#Write the json file includes node data into .xmind file
if(os.path.exists('Output')):
    shutil.rmtree('Output')
os.mkdir('Output')
shutil.copyfile("Templates\Mind.xmind","Output\Out.xmind")
with open('Output\content.json','w') as Output:
    Output.write(json.dumps(output))
with zipfile.ZipFile('Output\Out.xmind','a') as tar:
    tar.write('Output\content.json','content.json')
