import re

webpage='''
            <hr>
    Hey I'm Pumple. <br>My Puzzle is very famous around here.
    Do you think you have what it takes to solve it? <br>
    No, you don't - haha! Noone solved it yet.
    <hr>


            <div>
                <pre class="mb-2">There are five bunnies.</pre>
            </div>

            <div>
                <pre class="mb-2">The backpack of Midnight is yellow.</pre>
            </div>

            <div>
                <pre class="mb-2">Angel&#39;s star sign is virgo.</pre>
            </div>

            <div>
                <pre class="mb-2">The camouflaged backpack is also green.</pre>
            </div>

            <div>
                <pre class="mb-2">The one-coloured backpack by Bunny was expensive.</pre>
            </div>

            <div>
                <pre class="mb-2">The bunny with the green backpack sits next to the bunny with the white backpack, on the left.</pre>
            </div>

            <div>
                <pre class="mb-2">The capricorn is also attractive.</pre>
            </div>

            <div>
                <pre class="mb-2">The scared bunny has a red backpack.</pre>
            </div>

            <div>
                <pre class="mb-2">The bunny with the chequered backpack sits in the middle.</pre>
            </div>

            <div>
                <pre class="mb-2">Snowball is the first bunny.</pre>
            </div>

            <div>
                <pre class="mb-2">The bunny with a dotted backpack sits next to the funny bunny.</pre>
            </div>

            <div>
                <pre class="mb-2">The funny bunny sits also next to the taurus.</pre>
            </div>

            <div>
                <pre class="mb-2">The scared bunny sits next to the aquarius.</pre>
            </div>

            <div>
                <pre class="mb-2">The backpack of the lovely bunny is striped.</pre>
            </div>

            <div>
                <pre class="mb-2">Thumper is a handsome bunny.</pre>
            </div>

            <div>
                <pre class="mb-2">Snowball sits next to the bunny with a blue backpack.</pre>
            </div>

        <form>
            <table class="table table-bordered table-striped m-3">
                <thead>
                <tr>
                    <th></th>
                    <th>Bunny #1</th>
                    <th>Bunny #2</th>
                    <th>Bunny #3</th>
                    <th>Bunny #4</th>
                    <th>Bunny #5</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>Name</td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Angel">Angel</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Snowball">Snowball</option>

                        </select>
                    </td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Angel">Angel</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Snowball">Snowball</option>

                        </select>
                    </td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Angel">Angel</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Snowball">Snowball</option>

                        </select>
                    </td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Angel">Angel</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Snowball">Snowball</option>

                        </select>
                    </td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Angel">Angel</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Snowball">Snowball</option>

                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Color of backpack</td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Yellow">Yellow</option>

                                <option value="Green">Green</option>

                                <option value="White">White</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                        </select>
                    </td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Yellow">Yellow</option>

                                <option value="Green">Green</option>

                                <option value="White">White</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                        </select>
                    </td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Yellow">Yellow</option>

                                <option value="Green">Green</option>

                                <option value="White">White</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                        </select>
                    </td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Yellow">Yellow</option>

                                <option value="Green">Green</option>

                                <option value="White">White</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                        </select>
                    </td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Yellow">Yellow</option>

                                <option value="Green">Green</option>

                                <option value="White">White</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Characteristics</td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Attractive">Attractive</option>

                                <option value="Scared">Scared</option>

                                <option value="Funny">Funny</option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                        </select>
                    </td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Attractive">Attractive</option>

                                <option value="Scared">Scared</option>

                                <option value="Funny">Funny</option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                        </select>
                    </td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Attractive">Attractive</option>

                                <option value="Scared">Scared</option>

                                <option value="Funny">Funny</option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                        </select>
                    </td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Attractive">Attractive</option>

                                <option value="Scared">Scared</option>

                                <option value="Funny">Funny</option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                        </select>
                    </td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Attractive">Attractive</option>

                                <option value="Scared">Scared</option>

                                <option value="Funny">Funny</option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Star sign</td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Virgo">Virgo</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Taurus">Taurus</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Pisces">Pisces</option>

                        </select>
                    </td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Virgo">Virgo</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Taurus">Taurus</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Pisces">Pisces</option>

                        </select>
                    </td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Virgo">Virgo</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Taurus">Taurus</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Pisces">Pisces</option>

                        </select>
                    </td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Virgo">Virgo</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Taurus">Taurus</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Pisces">Pisces</option>

                        </select>
                    </td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Virgo">Virgo</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Taurus">Taurus</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Pisces">Pisces</option>

                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Pattern on backback</td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="One-coloured">One-coloured</option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Striped">Striped</option>

                                <option value="Dotted">Dotted</option>

                        </select>
                    </td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="One-coloured">One-coloured</option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Striped">Striped</option>

                                <option value="Dotted">Dotted</option>

                        </select>
                    </td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="One-coloured">One-coloured</option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Striped">Striped</option>

                                <option value="Dotted">Dotted</option>

                        </select>
                    </td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="One-coloured">One-coloured</option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Striped">Striped</option>

                                <option value="Dotted">Dotted</option>

                        </select>
                    </td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="One-coloured">One-coloured</option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Striped">Striped</option>

                                <option value="Dotted">Dotted</option>

                        </select>
                    </td>
                </tr>
                </tbody>
            </table>
            <input class="btn btn-info mb-3" type="submit" value="submit">
        </form>
        <script type="text/javascript">
            'use strict';
            console.log('');
            $('form').submit(function (e) {
                e.preventDefault();
                e.stopPropagation();

                var str = 'Name,';

                $('td.names').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str += 'Color,';
                $('td.colors').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str += 'Characteristic,';
                $('td.characteristics').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str += 'Starsign,';
                $('td.starsigns').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str += 'Mask,';
                $('td.masks').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str = str.substr(0, str.length - 1);

                location.href = "/?solution=" + str;
            });
        </script>

            '''


