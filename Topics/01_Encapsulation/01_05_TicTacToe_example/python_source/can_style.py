html = """
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><table><tr><td><pre style="margin: 0; line-height: 125%"> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33</pre></td><td><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get_average</span>(grades):
    <span style="color: #888888"># Code here</span>
    <span style="color: #008800; font-weight: bold">return</span> <span style="color: #6600EE; font-weight: bold">75.5</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get_number_fails</span>(grades):
    <span style="color: #888888"># Code here</span>
    <span style="color: #008800; font-weight: bold">return</span> <span style="color: #0000DD; font-weight: bold">3</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get_highest_grade</span>(grades):
    <span style="color: #888888"># Code here</span>
    <span style="color: #008800; font-weight: bold">return</span> <span style="color: #0000DD; font-weight: bold">90</span>

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get_grade</span>(grades, index):
    <span style="color: #008800; font-weight: bold">return</span> grades[index]

<span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">set_grade</span>(grades, index, value):
    grades[index] <span style="color: #333333">=</span> value

jan <span style="color: #333333">=</span> [<span style="color: #0000DD; font-weight: bold">100</span>,<span style="color: #0000DD; font-weight: bold">100</span>,<span style="color: #0000DD; font-weight: bold">80</span>,<span style="color: #0000DD; font-weight: bold">95</span>,<span style="color: #0000DD; font-weight: bold">100</span>,<span style="color: #0000DD; font-weight: bold">90</span>,<span style="color: #0000DD; font-weight: bold">92</span>,<span style="color: #0000DD; font-weight: bold">84</span>,<span style="color: #0000DD; font-weight: bold">98</span>,<span style="color: #0000DD; font-weight: bold">100</span>]    
bobby <span style="color: #333333">=</span> [<span style="color: #0000DD; font-weight: bold">75</span>,<span style="color: #0000DD; font-weight: bold">66</span>,<span style="color: #0000DD; font-weight: bold">84</span>,<span style="color: #0000DD; font-weight: bold">90</span>,<span style="color: #0000DD; font-weight: bold">92</span>,<span style="color: #0000DD; font-weight: bold">100</span>,<span style="color: #0000DD; font-weight: bold">38</span>,<span style="color: #0000DD; font-weight: bold">73</span>,<span style="color: #0000DD; font-weight: bold">22</span>,<span style="color: #0000DD; font-weight: bold">95</span>]

<span style="color: #008800; font-weight: bold">print</span>( get_average(jan) )

<span style="color: #008800; font-weight: bold">print</span>( get_highest_grade(jan) )

v <span style="color: #333333">=</span> get_grade(jan, <span style="color: #0000DD; font-weight: bold">8</span>)
set_grade(bobby, <span style="color: #0000DD; font-weight: bold">8</span>, v)

set_grade(bobby, <span style="color: #0000DD; font-weight: bold">7</span>, get_grade(jan, <span style="color: #0000DD; font-weight: bold">7</span>))

<span style="color: #008800; font-weight: bold">print</span>( get_grade(bobby, <span style="color: #0000DD; font-weight: bold">8</span>) )

<span style="color: #008800; font-weight: bold">print</span>( get_number_fails(bobby) )
</pre></td></tr></table></div>
"""

print('<p style="display: none;">-----------------------------------------------</p>')
html = html.replace('<pre style="','<pre style="border-radius:unset;')
print(html)
print('<p style="display: none;">-----------------------------------------------</p>')
