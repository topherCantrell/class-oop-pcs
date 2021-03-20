import requests
import html

IMAGE_MAP = {
    'crump.jpg' : '<img src="https://uah.instructure.com/courses/44030/files/4361279/preview" alt="crump.jpg" width="133" height="141" data-api-endpoint="https://uah.instructure.com/api/v1/courses/44030/files/4361279" data-api-returntype="File" />'
}

def skip_blank_lines(lines,pos):    
    while True:
        if pos>=len(lines):
            return pos
        if lines[pos].strip():
            return pos
        pos+=1    

def encode_special(text,pos):
    while True:
        i = text.find('`')
        if i>=0:
            j = text.find('`',i+1)
            if j<0:
                raise Exception('line '+str(pos+1)+' bad `...` syntax')
            spc = text[i+1:j]
            spc_text = '</span><code>'+spc+'</code><span>'
            text = text[0:i] + spc_text + text[j+1:]
            continue
        return text

def generate_paragraph(lines,pos):
    print('<p>',end='')
    first_line = True
    while True:
        if pos>=len(lines):
            print('</p>')
            return pos
        g = lines[pos].strip()            
        if not g or not g[0].isalnum():
            print('</p>')
            return pos
        g = encode_special(g,pos)
        if not first_line:
            print()
        else:
            first_line = False            
        print(g,end='')
        pos += 1        

with open('../Topics/01_Encapsulation/01_01_OO/README.md') as f:
    lines = f.readlines()
    
if not lines[0].startswith('# '):
    raise Exception('First line must be "# ..."')

pos = 1

while True:
    
    pos = skip_blank_lines(lines,pos)
    
    # End of the file
    if pos>=len(lines):
        break
    
    # Plain alpha-numeric ... this is a regular old paragraph
    g = lines[pos].strip()
    if g[0].isalnum():
        pos = generate_paragraph(lines,pos)        
        continue
    
    # Header ... count the '#'
    if g.startswith('#'):
        cnt = 0
        while g[cnt]=='#':
            cnt += 1
        print('<h'+str(cnt)+'>'+g[cnt:].strip()+'</h'+str(cnt)+'>')
        pos += 1
        continue
    
    # Simple embedded image
    if g.startswith('![]('):
        name = g[4:-1]
        if name not in IMAGE_MAP:
            raise Exception('Line '+str(pos+1)+' unknown image:'+name)
        print('<p>'+IMAGE_MAP[name]+'</p>')
        pos += 1
        continue
    
    # Formatted code block
    if g.startswith('```python'):  # Add other OR here
        g = g[3:]
        extra = ''
        i = g.find(' ')
        if i>=0:
            extra = g[i+1:].strip()
            g = g[0:i]
        code = ''
        pos+=1
        while not lines[pos].startswith('```'):
            code = code + lines[pos]
            pos+=1
        pos += 1
        
        resp = requests.post('http://hilite.me',
                             data={'code':code,'style':'colorful','linenos':'yes','lexer':g}).text
                             
        i = resp.find('<textarea id="html"')
        i = resp.find('>',i)
        j = resp.find('</textarea>',i)
        hilite_code = resp[i+1:j]
        hilite_code = html.unescape(hilite_code)
        
        i = hilite_code.find('<table>')
        header = '<span style="color: #3366ff; font-size: 8pt;"><em><strong>'+g+' '+extra+'</strong></em></span>'
        
        hilite_code = hilite_code[0:i] + header + hilite_code[i:] 
        
        print(hilite_code)
        
        continue
        
    raise Exception('## Unexpected line '+str(pos+1)+': '+lines[pos])
    
