Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(1.2,3,4,5,sep=",,,",end=':')
1.2,,,3,,,4,,,5:
>>> print(1.2,3,4,5,sep=",,,",end='::::::::')
1.2,,,3,,,4,,,5::::::::
>>> print(1.2,3,4,5,flush=True)
1.2 3 4 5
>>> print(1.2,3,4,5,flush=False)
1.2 3 4 5
>>> int(10)
10
>>> int(12.0033)
12
>>> int(13.999999)
13
>>> int(2+3j)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(2+3j)
TypeError: can't convert complex to int
>>> help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Built-in subclasses:
 |      bool
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original int
 |      and with a positive denominator.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  to_bytes(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> int(10,2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(10,2)
TypeError: int() can't convert non-string with explicit base
>>> int(str(10),2)
2
>>> int(12,base=2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int(12,base=2)
TypeError: int() can't convert non-string with explicit base
>>> int(str(12),base=2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(str(12),base=2)
ValueError: invalid literal for int() with base 2: '12'
>>> int('ob001',base=2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int('ob001',base=2)
ValueError: invalid literal for int() with base 2: 'ob001'
>>> int('0b001',base=2)
1
>>> d={}
>>> type(d)
<class 'dict'>
>>> c=set()
>>> s
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> c
set()
>>> type(c)
<class 'set'>
>>> d=dict()
>>> type(d)
<class 'dict'>
>>> int(0b011,base=2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(0b011,base=2)
TypeError: int() can't convert non-string with explicit base
>>> c.append(1,2,3,4,4,5,6)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c.append(1,2,3,4,4,5,6)
AttributeError: 'set' object has no attribute 'append'
>>> c.update(1,2,3,34)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c.update(1,2,3,34)
TypeError: 'int' object is not iterable
>>> i=2
>>> i is True
False
>>> i=1
>>> i is True
False
>>> i==True
True
>>> i=10
>>> i is True
False
>>> i==True
False
>>> i=10
>>> i==True
False
>>> if i:
	print(i)

	
10
>>> i=0
>>> i==False
True
>>> i==True
False
>>> i=20
>>> i==True
False
>>> s='a'
>>> s=input()
hI
>>> s
'hI'
>>> s=""
>>> s=input()
wgdjhregoredfjcpier
>>> s
'wgdjhregoredfjcpier'
>>> l=list([1,2,3,4,5])
>>> l
[1, 2, 3, 4, 5]
>>> a=1,2,,3,4,5
SyntaxError: invalid syntax
>>> a=1,2,3,4,5
>>> a
(1, 2, 3, 4, 5)
>>> s={1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> type(s)
<class 'set'>
>>> l=list()
>>> l
[]
>>> a=5
>>> b=10
>>> l=[a,b]
>>> l
[5, 10]
>>> a=10
>>> b=a
>>> id(a),id(b)
(1871030336, 1871030336)
>>> a=20
>>> b
10
>>> len({1:2,3;4})
SyntaxError: invalid syntax
>>> len({1:2,3:4})
2
>>> t=1,2,3
>>> t1=t
>>> id(t),id(t1)
(8944552, 8944552)
>>> t1=2,3,4
>>> id(t),id(t1)
(8944552, 8904264)
>>> reverse([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    reverse([1,2,3,4])
NameError: name 'reverse' is not defined
>>> reversed([1,2,3,4])
<list_reverseiterator object at 0x0088C688>
>>> l=[1,2,3,4]
>>> l.reverse()
>>> l
[4, 3, 2, 1]
>>> t1=1,2,3
>>> t1
(1, 2, 3)
>>> t1=2,3,4,5
>>> t1
(2, 3, 4, 5)
>>> len(t1)
4
>>> round(12,3)
12
>>> print('%05d'%12)
00012
>>> print('%50d'%12)
                                                12
>>> print('%1d'%12)
12
>>> print('%2d'%12)
12
>>> print('%10d'%12)
        12
>>> print('%110d'%12)
                                                                                                            12
>>> print('%010d'%12)
0000000012
>>> s='123345623244'
>>> sorted(s)
['1', '2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '6']
>>> l=[1,2,3,4,5,6]
>>> sorted(l)
[1, 2, 3, 4, 5, 6]
>>> sort(l)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    sort(l)
NameError: name 'sort' is not defined
>>> l.sort()
>>> l
[1, 2, 3, 4, 5, 6]
>>> l=[7,3,4,2,4,62,1]
>>> sorted(l)
[1, 2, 3, 4, 4, 7, 62]
>>> l
[7, 3, 4, 2, 4, 62, 1]
>>> l.sort(0
       )
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    l.sort(0
TypeError: sort() takes no positional arguments
>>> l.sort()
>>> l
[1, 2, 3, 4, 4, 7, 62]
>>> s
'123345623244'
>>> s.sort()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    s.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> sorted(s)
['1', '2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '6']
>>> min(1,2,3,4)
1
>>> hex(12)
'0xc'
>>> hex(12)+hex(3)
'0xc0x3'
>>> hex(12+4)
'0x10'
>>> l1
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    l1
NameError: name 'l1' is not defined
>>> l
[1, 2, 3, 4, 4, 7, 62]
>>> l1=l[:]
>>> id(l1),id(l)
(54643592, 8933064)
>>> li is l
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    li is l
NameError: name 'li' is not defined
>>> l1 is l
False
>>> li==l
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    li==l
NameError: name 'li' is not defined
>>> l1==l
True
>>> t1
(2, 3, 4, 5)
>>> t
(1, 2, 3)
>>> t2=t1
>>> t2
(2, 3, 4, 5)
>>> t2 is t1
True
>>> t2==t1
True
>>> a
20
>>> b
10
>>> c
set()
>>> d
{}
>>> e
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> e=complex(2,3)
>>> f=complex(3,4)
>>> e
(2+3j)
>>> f
(3+4j)
>>> e+f
(5+7j)
>>> e-f
(-1-1j)
>>> e*f
(-6+17j)
>>> e/f
(0.72+0.04j)
>>> 2/3
0.6666666666666666
>>> 3/4
0.75
>>> s='abcd'
>>> s.strip()
'abcd'
>>> list(s)
['a', 'b', 'c', 'd']
>>> sorted(s)
['a', 'b', 'c', 'd']
>>> s='vcbfdhdfgvd'
>>> sorted(s)
['b', 'c', 'd', 'd', 'd', 'f', 'f', 'g', 'h', 'v', 'v']
>>> set(s)
{'d', 'g', 'c', 'h', 'f', 'v', 'b'}
>>> sorted(s)
['b', 'c', 'd', 'd', 'd', 'f', 'f', 'g', 'h', 'v', 'v']
>>> s1=set(s)
>>> s1
{'d', 'g', 'c', 'h', 'f', 'v', 'b'}
>>> sorted(s1)
['b', 'c', 'd', 'f', 'g', 'h', 'v']
>>> '{}{}{}'.format('Hi','HEllo','bee')
'HiHEllobee'
>>> '{1}{0}{2}'.format('Hi','HEllo','bee')
'HElloHibee'
>>> len(str(3.14285714285714279370154144999105483293533325195312))
17
>>> list(str(3.14285714285714279370154144999105483293533325195312))
['3', '.', '1', '4', '2', '8', '5', '7', '1', '4', '2', '8', '5', '7', '1', '4', '3']
>>> len(list(str(3.14285714285714279370154144999105483293533325195312)))
17
>>> print('%50d'%(22/7))
                                                 3
>>> print('%.50f'%(22/7))
3.14285714285714279370154144999105483293533325195312
>>> print('The value of %d in hex=%x, in oct=%o, in bin=%b'%(12,12,12,12))
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    print('The value of %d in hex=%x, in oct=%o, in bin=%b'%(12,12,12,12))
ValueError: unsupported format character 'b' (0x62) at index 46
>>> print('The value of %d in hex=%x, in oct=%o'%(12,12,12))
The value of 12 in hex=c, in oct=14
>>> print(f'The value of pi is {22/7:.10f}')
The value of pi is 3.1428571429
>>> print(f'The value of pi is {22/7:5.10f}')
The value of pi is 3.1428571429
>>> print(f'The value of pi is {22/7:05.10f}')
The value of pi is 3.1428571429
>>> print('The value of pi is {{0}}'.format(22/7))
The value of pi is {0}
>>> print('The value of pi is { {0} }'.format(22/7))
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    print('The value of pi is { {0} }'.format(22/7))
ValueError: unexpected '{' in field name
>>> print('The value of pi is {0}'.format(22/7))
The value of pi is 3.142857142857143
>>> print('The value of pi is {.10f}'.format(22/7))
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    print('The value of pi is {.10f}'.format(22/7))
AttributeError: 'float' object has no attribute '10f'
>>> l=[]
>>> if l:
	print('Yes')

	
>>> if not l:
	print('NO')

	
NO
>>> a='ob001'
>>> b='0b011'
>>> a='0b0012'
>>> a & b
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    a & b
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> a
'0b0012'
>>> b
'0b011'
>>> c
set()
>>> c.add(2,3)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    c.add(2,3)
TypeError: add() takes exactly one argument (2 given)
>>> c.add(2)
>>> c
{2}
>>> c.add({2,3,4,5})
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    c.add({2,3,4,5})
TypeError: unhashable type: 'set'
>>> c.update({1,2,3,,4,4,5,5,6,6,6,6,7,7})
SyntaxError: invalid syntax
>>> c.update({1,2,3,4,4,5,5,6,6,6,6,7,7})
>>> c
{1, 2, 3, 4, 5, 6, 7}
>>> c.update([1,9,[1,2],[1,2],(1,2),(1,2)])
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    c.update([1,9,[1,2],[1,2],(1,2),(1,2)])
TypeError: unhashable type: 'list'
>>> s.update([1,2])
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    s.update([1,2])
AttributeError: 'str' object has no attribute 'update'
>>> a.update([1,2])
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    a.update([1,2])
AttributeError: 'str' object has no attribute 'update'
>>> c.update([1,2])
>>> c
{1, 2, 3, 4, 5, 6, 7, 9}
>>> l
[]
>>> l=[1,2,3,4]
>>> l.clear()
>>> l
[]
>>> a=frozenset(1,2,3)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    a=frozenset(1,2,3)
TypeError: frozenset expected at most 1 argument, got 3
>>> a=frozenset([1,2,3])
>>> a
frozenset({1, 2, 3})
>>> a.add(4)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    a.add(4)
AttributeError: 'frozenset' object has no attribute 'add'
>>> c
{1, 2, 3, 4, 5, 6, 7, 9}
>>> a=c.copy()
>>> a
{1, 2, 3, 4, 5, 6, 7, 9}
>>> a.add(12)
>>> a
{1, 2, 3, 4, 5, 6, 7, 9, 12}
>>> c
{1, 2, 3, 4, 5, 6, 7, 9}
>>> b=c
>>> b.add(120)
>>> b
{1, 2, 3, 4, 5, 6, 7, 9, 120}
>>> c
{1, 2, 3, 4, 5, 6, 7, 9, 120}
>>> l
[]
>>> l=[1,2]
>>> del l[0]
>>> l
[2]
>>> del(l[0])
>>> l
[]
>>> l=[i for i in range(10)]
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> l.pop()
9
>>> c.pop()
1
>>> c
{2, 3, 4, 5, 6, 7, 9, 120}
>>> c.pop()
2
>>> c.pop()
3
>>> type(c)
<class 'set'>
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> l=[i for i in  range(2)]
>>> l
[0, 1]
>>> (a,b)=l
>>> a
0
>>> b
1
>>> 