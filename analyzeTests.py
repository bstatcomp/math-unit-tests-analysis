import glob
import os

def LOC(filename):
    """
        Counts effective lines of code in a file
    """
    count = 0
    skip= False  
    for line in open(filename).readlines(): 
        line = line.strip()
        if line:
            if line.startswith('//'):
                continue
            if line.startswith('/*'):
                skip = True
                continue
            if line.startswith('*/') or line.endswith('*/'):
                skip = False
                continue
            if not skip:
                count+= 1
    return count


root='D:/FRI/ProjektStrumbelj/Testing/math'

#Functions
#Prim
primDir = root + '/stan/math/prim/'
#scal
primScalDir = primDir + 'scal/fun'
#mat
primMatDir = primDir + 'mat/fun'

#Rev
revDir = root + '/stan/math/rev/'
#scal
revScalDir = revDir + 'scal/fun'
#mat
revMatDir = revDir + 'mat/fun'

#Fwd
fwdDir = root + '/stan/math/fwd/'
#scal
fwdScalDir = fwdDir + 'scal/fun'
#mat
fwdMatDir = fwdDir + 'mat/fun'



#Tests
#PrimTests
primDirT = root + '/test/unit/math/prim/'
#scal
primScalDirT = primDirT + 'scal/fun'
#mat
primMatDirT = primDirT + 'mat/fun'

#RevTests
revDirT = root + '/test/unit/math/rev/'
#scal
revScalDirT = revDirT + 'scal/fun'
#mat
revMatDirT = revDirT + 'mat/fun'

#FwdTests
fwdDirT = root + '/test/unit/math/fwd/'
#scal
fwdScalDirT = fwdDirT + 'scal/fun'
#mat
fwdMatDirT = fwdDirT + 'mat/fun'


scalarFun ={
  "prim": [],
  "rev": [],
  "fwd": [],
  "all": [] 
}


matFun ={
  "prim": [],
  "rev": [],
  "fwd": [],
  "all": [] 
}

scalarFunLOC ={
  "prim": {},
  "rev": {},
  "fwd": {}
}

matFunLOC ={
  "prim": {},
  "rev": {},
  "fwd": {}
}

scalarTests ={
  "prim": [],
  "rev": [],
  "fwd": [],
  "all": [] 
}


scalarTestsLOC ={
  "prim": {},
  "rev": {},
  "fwd": {}
}

matTestsLOC ={
  "prim": {},
  "rev": {},
  "fwd": {}
}

matTests ={
  "prim": [],
  "rev": [],
  "fwd": [],
  "all": [] 
}
#Get scalar functions
for filename in glob.glob(primScalDir+'/*.hpp'):
    scalarFun["prim"].append(os.path.basename(filename).split('.')[0])
    scalarFunLOC["prim"][os.path.basename(filename).split('.')[0]]=LOC(filename)
for filename in glob.glob(revScalDir+'/*.hpp'):
    scalarFun["rev"].append(os.path.basename(filename).split('.')[0])
    scalarFunLOC["rev"][os.path.basename(filename).split('.')[0]]=LOC(filename)
for filename in glob.glob(fwdScalDir+'/*.hpp'):
    scalarFun["fwd"].append(os.path.basename(filename).split('.')[0])
    scalarFunLOC["fwd"][os.path.basename(filename).split('.')[0]]=LOC(filename)

scalarFun["all"]=list(set().union(scalarFun["prim"],scalarFun["rev"],scalarFun["fwd"]))

#Get mat functions
for filename in glob.glob(primMatDir+'/*.hpp'):
    matFun["prim"].append(os.path.basename(filename).split('.')[0])
    matFunLOC["prim"][os.path.basename(filename).split('.')[0]]=LOC(filename)
for filename in glob.glob(revMatDir+'/*.hpp'):
    matFun["rev"].append(os.path.basename(filename).split('.')[0])
    matFunLOC["rev"][os.path.basename(filename).split('.')[0]]=LOC(filename)
for filename in glob.glob(fwdMatDir+'/*.hpp'):
    matFun["fwd"].append(os.path.basename(filename).split('.')[0])
    matFunLOC["fwd"][os.path.basename(filename).split('.')[0]]=LOC(filename)


matFun["all"]=list(set().union(matFun["prim"],matFun["rev"],matFun["fwd"]))


#Get scalar function tests
for filename in glob.glob(primScalDirT+'/*.cpp'):
    scalarTests["prim"].append(os.path.basename(filename).split('_test')[0])
    scalarTestsLOC["prim"][os.path.basename(filename).split('_test')[0]]=LOC(filename)
for filename in glob.glob(revScalDirT+'/*.cpp'):
    scalarTests["rev"].append(os.path.basename(filename).split('_test')[0])
    scalarTestsLOC["rev"][os.path.basename(filename).split('_test')[0]]=LOC(filename)