from kanren import *

from kanren.core import lall

import time

def lefto(q, p, list):
        # give me q such that q is left of p in list
        # zip(list, list[1:]) gives a list of 2-tuples of neighboring combinations
        # which can then be pattern-matched against the query
        return membero((q,p), zip(list, list[1:]))

def nexto(q, p, list):
        # give me q such that q is next to p in list
        # match lefto(q, p) OR lefto(p, q)
        # requirement of vector args instead of tuples doesn't seem to be documented
        return conde([lefto(q, p, list)], [lefto(p, q, list)])


houses = var()

'''

http://log.liminastudio.com/programming/a-python-solution-to-the-zebra-problem-using-logic-programming

Nationality		Smokes		Drinks		Pet		Color
-----------------------------------------------------
Englishman
Swede
'''
'''
zebraRules = lall(
        # there are 5 houses
        (eq,            (var(), var(), var(), var(), var()), houses),
        # the Englishman's house is red
        (membero,       ('Englishman', var(), var(), var(), 'red'), houses),
        # the Swede has a dog
        (membero,       ('Swede', var(), var(), 'dog', var()), houses),
        # the Dane drinks tea
        (membero,       ('Dane', var(), 'tea', var(), var()), houses),
        # the Green house is left of the White house
        (lefto,         (var(), var(), var(), var(), 'green'),  (var(), var(), var(), var(), 'white'), houses),

        # coffee is the drink of the green house
        #(membero,       (var(), var(), 'coffee', var(), 'green'), houses),
        # the Pall Mall smoker has birds
        #(membero,       (var(), 'Pall Mall', var(), 'birds', var()), houses),
        # the yellow house smokes Dunhills
        #(membero,       (var(), 'Dunhill', var(), var(), 'yellow'), houses),
        # the middle house drinks milk
        #(eq,            (var(), var(), ( var(), var(), 'milk', var(), var() ) , var(), var()), houses),
        # #the Norwegian is the first house
        #(eq,            ( ('Norwegian', var(), var(), var(), var()),  var(), var(), var(), var()), houses),
        # the Blend smoker is in the house next to the house with cats
        #(nexto,         (var(), 'Blend', var(), var(), var()), (var(), var(), var(), 'cats', var()), houses),

        # the Dunhill smoker is next to the house where they have a horse
        #(nexto,         (var(), 'Dunhill', var(), var(), var()), (var(), var(), var(), 'horse', var()), houses),

        # the Blue Master smoker drinks beer
        #(membero,       (var(), 'Blue Master', 'beer', var(), var()), houses),
        # the German smokes Prince
        #(membero,       ('German', 'Prince', var(), var(), var()), houses),
        # the Norwegian is next to the blue house
        #(nexto,         ('Norwegian', var(), var(), var(), var()),(var(), var(), var(), var(), 'blue'), houses),

        # the house next to the Blend smoker drinks water
        #(nexto,         (var(), 'Blend', var(), var(), var()), (var(), var(), 'water', var(), var()), houses),

        # one of the houses has a zebra--but whose?
        #(membero,       (var(), var(), var(), 'zebra', var()), houses)
)
'''

