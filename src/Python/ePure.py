import argparse

import iris
import json

def ddata(gref):
    """simulate $data() for existence and content"""
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


def node(nd,nxt,fil):
    """build JSON object for data node"""
    gn={}	
    gn["sub"]=nd[0]
    gn["val"]=nd[1]
    fil.writelines([nxt+json.dumps(gn),'\n'])
    return ','


def dump(glob,file):
    """dump global"""
    glob=glob.replace('^','')
    gref=iris.gref(glob)		 
    _d=ddata(gref)
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
        nxt = node(('',_d[1]),nxt,fil)
    _qu=list(gref.query(['']))	
    #; loop on subscripted nodes
    for i in range(len(_qu)):
        _nd=_qu[i]
    #; need to check for data
        if _nd[1] == None:
                continue
        nxt = node(_nd,nxt,fil)
    fil.write(']}')
    fil.close()
    
    return 1


def load(file):
    g=""
    with open(file,'r') as fil:
        for lin in fil:
            if lin == ']}': 
                break
        
            if lin[:7] == '{"gbl":' :
                glob =  '^'+lin[7:].split('"')[1]
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    argdump = subparser.add_parser('dump')
    argdump.add_argument('--file', metavar=str, required=True,
                        help='json file')
    argdump.add_argument('--glob', metavar=str, required=True,
                        help='global name')

    argload = subparser.add_parser('load')
    argload.add_argument('--file', metavar=str, required=True,
                        help='json file')

    args = parser.parse_args()
    
    if args.command == 'dump':
        dump(args.glob,args.file)
    elif args.command == 'load':
        load(args.file)
    else:
        parser.print_help()


