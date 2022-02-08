Class dc.GblToJSON.ePure [ Language = python ]
{

ClassMethod do(
	glob As %String = "^%",
	file = "") As %Boolean
{
import iris
import json

#; simulate $data() for existence and content
def Ddata(gref):
	val = None
	_d = 11
#; check for subscripts	
	o=gref.order([])
	if o == None:
		_d -= 10
	
	try:
		val=gref.get([])
	except KeyError:
		#; no value @ top node
		_d -= 1
	return [_d,val]		

#; build JSON object for data node
def node(nd,nxt):
	gn={}	
	gn["sub"]=nd[0]
	gn["val"]=nd[1]
	fil.writelines([nxt+json.dumps(gn),'\n'])
	return ','

#; dump global
glob=glob.replace('^','')
gref=iris.gref(glob)		 
_d=Ddata(gref)
if _d[0] < 1 :
	print('Global not found')
	return 0
	
if file == "" :
	file=glob+".json"
#; init file
fil=open(file,'w')
fil.write('{"gbl":"'+glob+'","nodes":\n[')
nxt=''
#; top node
if _d[0]%10>0:
	nxt = node(('',_d[1]),nxt)
_qu=list(gref.query(['']))	
#; loop on subscripted nodes
for i in range(len(_qu)):
	_nd=_qu[i]
#; need to check for data
	if _nd[1] == None:
			continue
	nxt = node(_nd,nxt)
fil.write(']}')
fil.close()
return 1
}

/// reload from .json file
ClassMethod load(file As %String = "gbl.json") As %Status [ Language = python ]
{
import json
import iris
g=""

with open(file,'r') as fil:
	for lin in fil:
	
		if lin == ']}': 
			break
	
		if lin[:7] == '{"gbl":' :
			glob =  '^X'+lin[7:].split('"')[1]
			gref=iris.gref(glob)
			continue
		lin = lin[1:].replace('\n','')
		
		jsn=json.loads(lin)
		sub=jsn["sub"]
		val=jsn["val"]
		if val == 'none' :
			continue
		if sub == '':
			gref[None]=val
		else:
			gref[sub]=val
					
print('\tdone')	
fil.close()
return 1
}

}