bunnies = var()

#     Name    ColorofBackpack         Characteristics         StarSign        PatternBackpack


autobunny = var()
tuple_list = []
# Read all the rules and add them to the list

statements = []


regex = '<pre class="mb-2">(.*)</pre>'
hit = re.findall(regex, webpage)
for h in hit:
        statements.append(h)
'''        
statements.append("There are five bunnies.") #
statements.append("The capricorn is also attractive.")
statements.append("Thumper is a handsome bunny.")
statements.append("The scared bunny has a red backpack.")
statements.append("The backpack of Midnight is yellow.")
statements.append("The scared bunny sits next to the aquarius.")
statements.append("The camouflaged backpack is also green.")
statements.append("The one-coloured backpack by Bunny was expensive.")
statements.append("The bunny with a dotted backpack sits next to the funny bunny.")
statements.append("Snowball is the first bunny.") #
statements.append("The bunny with the chequered backpack sits in the middle.") #
statements.append("The funny bunny sits also next to the taurus.") #
statements.append("Angel's star sign is virgo.") #
statements.append("The backpack of the lovely bunny is striped.") #
statements.append("The bunny with the green backpack sits next to the bunny with the white backpack, on the left.") #
statements.append("Snowball sits next to the bunny with a blue backpack.") #
'''
while len(statements)>0:
        s = statements.pop()
        # Check which rule we're dealing with
        if "There are five bunnies." in s:
                tuple_list.append((eq,            (var(), var(), var(), var(), var()), bunnies))
        elif "The backpack of the " in s:
                # Regex it out
                regex = 'The backpack of the (.*) bunny is (.*)\.'
                hit = re.findall(regex, s)
                tuple_list.append((membero, (var(), var(), hit[0][0], var(), hit[0][1]), bunnies))
        elif "sits next to the bunny with a" in s:
                regex = '(.*) sits next to the bunny with a (.*) backpack'
                hit = re.findall(regex,s)
                tuple_list.append((nexto,         (hit[0][0], var(), var(), var(), var()),(var(), hit[0][1], var(), var(), var()), bunnies))
        elif ", on the left." in s:
                regex = 'The bunny with the (.*) backpack sits next to the bunny with the (.*) backpack, on the left'
                hit = re.findall(regex,s)
                tuple_list.append((lefto, (var(), hit[0][0], var(), var(), var()), (var(), hit[0][1], var(), var(), var()), bunnies))
        elif "star sign is" in s:
                regex = "(.*)&#39;s star sign is (.*)"
                hit = re.findall(regex,s)
                tuple_list.append((membero,       (hit[0][0], var(), var(), hit[0][1], var()), bunnies))
        elif "sits also next to the" in s:
                regex = "The (.*) bunny sits also next to the (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append((nexto,         (var(), var(), hit[0][0], var(), var()),(var(), var(), var(), hit[0][1], var()), bunnies))
        elif "sits in the middle" in s:
                regex = "The bunny with the (.*) backpack sits in the middle"
                hit = re.findall(regex, s)
                tuple_list.append((eq,            (var(), var(), (var(), var(), var(), var(), hit[0]), var(), var()), bunnies))
        elif "the first bunny" in s:
                regex = "(.*) is the first bunny"
                hit = re.findall(regex, s)
                tuple_list.append((eq,           ((hit[0], var(), var(), var(), var()),var(), var(), var(), var()), bunnies))
        elif "The bunny with a" in s:
                regex = "The bunny with a (.*) backpack sits next to the (.*) bunny"
                hit = re.findall(regex, s)
                tuple_list.append((nexto,         (var(), var(), hit[0][1], var(), var()), (var(), var(), var(), var(), hit[0][0]), bunnies))
        elif "was expensive" in s:
                regex = "The (.*) backpack by (.*) was expensive"
                hit = re.findall(regex, s)
                tuple_list.append((membero,       (hit[0][1], var(), var(), var(), hit[0][0]), bunnies))
        elif "backpack is also" in s:
                regex = "The (.*) backpack is also (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append((membero,       (var(), hit[0][1], var(), var(), hit[0][0]), bunnies))
        elif "sits next to the" in s: # Warning! Less generic than another rule
                regex = "The (.*) bunny sits next to the (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append((nexto, (var(), var(), hit[0][0], var(), var()), (var(), var(), var(), hit[0][1], var()), bunnies))
        elif "The backpack of" in s: # Warning! Less generic than another rule
                regex = "The backpack of (.*) is (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append((membero,       (hit[0][0], hit[0][1], var(), var(), var()), bunnies))
        elif "bunny has a" in s: # Warning! Less generic than another rule
                regex = "The (.*) bunny has a (.*) backpack"
                hit = re.findall(regex, s)
                tuple_list.append((membero,       (var(), hit[0][1], hit[0][0], var(), var()), bunnies))
        elif "is also" in s:
                regex = "The (.*) is also (.*)\."
                hit = re.findall(regex,s)
                tuple_list.append((membero,       (var(),var(), hit[0][1], hit[0][0], var()), bunnies))
        else:
                regex = "(.*) is a (.*) bunny"
                hit = re.findall(regex, s)
                tuple_list.append((membero,        (hit[0][0],    var(),  hit[0][1], var(), var()), bunnies))