for filename in glob.glob(fwdScalDirT+'/*.cpp'):
    scalarTests["fwd"].append(os.path.basename(filename).split('_test')[0])
    scalarTestsLOC["fwd"][os.path.basename(filename).split('_test')[0]]=LOC(filename)


scalarTests["all"]=list(set().union(scalarTests["prim"],scalarTests["rev"],scalarTests["fwd"]))

#missingPrim=list(set(scalarTests["all"])-set(scalarTests["prim"]))
#missingRev=list(set(scalarTests["all"])-set(scalarTests["rev"]))
#missingFwd=list(set(scalarTests["all"])-set(scalarTests["fwd"]))

#print('Missing Prim scalar function tests:\n')
#print(*missingPrim, sep='\n')
#print('\n')
#print('Missing Rev scalar function tests:\n')
#print(*missingFwd, sep='\n')
#print('\n')
#print('Missing Fwd scalar function tests:\n')
#print(*missingRev, sep='\n')

print("STANMATH SCALAR FUNCTIONS AND TESTS")
line='FUN PRIM REV FWD TPRIM TREV TFWD'.split()
print(f'{line[0]:<30}  {line[1]:<5}  {line[2]:<5}  {line[3]:<5}  {line[4]:<5}  {line[5]:<5}  {line[6]:<5}')
listF=list(set().union(scalarTests["all"],scalarFun["all"]))
for f in sorted(listF, key=lambda s: s.casefold()):
    line=f
    if f in scalarFun["prim"]:
        line=line+'\n'+str(scalarFunLOC["prim"][f])
    else:
        line=line+'\n'+' '
    if f in scalarFun["rev"]:
        line=line+'\n'+str(scalarFunLOC["rev"][f])
    else:
        line=line+'\n'+' '
    if f in scalarFun["fwd"]:
        line=line+'\n'+str(scalarFunLOC["fwd"][f])
    else:
        line=line+'\n'+' '
    if f in scalarTests["prim"]:
        line=line+'\n'+str(scalarTestsLOC["prim"][f])
    else:
        line=line+'\n'+' '
    if f in scalarTests["rev"]:
        line=line+'\n'+str(scalarTestsLOC["rev"][f])
    else:
        line=line+'\n'+' '
    if f in scalarTests["fwd"]:
        line=line+'\n'+str(scalarTestsLOC["fwd"][f])
    else:
        line=line+'\n'+' '
    line=line.split('\n')
    print(f'{line[0]:<30}  {line[1]:<5}  {line[2]:<5}  {line[3]:<5}  {line[4]:<5}  {line[5]:<5}  {line[6]:<5}')

#Get mat tests
for filename in glob.glob(primMatDirT+'/*.cpp'):
    matTests["prim"].append(os.path.basename(filename).split('_test')[0])
    matTestsLOC["prim"][os.path.basename(filename).split('_test')[0]]=LOC(filename)

for filename in glob.glob(revMatDirT+'/*.cpp'):
    matTests["rev"].append(os.path.basename(filename).split('_test')[0])
    matTestsLOC["rev"][os.path.basename(filename).split('_test')[0]]=LOC(filename)

for filename in glob.glob(fwdMatDirT+'/*.cpp'):
    matTests["fwd"].append(os.path.basename(filename).split('_test')[0])
    matTestsLOC["fwd"][os.path.basename(filename).split('_test')[0]]=LOC(filename)

matTests["all"]=list(set().union(matTests["prim"],matTests["rev"],matTests["fwd"]))

print("\nSTANMATH MAT FUNCTIONS AND TESTS")
line='FUN PRIM REV FWD TPRIM TREV TFWD'.split()
print(f'{line[0]:<30}  {line[1]:<5}  {line[2]:<5}  {line[3]:<5}  {line[4]:<5}  {line[5]:<5}  {line[6]:<5}')
listF=list(set().union(matTests["all"],matFun["all"]))
for f in sorted(listF, key=lambda s: s.casefold()):
    line=f
    if f in matFun["prim"]:
        line=line+'\n'+str(matFunLOC["prim"][f])
    else:
        line=line+'\n'+' '
    if f in matFun["rev"]:
        line=line+'\n'+str(matFunLOC["rev"][f])
    else:
        line=line+'\n'+' '
    if f in matFun["fwd"]:
        line=line+'\n'+str(matFunLOC["fwd"][f])
    else:
        line=line+'\n'+' '
    if f in matTests["prim"]:
        line=line+'\n'+str(matTestsLOC["prim"][f])
    else:
        line=line+'\n'+' '
    if f in matTests["rev"]:
        line=line+'\n'+str(matTestsLOC["rev"][f])
    else:
        line=line+'\n'+' '
    if f in matTests["fwd"]:
        line=line+'\n'+str(matTestsLOC["fwd"][f])
    else:
        line=line+'\n'+' '
    line=line.split('\n')
    print(f'{line[0]:<30}  {line[1]:<5}  {line[2]:<5}  {line[3]:<5}  {line[4]:<5}  {line[5]:<5}  {line[6]:<5}')
