###################################################################################################
#### Data Type Data Type Data Type Data Type Data Type Data Type Data Type Data Type Data Type ####
###################################################################################################
integer_definition = """An integer is any whole positive or negative numbers. 
<i>int()</i> converts input into an integer and truncate the decimals. 
Integera is a <button onclick="ajaxSubmit('data type')">data type</button>"""

integer_code = """print( int(1.9) )
print( int('2') )
print( int(-3.7) )"""

float_definition = """Float is a non-integer real numbers. <i>float()</i> converts input into a floating number.
Float is a <button onclick="ajaxSubmit('data type')">data type</button>"""

float_code = """print( float(1.99) )
print( float('2') )
print( float(-3.7) )"""

string_definition = """String is made up of characters. Strings can be concatenated (adding) together. <i>float()</i> converts input into a string.
String is a <button onclick="ajaxSubmit('data type')">data type</button>"""

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


list_definition_short = """A list is an array of <i>ordered</i> and <i>indexed</i> elements. 
A list is constructed by a square bracket with commas separating elements inside. An example of a list: 
<div id='codeDiv'>animal_list = ['fish', 'donkey', 'shark', 'whale']</div>
"""
dictionary_definition_short = """A dictionary is a collection of <i>unordered keys</i> and <i>indexed values</i>. 
A dictionary is constructed by a curly bracket with commas separating <i>key:value</i>. An example of a dicitonary: 
<div id='codeDiv'>animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}</div>
"""
tuple_definition_short = "A tuple..."
set_definition_short = "A set..."


data_type_definition = "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('integer')">int</button> """ + integer_definition + "</div>"
data_type_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('float')">float</button> """ + float_definition + "</div>"
data_type_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('string')">str</button> """ + string_definition + "</div>"
data_type_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('list')">list</button> """ + list_definition_short + "</div>"
data_type_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('dictionary')">dictionary</button> """ + dictionary_definition_short + "</div>"
data_type_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('tuple')">tuple</button> """ + tuple_definition_short + "</div>"
data_type_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('set')">set</button> """ + set_definition_short + "</div>"

data_type_code = """print( int(3.14) )
print( float(3.14) )
print( str(3.14) )"""

###################################################################################################
##### List List  List List  List List  List List  List List  List List  List List  List List  #####
###################################################################################################
index_list_definition = """Get element of <button id='typeButton' onclick="ajaxSubmit('list')">list</button> using index. 
Use negative index to get element from end of list."""

index_list_code = """list = ['fish', 'donkey', 'shark', 'whale']
print(list[1])
print(list[-1])
print(list[-2])"""

slice_definition = """Use slice to get range of <button id='typeButton' onclick="ajaxSubmit('list')">list</button>"""

slice_code = """list = ['fish', 'donkey', 'shark', 'whale']
print(list[1:3])
print(list[1:])"""

length_list_definition = """Use <i>len()</i> to get length of <button id='typeButton' onclick="ajaxSubmit('list')">list</button>"""

length_list_code = """list = ['fish', 'donkey', 'shark', 'whale']
print(len(list))"""

if_in_list_definition = """Check if element is in <button id='typeButton' onclick="ajaxSubmit('list')">list</button>"""

if_in_list_code = """list = ['fish', 'donkey', 'shark', 'whale']
if 'fish' in list: print('fish is in list')
if 'sheep' in list: print('sheep is in list')
else: print('sheep is not in list')"""

append_list_definition = """Use <i>append</i> to add element to <button id='typeButton' onclick="ajaxSubmit('list')">list</button><br/>
list.append(<i>element</i>)<br/>
<div id='codeDiv'>list = ['a', 'b', 'c', 'd', 'e']<br/>
list.append( 'f' )<br/>
print( list )<br/>
>> ['a', 'b', 'c', 'd', 'e', 'f']</div>"""

append_list_code = """list = ['a', 'b', 'c', 'd', 'e']
list.append( 'f' )
print( list )"""

insert_list_definition = """Use <i>insert()</i> to add an element at a specified index of the <button id='typeButton' onclick="ajaxSubmit('list')">list</button>"""

insert_list_code = """list = ['fish', 'donkey', 'shark', 'whale']
list.insert(2, 'sheep')
print( list )"""

delete_list_definition = """<i>del</i> removes an element from the <button id='typeButton' onclick="ajaxSubmit('list')">list</button> at specified index and does NOT return the removed element:
del[<i>index</i>]<br/>
<div id='codeDiv'>list = ['a', 'b', 'c', 'd', 'e']<br/>
del list[2]<br/>
print( list )<br/>
>> ['a', 'b', 'd', 'e']</div>
To delete the entire list, use <i>del</i> without index: <div id='codeDiv'>del list</div>"""

delete_list_code = """list = ['a', 'b', 'c', 'd', 'e']
del list[2]
print( list )
del list
print( list )"""

pop_list_definition = """
<i>list</i>.pop(<i>index</i>)<br/>
<i>pop</i> removes an element from the <button id='typeButton' onclick="ajaxSubmit('list')">list</button> at specified index and also returns the remove element.<br/>
<div id='codeDiv'>list = ['a', 'b', 'c', 'd', 'e']<br/>
pop_remove = list.pop(2)<br/>
print( list )<br/>
>> ['a', 'b', 'd', 'e']<br/>
print( pop_remove )<br/>
>> 'c'</div>"""

pop_list_code = """list = ['a', 'b', 'c', 'd', 'e']
pop_remove = list.pop(2)
print( list )"""