autobunnyRules = lall(*tuple(tuple_list))





bunnyRules = lall(
        #There are five bunnies.
        (eq,            (var(), var(), var(), var(), var()), bunnies),

        #The backpack of Midnight is yellow.
        (membero,       ('Midnight', 'yellow', var(), var(), var()), bunnies),

        #Angel's star sign is virgo.
        (membero,       ('Angel', var(), var(), 'virgo', var()), bunnies),

        # Thumper is a handsome bunny.
        (membero,        ('Thumper',    var(),  'handsome', var(), var()), bunnies),

        #The bunny with the green backpack sits next to the bunny with the white backpack, on the left.
        (lefto, (var(), 'green', var(), var(), var()), (var(), 'white', var(), var(), var()), bunnies),

        #The one-coloured backpack by Bunny was expensive.
        (membero,       ('Bunny', var(), var(), var(), 'one-coloured'), bunnies),

        #The camouflaged backpack is also green.
         (membero,       (var(), 'green', var(), var(), 'camouflaged'), bunnies),


        #The capricorn is also attractive.
        (membero,       (var(),var(), 'attractive', 'capricorn', var()), bunnies),

        #The scared bunny has a red backpack.
        (membero,       (var(), 'red', 'scared', var(), var()), bunnies),

        #The bunny with the chequered backpack sits in the middle.
        (eq,            (var(), var(), (var(), var(), var(), var(), 'chequered'), var(), var()), bunnies),

        #Snowball is the first bunny.
        (eq,           (('Snowball', var(), var(), var(), var()),var(), var(), var(), var()), bunnies),

        #The bunny with a dotted backpack sits next to the funny bunny.
        (nexto,         (var(), var(), 'funny', var(), var()), (var(), var(), var(), var(), 'dotted'), bunnies),

        #The funny bunny sits also next to the taurus.
        (nexto,         (var(), var(), 'funny', var(), var()),(var(), var(), var(), 'taurus', var()), bunnies),

        #The scared bunny sits next to the aquarius.
        (nexto,         (var(), var(), 'scared', var(), var()),(var(), var(), var(), 'aquarius', var()), bunnies),

        #The backpack of the lovely bunny is striped.
        (membero,       (var(), var(),  'lovely', var(), 'striped'), bunnies),


        #Snowball sits next to the bunny with a blue backpack.
        (nexto,         ('Snowball', var(), var(), var(), var()),(var(), 'blue', var(), var(), var()), bunnies)
)

'''
t0 = time.time()
solutions = run(0, houses, zebraRules)
t1 = time.time()
dur = t1-t0

count = len(solutions)
#zebraOwner = [house for house in solutions[0] if 'zebra' in house][0][0]

print "%i solutions in %.2f seconds" % (count, dur)
#print "The %s is the owner of the zebra" % zebraOwner
print "Here are all the houses:"
for line in solutions[0]:
        print str(line)

'''

t0 = time.time()
solutions = run(0, bunnies, autobunnyRules)
t1 = time.time()
dur = t1-t0

count = len(solutions)
#zebraOwner = [house for house in solutions[0] if 'zebra' in house][0][0]

print "%i solutions in %.2f seconds" % (count, dur)
#print "The %s is the owner of the zebra" % zebraOwner
print "Here are all the bunnies:"
for line in solutions[0]:
        print str(line)


