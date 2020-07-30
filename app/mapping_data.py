###################################################################################################
#### Data Type Data Type Data Type Data Type Data Type Data Type Data Type Data Type Data Type ####
###################################################################################################
integer_definition = "int() converts input into integer and truncate the decimals"

integer_code = """print( int(1.9) )
print( int('2') )
print( int(-3.7) )"""

float_definition = "float() converts input into float number"

float_code = """print( float(1.99) )
print( float('2') )
print( float(-3.7) )"""

string_definition = "str() converts input into string. Strings can be concatenated (adding) together."

string_code = """print( str(1.99) )
print( str('2') )
print( str('hello')  + ' ' + 'world' ) #string concatenation"""

global_local_variable_definition = "Global variables are variable created outside of functions and exist (can be used) by every functions. Conversely, local variables are created inside of a function and can only be used inside the respective function. The keyword <i>global</i> can be used to create a global variable inside of a function."

global_local_variable_code = """global_var = 'I am global.'
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

random_number_definition = "To generate random numbers, import random and use randrange."

random_number_code = """import random

x = random.randrange(0,9)
y = random.randrange(0,9)
print(x)
print(y)"""

###################################################################################################
##### List List  List List  List List  List List  List List  List List  List List  List List  #####
###################################################################################################
index_list_definition = """Get element of <button onclick="ajaxSubmit('list')">list</button> using index. 
Use negative index to get element from end of list."""

index_list_code = """list = ['fish', 'donkey', 'shark', 'whale']
print(list[1])
print(list[-1])
print(list[-2])"""

slice_definition = """Use slice to get range of <button onclick="ajaxSubmit('list')">list</button>"""

slice_code = """list = ['fish', 'donkey', 'shark', 'whale']
print(list[1:3])
print(list[1:])"""

length_list_definition = """Use <i>len()</i> to get length of <button onclick="ajaxSubmit('list')">list</button>"""

length_list_code = """list = ['fish', 'donkey', 'shark', 'whale']
print(len(list))"""

if_in_list_definition = """Check if element is in <button onclick="ajaxSubmit('list')">list</button>"""

if_in_list_code = """list = ['fish', 'donkey', 'shark', 'whale']
if 'fish' in list: print('fish is in list')
if 'sheep' in list: print('sheep is in list')
else: print('sheep is not in list')"""

append_list_definition = """Use <i>append</i> to add element to <button onclick="ajaxSubmit('list')">list</button><br/>
list.append(<i>element</i>)<br/>
<br/>
list = ['a', 'b', 'c', 'd', 'e']<br/>
list.append( 'f' )<br/>
print( list )<br/>
>> ['a', 'b', 'c', 'd', 'e', 'f']<br/>"""

append_list_code = """list = ['a', 'b', 'c', 'd', 'e']
list.append( 'f' )
print( list )"""

insert_list_definition = """Use <i>insert()</i> to add an element at a specified index of the <button onclick="ajaxSubmit('list')">list</button>"""

insert_list_code = """list = ['fish', 'donkey', 'shark', 'whale']
list.insert(2, 'sheep')
print( list )"""

delete_list_definition = """<i>del</i> removes an element from the <button onclick="ajaxSubmit('list')">list</button> at specified index and does NOT return the removed element.<br/>
del[<i>index</i>]<br/>
<br/>
list = ['a', 'b', 'c', 'd', 'e']<br/>
del list[2]<br/>
print( list )<br/>
>> ['a', 'b', 'd', 'e']
To delete the entire list, use <i>del</i> without index: del list"""

delete_list_code = """list = ['a', 'b', 'c', 'd', 'e']
del list[2]
print( list )
del list
print( list )"""

pop_list_definition = """
<i>list</i>.pop(<i>index</i>)<br/>
<i>pop</i> removes an element from the <button onclick="ajaxSubmit('list')">list</button> at specified index and also returns the remove element.<br/>
<br/>
list = ['a', 'b', 'c', 'd', 'e']<br/>
pop_remove = list.pop(2)<br/>
print( list )<br/>
>> ['a', 'b', 'd', 'e']<br/>
print( pop_remove )<br/>
>> 'c'"""

pop_list_code = """list = ['a', 'b', 'c', 'd', 'e']
pop_remove = list.pop(2)
print( list )"""

remove_list_definition = """<i>remove()</i> removes an element from the FIRST matching element of the <button onclick="ajaxSubmit('list')">list</button> 
and does NOT return the index of the removed element.<br/>
<i>list</i>.<i>remove(element)</i><br/>
<br/>
list = ['a', 'b', 'c', 'd', 'e', 'b']<br/>
list.remove('c')<br/>
print( list )<br/>
>> ['a', 'b', 'd', 'e', 'b']"""

remove_list_code = """list = ['a', 'b', 'c', 'd', 'e', 'b']
list.remove('c')
print( list )"""

join_list_definition = """To join two <button onclick="ajaxSubmit('list')">lists</button> together, 
simpliy use the <i>+</i> symbol to join them: <i>list_1 + list_2</i>"""

join_list_code = """list_1 = ['fish', 'donkey']
list_2 = ['shark', 'whale']
print( list_1 + list_2)"""

list_definition = "A list is an array of <i>ordered</i> and <i>indexed</i> elements." + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('index')">index of list</button> """ + index_list_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('slice')">slice</button> """ + slice_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('length list')">length of list</button> """ + length_list_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('if in list')">if in list</button> """ + if_in_list_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('append list')">append list</button> """ + append_list_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('insert list')">insert list</button> """ + insert_list_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('delete list')">delete list</button> """ + delete_list_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('pop list')">pop list</button> """ + pop_list_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('remove list')">remove list</button> """ + remove_list_definition + '<br/><br/>' 
list_definition += """<button onclick="ajaxSubmit('join list')">join list</button> """ + join_list_definition + '<br/><br/>' 

list_code = """list = ['fish', 'donkey', 'shark', 'whale']
print( list )"""


mapping_data = {

    "integer": [integer_definition, integer_code],

    "float": [float_definition, float_code],

    "string": [string_definition, string_code],

    "global": [global_local_variable_definition, global_local_variable_code],

    "local": [global_local_variable_definition, global_local_variable_code],

    "random": [random_number_definition, random_number_code],

    "list": [list_definition, list_code],

    "index": [index_list_definition, index_list_code],

    "slice":  [slice_definition, slice_code],

    "length list": [length_list_definition, length_list_code],

    "if in list": [if_in_list_definition, if_in_list_code],

    "append": [append_list_definition, append_list_code],

    "insert list": [insert_list_definition, insert_list_code],

    "delete list": [delete_list_definition, delete_list_code],

    "pop": [pop_list_definition, pop_list_code],

    "remove list": [remove_list_definition, remove_list_code],

    "join list": [join_list_definition, join_list_code],

    
}
