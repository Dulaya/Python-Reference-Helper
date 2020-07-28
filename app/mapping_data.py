mapping_data = {

    "integer": 
    [
        """int() converts input into integer and truncate the decimals
        """,
"""print( int(1.9) )
print( int('2') )
print( int(-3.7) )"""
    ],

        "float": 
    [
        """float() converts input into float number 
        """,
"""print( float(1.99) )
print( float('2') )
print( float(-3.7) )"""
    ],

        "string": 
    [
        """str() converts input into string. Strings can be concatenated (adding) together. 
        """,
"""print( str(1.99) )
print( str('2') )
print( str('hello')  + ' ' + 'world' ) #string concatenation"""
    ],

    "global local variable": 
    [
        """Global variables are variable created outside of functions and exist (can be used) by every functions. 
        Conversely, local variables are created inside of a function and can only be used inside the respective function.
        The keyword <i>global</i> can be used to create a global variable inside of a function.
        """,
"""global_var = 'I am global.'

def funct():
    local_var = 'I am local.'

    print(local_var)
    print(global_var)

def funct_2():
    global global_var_2
    global_var_2 = 'I am global too.'

funct()
funct_2()
print(global_var)
print(global_var_2)
#print(local_var)"""
    ],

    "random number": 
    [
        """To generate random numbers, import random and use randrange.
        """,
"""import random

x = random.randrange(0,9)
y = random.randrange(0,9)
print(x)
print(y)
"""
    ],

#################################################### List ################################################################
"index list": 
[
"""Get element of list using index. Using negative index to get element from end of list.
""",
"""list = ['fish', 'donkey', 'shark', 'whale']
print(list[1])
print(list[-1])
print(list[-2])
"""
],

"slice list": 
[
"""Use slice to get range of list.
""",
"""list = ['fish', 'donkey', 'shark', 'whale']
print(list[1:3])
print(list[1:])
"""
],

"length list": 
[
"""Use <i>len()</i> to get list of list.
""",
"""list = ['fish', 'donkey', 'shark', 'whale']
print(len(list))
"""
],

"if in list": 
[
"""Check if element is in list.
""",
"""list = ['fish', 'donkey', 'shark', 'whale']
if 'fish' in list: print('fish is in list')
if 'sheep' in list: print('sheep is in list')
else: print('sheep is not in list')
"""
],

    "append element list": 
    [
        """
        list.append(<i>element</i>)<br/>
        <br/>
        list = ['a', 'b', 'c', 'd', 'e']<br/>
        list.append( 'f' )<br/>
        print( list )<br/>
        >> ['a', 'b', 'c', 'd', 'e', 'f']
        """,
        """list = ['a', 'b', 'c', 'd', 'e']
list.append( 'f' )
print( list )"""
    ],

    "delete element list": 
    [
        """<i>del</i> removes an element from the list at specified index and does NOT return the removed element.<br/>
        del[<i>index</i>]<br/>
        <br/>
        list = ['a', 'b', 'c', 'd', 'e']<br/>
        del list[2]<br/>
        print( list )<br/>
        >> ['a', 'b', 'd', 'e']""",
        """list = ['a', 'b', 'c', 'd', 'e']
del list[2]
print( list )"""
    ],

    "pop element list": 
    [
        """
        <i>list</i>.pop(<i>index</i>)<br/>
        <i>pop</i> removes an element from the list at specified index and also returns the remove element.<br/>
        <br/>
        list = ['a', 'b', 'c', 'd', 'e']<br/>
        pop_remove = list.pop(2)<br/>
        print( list )<br/>
        >> ['a', 'b', 'd', 'e']<br/>
        print( pop_remove )<br/>
        >> 'c'
        """,
        """list = ['a', 'b', 'c', 'd', 'e']
pop_remove = list.pop(2)
print( list )"""
    ],

    "remove element list": 
    [
        """
        <i>remove</i> removes an element from the FIRST matching element of the list and does NOT return the index of the removed element.<br/>
        <i>list</i>.<i>remove(element)</i><br/>
        <br/>
        list = ['a', 'b', 'c', 'd', 'e', 'b']<br/>
        list.remove('c')<br/>
        print( list )<br/>
        >> ['a', 'b', 'd', 'e', 'b']
        """,
        """list = ['a', 'b', 'c', 'd', 'e', 'b']
list.remove('c')
print( list )"""
    ],
    


    
}