'''
More test data

  
            <div>
                <pre class="mb-2">There are five bunnies.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The backpack of Snowball is blue.</pre>
            </div>
        
            <div>
                <pre class="mb-2">Thumper&#39;s star sign is taurus.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The dotted backpack is also yellow.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The striped backpack by Bunny was expensive.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The bunny with the yellow backpack sits next to the bunny with the green backpack, on the left.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The pisces is also attractive.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The lovely bunny has a white backpack.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The bunny with the camouflaged backpack sits in the middle.</pre>
            </div>
        
            <div>
                <pre class="mb-2">Angel is the first bunny.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The bunny with a chequered backpack sits next to the scared bunny.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The scared bunny sits also next to the virgo.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The lovely bunny sits next to the aquarius.</pre>
            </div>
        
            <div>
                <pre class="mb-2">The backpack of the handsome bunny is one-coloured.</pre>
            </div>
        
            <div>
                <pre class="mb-2">Midnight is a funny bunny.</pre>
            </div>
        
            <div>
                <pre class="mb-2">Angel sits next to the bunny with a red backpack.</pre>
            </div>
        
'''

'''
Yet another:

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 26813
Set-Cookie: session=z.w8DF5SGkmLOUGQcgV+xJR/2NzOOOTs6AKoKRrlIaQK3YFUTdwzQ78CWciJZ/cjOa1fSEPfBwWYByr/H4664310cTDiD62WPrsBBZfiJDd585YwS01K9urLdcmOPKq5hzD1bumCX+QyRaaBXLcVgaSY5NtTftMTl8EnZwE9N4j2a2y4JTwZfZJ+L1js+BE2kujLyASuhjOLzcsjx4n+PgSvV8Exx3tvSDzFrxDe/msOJvImB3+AB1o/EGAzbYvt/cxnRrlpYlmuh1nTNW8xuQ3zbYN9FC8eU0ZmgJSz3BgwKc/X9PtNfrda+KuGl0x6Kve0KPv/8PPkkUcF0/A/1e5f22V4PZ8/7IDdBbFK+YnuMMjU1lX3ojhHZH7EbHnQyQsz7rzEgRjFonBfevUCTb9Z2b3qeAfQSKdLmDRq1DbjKUaDGQk7QWCIRHxZ3GH4VAo5uKRtU54itzSk/kJEKG1v8jVBt82+krKIN2E6K9Wyl51xhBNwqyNTxskd1g6LAnTuEuRZZLoG4CqT9+MLY0NX26a5/W82ay5wuvSIOsdIOqxNNBy6i2HwdAfVqIG+7AsEbkAAmDjlJv+38GZajMJvLBkPbJaOJxR/6TpF5KcVm0k3aGdSQ71Ke/28QSXANsu6SbhVf5VI3Kzki+fRpP6dFwrJRxZEMpvvLjQQSRQqCJEU/QFlax3Du9hoW9cCWmCfxcIaHyA8moqennk4/cdXqrfEJkh+l+q/1tKmBpIL4Znh/jB5/ro3/dH8CEF0Klb+E8VxZpnc/QF9TG+rC1QzncvShRYQ0UvCmaby4+sXQD4afceP0/4AFHoieacIucS/KiL1OA6eGA5jwBeqKLKoOpxYMxfmA6CZ6eKRN+KU2GH+H3cMWjGPR9gT61TxrUE9I+t00849nsW1TYjvp0xbNTAAwpMT4I3AM3Sm29S//6SY+P/2d0iHK40is3sk3MjxsWLeNLOa2LhuU6QZz9Gqc82daeXSu6V5fKlaP7etmaZLSCctMCXPaVkpFdmrHYfbPPuwvP7FxTN5fqQWt3nBbZVt6R51kF8TbJDbDBTui8gUDdPHQ=.xve0DGu2yDxkBURbCiK5OQ==.UJY8RMbaMkg9MydF+d4frQ==; Expires=Fri, 07-Jun-2019 21:27:26 GMT; HttpOnly; Path=/
Server: Werkzeug/0.15.2 Python/3.6.7
Date: Tue, 07 May 2019 21:27:26 GMT

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Travel Navigator</title>
    <link rel="stylesheet" href="/static/css/fa-5.6.3.min.css">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/css/main.css">
</head>


<body>
<script src="/static/js/jquery-3.3.1.min.js"></script>

<!-- Navigation -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
    <div class="container">
        <a class="navbar-brand" href="/"><i class="fas fa-drafting-compass"></i> Travel
            Navigator</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive"
                aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">

                    <li class="nav-item">
                        <a class="nav-link" href="/exit">
                            <button class="btn btn-danger">Exit</button>
                        </a>
                    </li>

            </ul>
        </div>
    </div>
</nav>

<!-- Page Content -->
<div class="container">
    <div class="row">
        <div class="col-lg-12">
            <h1 class="mt-5"></h1>





    <div class="row">
        <div class="col-3" style="border-right: 1px solid black">
            <span class="font-weight-bold">Carrots</span>
            <br>

                ð¥


                ð¥


                ð¥


                ð¥


                ð¥

                    <br>


                ð¥


                ð¥


                ð¥


                ð¥


                ð¥


            <hr>
            <div style="height: 200px">
                <h5>Navigator says:</h5>
                <p>Boring - you can do that on your own!</p>

            </div>


                <hr>
                <h6>Solved:</h6>
                <div>
                    <ul class="checkmark">

                            <li class="tick">Warmup</li>

                            <li class="tick">C0tt0nt4il Ch3ck</li>

                            <li class="tick">Mathonymous</li>

                    </ul>
                </div>

        </div>
        <div class="col-9">

    <h3>Pumple's Puzzle</h3>
    <img src="/static/img/ch14.jpg">
    <hr>
    Hey I'm Pumple. <br>My Puzzle is very famous around here.
    Do you think you have what it takes to solve it? <br>
    No, you don't - haha! Noone solved it yet.
    <hr>


            <div>
                <pre class="mb-2">There are five bunnies.</pre>
            </div>

            <div>
                <pre class="mb-2">The backpack of Midnight is green.</pre>
            </div>

            <div>
                <pre class="mb-2">Thumper&#39;s star sign is pisces.</pre>
            </div>

            <div>
                <pre class="mb-2">The striped backpack is also yellow.</pre>
            </div>

            <div>
                <pre class="mb-2">The camouflaged backpack by Bunny was expensive.</pre>
            </div>

            <div>
                <pre class="mb-2">The bunny with the yellow backpack sits next to the bunny with the red backpack, on the left.</pre>
            </div>

            <div>
                <pre class="mb-2">The capricorn is also lovely.</pre>
            </div>

            <div>
                <pre class="mb-2">The handsome bunny has a blue backpack.</pre>
            </div>

            <div>
                <pre class="mb-2">The bunny with the chequered backpack sits in the middle.</pre>
            </div>

            <div>
                <pre class="mb-2">Angel is the first bunny.</pre>
            </div>

            <div>
                <pre class="mb-2">The bunny with a one-coloured backpack sits next to the funny bunny.</pre>
            </div>

            <div>
                <pre class="mb-2">The funny bunny sits also next to the aquarius.</pre>
            </div>

            <div>
                <pre class="mb-2">The handsome bunny sits next to the virgo.</pre>
            </div>

            <div>
                <pre class="mb-2">The backpack of the scared bunny is dotted.</pre>
            </div>

            <div>
                <pre class="mb-2">Snowball is a attractive bunny.</pre>
            </div>

            <div>
                <pre class="mb-2">Angel sits next to the bunny with a white backpack.</pre>
            </div>

        <form>
            <table class="table table-bordered table-striped m-3">
                <thead>
                <tr>
                    <th></th>
                    <th>Bunny #1</th>
                    <th>Bunny #2</th>
                    <th>Bunny #3</th>
                    <th>Bunny #4</th>
                    <th>Bunny #5</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>Name</td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Snowball">Snowball</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Angel">Angel</option>

                        </select>
                    </td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Snowball">Snowball</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Angel">Angel</option>

                        </select>
                    </td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Snowball">Snowball</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Angel">Angel</option>

                        </select>
                    </td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Snowball">Snowball</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Angel">Angel</option>

                        </select>
                    </td>
                    <td class="names">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Midnight">Midnight</option>

                                <option value="Thumper">Thumper</option>

                                <option value="Snowball">Snowball</option>

                                <option value="Bunny">Bunny</option>

                                <option value="Angel">Angel</option>

                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Color of backpack</td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Green">Green</option>

                                <option value="Yellow">Yellow</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                                <option value="White">White</option>

                        </select>
                    </td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Green">Green</option>

                                <option value="Yellow">Yellow</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                                <option value="White">White</option>

                        </select>
                    </td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Green">Green</option>

                                <option value="Yellow">Yellow</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                                <option value="White">White</option>

                        </select>
                    </td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Green">Green</option>

                                <option value="Yellow">Yellow</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                                <option value="White">White</option>

                        </select>
                    </td>
                    <td class="colors">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Green">Green</option>

                                <option value="Yellow">Yellow</option>

                                <option value="Red">Red</option>

                                <option value="Blue">Blue</option>

                                <option value="White">White</option>

                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Characteristics</td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                                <option value="Funny">Funny</option>

                                <option value="Scared">Scared</option>

                                <option value="Attractive">Attractive</option>

                        </select>
                    </td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                                <option value="Funny">Funny</option>

                                <option value="Scared">Scared</option>

                                <option value="Attractive">Attractive</option>

                        </select>
                    </td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                                <option value="Funny">Funny</option>

                                <option value="Scared">Scared</option>

                                <option value="Attractive">Attractive</option>

                        </select>
                    </td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                                <option value="Funny">Funny</option>

                                <option value="Scared">Scared</option>

                                <option value="Attractive">Attractive</option>

                        </select>
                    </td>
                    <td class="characteristics">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Lovely">Lovely</option>

                                <option value="Handsome">Handsome</option>

                                <option value="Funny">Funny</option>

                                <option value="Scared">Scared</option>

                                <option value="Attractive">Attractive</option>

                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Star sign</td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Pisces">Pisces</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Virgo">Virgo</option>

                                <option value="Taurus">Taurus</option>

                        </select>
                    </td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Pisces">Pisces</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Virgo">Virgo</option>

                                <option value="Taurus">Taurus</option>

                        </select>
                    </td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Pisces">Pisces</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Virgo">Virgo</option>

                                <option value="Taurus">Taurus</option>

                        </select>
                    </td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Pisces">Pisces</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Virgo">Virgo</option>

                                <option value="Taurus">Taurus</option>

                        </select>
                    </td>
                    <td class="starsigns">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Pisces">Pisces</option>

                                <option value="Capricorn">Capricorn</option>

                                <option value="Aquarius">Aquarius</option>

                                <option value="Virgo">Virgo</option>

                                <option value="Taurus">Taurus</option>

                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Pattern on backback</td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Striped">Striped</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Dotted">Dotted</option>

                                <option value="One-coloured">One-coloured</option>

                        </select>
                    </td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Striped">Striped</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Dotted">Dotted</option>

                                <option value="One-coloured">One-coloured</option>

                        </select>
                    </td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Striped">Striped</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Dotted">Dotted</option>

                                <option value="One-coloured">One-coloured</option>

                        </select>
                    </td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Striped">Striped</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Dotted">Dotted</option>

                                <option value="One-coloured">One-coloured</option>

                        </select>
                    </td>
                    <td class="masks">
                        <select class="custom-select">
                            <option class="selected"></option>

                                <option value="Camouflaged">Camouflaged</option>

                                <option value="Striped">Striped</option>

                                <option value="Chequered">Chequered</option>

                                <option value="Dotted">Dotted</option>

                                <option value="One-coloured">One-coloured</option>

                        </select>
                    </td>
                </tr>
                </tbody>
            </table>
            <input class="btn btn-info mb-3" type="submit" value="submit">
        </form>
        <script type="text/javascript">
            'use strict';
            console.log('');
            $('form').submit(function (e) {
                e.preventDefault();
                e.stopPropagation();

                var str = 'Name,';

                $('td.names').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str += 'Color,';
                $('td.colors').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str += 'Characteristic,';
                $('td.characteristics').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str += 'Starsign,';
                $('td.starsigns').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str += 'Mask,';
                $('td.masks').each(function () {
                    str += $(this).find('select').first().val() + ','
                });
                str = str.substr(0, str.length - 1);

                location.href = "/?solution=" + str;
            });
        </script>



        </div>
    </div>


        </div>
    </div>
</div>

<!-- Bootstrap core JavaScript -->

<script type="application/javascript" src="/static/js/popper.min.js"></script>
<script type="application/javascript" src="/static/js/bootstrap.min.js"></script>

<script>
    $(function () {
        $('[data-toggle="popover"]').popover()
    })
</script>
</body>

</html>'''