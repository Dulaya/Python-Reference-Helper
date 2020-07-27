mapping_data = {



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
        list.remove(c)<br/>
        print( list )<br/>
        >> ['a', 'b', 'd', 'e', 'b']
        """,
        """list = ['a', 'b', 'c', 'd', 'e', 'b']
list.remove(c)
print( list )"""
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

    
}
