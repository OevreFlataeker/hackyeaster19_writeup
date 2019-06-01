import re
import urllib

def mathonymous(n1,n2,n3,n4,n5,n6,res):
    s = [str(float(n1.strip())),'',str(float(n2.strip())),'',str(float(n3.strip())),'',str(float(n4.strip())),'',str(float(n5.strip())),'',str(float(n6.strip()))]
    should = res

    for op1 in ['+','-','/','*']:
        s[1] = op1
        for op2 in ['+','-','/','*']:
            s[3] = op2
            for op3 in ['+','-','/','*']:
                s[5] = op3
                for op4 in ['+','-','/','*']:
                    s[7] = op4
                    for op5 in ['+','-','/','*']:
                        s[9] = op5

                        v = "".join(s)
                        #print(v)
                        res = eval(v)

                        #if should is None:
                        #    print(v,res)
                        #else:
                        if abs(float(should)-res) <= 0.01:
                            print(v,res,should)
                            yield s
                            #print(v,res,should)



def mathonymous2(n1,n2,n3,n4,n5,n6,res):
    s = ['(((((',n1,'',n2,')','',n3,')','',n4,')','',n5,')','',n6,')']
    should = res

    for op1 in ['+','-','/','*']:
        s[2] = op1
        for op2 in ['+','-','/','*']:
            s[5] = op2
            for op3 in ['+','-','/','*']:
                s[8] = op3
                for op4 in ['+','-','/','*']:
                    s[11] = op4
                    for op5 in ['+','-','/','*']:
                        s[14] = op5
                        v = "".join(s)
                        #print(v)
                        res = eval(v)
                        if should==None:
                            print(v,res)
                        else:
                            if abs(float(should)-res) <= 0.01:
                                print(v,res,should)
                                #return s
                            if res!=0:
                                print(v,should,(abs(float(should)-res)))
    return s


webpage = '''   <div>

            One in mind .... <br>
            plus ... <br>
            minus .... <br>
            WAAAAAH.<br><br>
            Oh wow it's you. I already heard you helped my brother.
            <br>

            This one should be easy for you then:

            <hr>
            <form method="get"
                  oninput="this.op.value=$('#op1').val()+$('#op2').val()+$('#op3').val()+$('#op4').val()+$('#op5').val();">
                <table>
                    
                        <input type="hidden" value="" name="op">
                        <td><code style="font-size: 1em; margin: 10px">16 </code></td>
                        <td><input class="form-control" id="op1" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 17 </code></td>
                        <td><input class="form-control" id="op2" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 9 </code></td>
                        <td><input class="form-control" id="op3" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 2 </code></td>
                        <td><input class="form-control" id="op4" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 4 </code></td>
                        <td><input class="form-control" id="op5" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 5</code></td>
                        <td><code style="font-size: 1em">= 2.904575163398693</code></td>
                    </tr>
                </table>
                <hr>

                <div class="form-group">
                    <input type="submit" class="btn btn-primary" value="Submit">
                </div>
            </form>'''

regex = '<td><code style="font-size: 1em; margin: 10px">(.*)</code></td>'
hit = re.findall(regex, webpage)

hit = ['19','10','12','14','13','13']

if len(hit)!=6:
    print("Error")
else:
    n1 = hit[0]
    n2 = hit[1]
    n3 = hit[2]
    n4 = hit[3]
    n5 = hit[4]
    n6 = hit[5]
    regex = '<td><code style="font-size: 1em">=(.*)</code></td>'
    hit = re.findall(regex, webpage)
    should = hit[0]
    should = '488.19999999999993'
    mathonymous(n1, n2, n3, n4, n5, n6, should)
    all_res = []
    all_res = mathonymous(n1,n2,n3,n4,n5,n6,should)
    URL = "http://somewhere"
    for val in all_res:
        print(val)
        l = [val[x] for x in range(len(val)) if x % 2 == 1]
        print(l)
        ops = "".join(l)
        print(ops)


        mygeturl = "{0}?op={1}".format(URL, urllib.quote(ops,safe=''))
        print(mygeturl)



