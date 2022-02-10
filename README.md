# GlobalToJSON-embeddedPython-pure
Export a Global into a JSON file and re-create it by reloading from this file. ***embeddedPython***    
refers to the new available technologies. It should be understood as a learning exercise of how to     
handle the language interfaces. The mayor difference to its predecessor package is:   
**only embedded Python is used** as a demand of the related contest to demonstrate it is doable.      
Only Global nodes containing data are presented in the generated JSON file.    

![](https://raw.githubusercontent.com/rcemper/GlobalToJSON-ePython-pure/master/Globals.png)    

## Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.
## Installation 
Clone/git pull the repo into any local directory
```
git clone https://github.com/rcemper/GlobalToJSON-ePython-pure.git
```
Run the IRIS container with your project: 
```
docker-compose up -d --build
```
## How to Test it

### ObjectScript Wrapper
This is the pre-loaded Global **^dc.MultiD** for testing.
![](https://raw.githubusercontent.com/rcemper/GlobalToJSON-ePython-pure/master/Global.JPG)

Open IRIS terminal 
```
$ docker-compose exec iris iris session iris
USER>
USER>; generate JSON object file from Global
USER>set sc=##class(dc.GblToJSON.ePure).do("^dc.MultiD","gbl.json")
USER>
```
This is the file content   

![gbl.json](https://raw.githubusercontent.com/rcemper/GlobalToJSON-ePython-pure/master/gbl.json.jpg)   

Now we want to verify the load function.   
First we make a copy of our source and then delete the source   
After the load operation the source Global is completely restored    
```
USER>merge ^keep=^dc.MultiD  

USER>kill ^dc.MultiD

USER>set sc=##class(dc.GblToJSON.ePure).load("gbl.json")
      done

USER>zw sc 
sc=1

USER>zw ^dc.MultiD
^dc.MultiD=5
^dc.MultiD(1)=$lb("Braam,Ted Q.",51353)
^dc.MultiD(1,"mJSON")="{}"
^dc.MultiD(2)=$lb("Klingman,Uma C.",62459)
^dc.MultiD(2,2,"Multi","a")=1
^dc.MultiD(2,2,"Multi","rob",1)="rcc"
^dc.MultiD(2,2,"Multi","rob",2)=2222
^dc.MultiD(2,"Multi","a")=1
^dc.MultiD(2,"Multi","rob",1)="rcc"
^dc.MultiD(2,"Multi","rob",2)=2222
^dc.MultiD(2,"mJSON")="{""A"":""ahahah"",""Rob"":""VIP"",""Rob2"":1111,""Rob3"":true}"
^dc.MultiD(3)=$lb("Goldman,Kenny H.",45831)
^dc.MultiD(3,"mJSON")="{}"
^dc.MultiD(4)=$lb("","")
^dc.MultiD(4,"mJSON")="{""rcc"":122}"
^dc.MultiD(5)=$lb("","")
^dc.MultiD(5,"mJSON")="{}"

USER> 
```

### Python command line

```
shell
cd /irisdev/app/src/Python
/usr/irissys/bin/irispython ePure.py dump --file /tmp/global.json --glob ^dc.MultiD
```
to see the generated file:
```
more /tmp/global.json
```
to load it
```
/usr/irissys/bin/irispython ePure.py load --file /tmp/global.json
```

**q.a.d.**   
### Code Quality 
![CodeQuality](https://raw.githubusercontent.com/rcemper/GlobalToJSON-ePython-pure/master/CodeQuality.JPG)   

[Video](https://youtu.be/kAtna_KU0R8)   

[Article in DC](https://community.intersystems.com/post/globaltojson-embeddedpython-pure)    
