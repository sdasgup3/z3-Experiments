#############################################
######## Auto Generated Proof Scripts #######
#############################################

import z3
import sys

def solve(s):
  print(s)
  res = s.check()
  print(res)
  if(z3.sat == res):
    print(s.model())


x1 = z3.Int('x1')
x2 = z3.Int('x2')
cf = z3.Int('cf')

bvl = 4
maxbvl = pow(2, bvl)
b1 = z3.BitVec('rax', bvl)
b2 = z3.BitVec('rbx', bvl)

s = z3.Solver()

s.push()
var1 = z3.If(z3.And(x1 + cf >= 0 , x1 + cf <= 4294967295), x1+cf, (x1+cf)% 4294967296)
var2 = (x1+cf)%4294967296

s.add(var1 != var2)
solve(s)
s.pop()

## addition of two ints followed by mod === addition of two bvs  
s.push()
var1 = (z3.BV2Int(b1) + z3.BV2Int(b2)) % maxbvl
var2 = z3.BV2Int(b1 + b2)

s.add(var1 != var2)
solve(s)
s.pop()

## addition of 2 bvs  is in 2's complement
s.push()
var1 =  b1 + b2
var2 = (b1 + b2) & z3.BitVecVal(maxbvl-1, bvl)

s.add(var1 != var2)
solve(s)
s.pop()