remove_list_definition = """<i>remove()</i> removes an element from the FIRST matching element of the <button id='typeButton' onclick="ajaxSubmit('list')">list</button> 
and does NOT return the index of the removed element.<br/>
<i>list</i>.<i>remove(element)</i><br/>
<div id='codeDiv'>list = ['a', 'b', 'c', 'd', 'e', 'b']<br/>
list.remove('c')<br/>
print( list )<br/>
>> ['a', 'b', 'd', 'e', 'b']</div>"""

remove_list_code = """list = ['a', 'b', 'c', 'd', 'e', 'b']
list.remove('c')
print( list )"""

join_list_definition = """To join two <button id='typeButton' onclick="ajaxSubmit('list')">lists</button> together, 
simpliy use the <i>+</i> symbol to join them: <i>list_1 + list_2</i>"""

join_list_code = """list_1 = ['fish', 'donkey']
list_2 = ['shark', 'whale']
print( list_1 + list_2)"""

list_definition = "<div id='alternateRow'>" + list_definition_short + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('index')">index of list</button> """ + index_list_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('slice')">slice</button> """ + slice_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('length list')">length of list</button> """ + length_list_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('if in list')">if in list</button> """ + if_in_list_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('append list')">append list</button> """ + append_list_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('insert list')">insert list</button> """ + insert_list_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('delete list')">delete list</button> """ + delete_list_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('pop list')">pop list</button> """ + pop_list_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('remove list')">remove list</button> """ + remove_list_definition + "</div>" 
list_definition +=  "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('join list')">join list</button> """ + join_list_definition + "</div>" 

list_code = """list = ['fish', 'donkey', 'shark', 'whale']
print( list )"""


###################################################################################################
##### Dictionary Dictionary Dictionary Dictionary Dictionary Dictionary Dictionary Dictionary #####
###################################################################################################
access_dictionary_definition = """To access a <button onclick="ajaxSubmit('dictionary')">dictionary</button>, use square bracket like this: 
<div id='codeDiv'>animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}</br>
print( animal_dict['fish'] ) <br/>
>> 'tuna'</div>
Note: Unlike a list, a dictionary is NOT ordered. This means that a dictionary CANNOT bet access by integers like list. 
This is an common example of a dictionary being wrongly accessed: 
<div id='codeDiv'>animal_dict[0]</div>
This is wrong because 0 is not a key of the dictionary. 
"""

access_dictionary_code = """animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}
print( animal_dict['fish'] )"""

update_dictionary_definition = """To update a <button onclick="ajaxSubmit('dictionary')">dictionary</button>, use square bracket and set it to a new value:
<div id='codeDiv'>animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}</br>
animal_dict['fish'] = 'salmon' <br/>
print( animal_dict )</div>"""

update_dictionary_code = """animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}
animal_dict['fish'] = 'salmon'
print( animal_dict )"""

keys_dictionary_definition = """To get all the keys of a <button onclick="ajaxSubmit('dictionary')">dictionary</button>, 
use <i>dictionary.keys()</i>, which will return a list of keys:
<div id='codeDiv'>animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}</br>
print( animal_dict.keys() )</div>
Since <i>dictionary.keys()</i> returns a list, an individual key can be accessed with an index: 
<div id='codeDiv'>print( animal_dict.keys()[0] )</div>
"""

keys_dictionary_code = """animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}
print( animal_dict.keys() )
print( animal_dict.keys()[0] )"""

values_dictionary_definition = """Similar to keys, all of the values of a <button onclick="ajaxSubmit('dictionary')">dictionary</button> can be accessed by <i>dictionary.values()</i>. 
This returns a list of values:
<div id='codeDiv'>animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}</br>
print( animal_dict.values() )</div>
Since <i>dictionary.values()</i> returns a list, an individual value can be accessed with an index: 
<div id='codeDiv'>print( animal_dict.values()[0] )</div>"""

values_dictionary_code = """animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}
print( animal_dict.values() )
print( animal_dict.values()[0] )"""


dictionary_definition = "<div id='alternateRow'>" + dictionary_definition_short + "</div>"
dictionary_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('access dictionary')">access dictionary</button> """ + access_dictionary_definition + "</div>"
dictionary_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('update dictionary')">update dictionary</button> """ + update_dictionary_definition + "</div>"
dictionary_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('keys dictionary')">keys dictionary</button> """ + keys_dictionary_definition + "</div>"
dictionary_definition += "<div id='alternateRow'>" + """<button onclick="ajaxSubmit('values dictionary')">values dictionary</button> """ + values_dictionary_definition + "</div>"


dictionary_code = """animal_dict = {'fish': 'tuna', 'dog': 'pug', 'shark': 'great white'}
print( animal_dict )"""

mapping_data = {

    "data type": [data_type_definition, data_type_code],

    "integer": [integer_definition, integer_code],

    "float": [float_definition, float_code],

    "string": [string_definition, string_code],

    "global": [global_local_variable_definition, global_local_variable_code],

    "local": [global_local_variable_definition, global_local_variable_code],

    "random": [random_number_definition, random_number_code],

    ########## List
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

    ########## Dictionary
    "dictionary": [dictionary_definition, dictionary_code],

    "access dictionary": [access_dictionary_definition, access_dictionary_code],

    "update dictionary": [update_dictionary_definition, update_dictionary_code],

    "keys dictionary": [keys_dictionary_definition, keys_dictionary_code],

    "values dictionary": [values_dictionary_definition, values_dictionary_code],


    
}
