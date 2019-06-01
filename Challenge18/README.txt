The decompiled wasm code:


int validateRange(unsigned int param0) {

    if((((unsigned int)(param0 == 48)) | ((unsigned int)(param0 == 49)) | ((unsigned int)(param0 == 51)) | ((unsigned int)(param0 == 52)) | ((unsigned int)(param0 == 53)) | ((unsigned int)(param0 == 72)) | ((unsigned int)(param0 == 76)) | ((unsigned int)(param0 == 88)) | ((unsigned int)(param0 == 99)) | ((unsigned int)(param0 == 100)) | ((unsigned int)(param0 == 102)) | ((unsigned int)(param0 == 114)))) {
        return 1;
    }
    else {
        return 0;
    }
}

int validatePassword(unsigned int param0, unsigned int param1, unsigned int param2, unsigned int param3, int param4, unsigned int param5, int param6, int param7, int param8, int param9, unsigned int param10, int param11, unsigned int param12, int param13, unsigned int param14, unsigned int param15, unsigned int param16, unsigned int param17, unsigned int param18, unsigned int param19, unsigned int param20, unsigned int param21, int param22, int param23) {
    functions();
    *24 = v4;
    *25 = v10;
    *26 = v17;
    *27 = v23;
    *28 = v5;
    *29 = v11;
    *30 = v16;
    *31 = v22;
    *32 = v6;
    *33 = v12;
    *34 = v18;
    *35 = v24;
    *36 = v7;
    *37 = v13;
    *38 = v19;
    *39 = v25;
    *40 = v8;
    *41 = v14;
    *42 = v20;
    *43 = v26;
    *44 = v9;
    *45 = v15;
    *46 = v21;
    *47 = v27;
    int v0 = 4;

    do {
        int v1 = validateRange(((unsigned int)(*(v0 + 24))));

        if(v1 == 0) {
            goto loc_50000118;
        }
        else {
            ++v0;
        }
    }
    while(param23 <= 24);

    if(param0 != 84) {
        return 0;
    }
    else if(param1 != 104) {
        return 0;
    }
    else if(param2 != 51) {
        return 0;
    }
    else if(param3 != 80) {
        return 0;
    }
    else if(param17 != param23) {
        return 0;
    }
    else if(param12 != param16) {
        return 0;
    }
    else if(param15 != param22) {
        return 0;
    }
    else if(param5 - param7 != 14) {
        return 0;
    }
    else if(param14 + 1 != param15) {
        return 0;
    }
    else if(param9 % param8 != 40) {
        return 0;
    }
    else if(param5 - param9 + param19 != 79) {
        return 0;
    }
    else if(param7 - param14 != param20) {
        return 0;
    }
    else if(param9 % param4 * 2 != param13) {
        return 0;
    }
    else if(param13 % param6 != 20) {
        return 0;
    }
    else if(param21 - 46 != param11 % param13) {
        return 0;
    }
    else if(param7 % param6 != param10) {
        return 0;
    }
    else if(param23 % param22 != 2) {
        return 0;
    }
    else {
        v0 = 4;
        unsigned int v2 = 0, v3 = 0;
        goto loc_50000228;
    loc_50000118:
        return 0;

        do {
        loc_50000228:
            v2 += (unsigned int)(*(v0 + 24));
            v3 ^= (unsigned int)(*(v0 + 24));
            ++v0;
        }
        while(v0 <= 24);

        if(v2 != 1352) {
            return 0;
        }
        else {

            if(v3 != 44) {
                return 0;
            }

            decrypt();
            return 1;
        }
    }
}

int decrypt() {

    do {
        *ptr0 = (unsigned char)(((unsigned int)(*(ptr0 + 6))) ^ ((unsigned int)(*ptr0)));
        ptr0 = (int*)(((char*)ptr0) + 1);
    }
    while(((unsigned char)(((int)ptr0) <= 24)));

    return 1337;
}



Using z3 (pip install z3-solver), we can write a small program:

from z3 import *

p0 = Int('p0')
p1 = Int('p1')
p2 = Int('p2')
p3 = Int('p3')
p4 = Int('p4')
p5 = Int('p5')
p6 = Int('p6')
p7 = Int('p7')
p8 = Int('p8')
p9 = Int('p9')
p10 = Int('p10')
p11 = Int('p11')
p12 = Int('p12')
p13 = Int('p13')
p14 = Int('p14')
p15 = Int('p15')
p16 = Int('p16')
p17 = Int('p17')
p18 = Int('p18')
p19 = Int('p19')
p20 = Int('p20')
p21 = Int('p21')
p22 = Int('p22')
p23 = Int('p23')

values = [48,49,51,52,53,72,76,88,99,100,102,114]
s=Solver()
s.add(p0==84)
s.add(p1==104)
s.add(p2==51)
s.add(p3==80)
s.add(p17==p23)
s.add(p12==p16)
s.add(p15==p22)
s.add((p5-p7)==14)
s.add((p14+1)==p15)
s.add((p9%p8)==40)
s.add((p5-p9+p19)==79)
s.add((p7-p14)==p20)
s.add((p9%p4)*2==p13)
s.add((p13%p6)==20)
s.add((p21-46)==(p11%p13))
s.add((p7%p6)==p10)
s.add((p23%p22)==2)
s.add(Or([p4==i for i in values]))
s.add(Or([p5==i for i in values]))
s.add(Or([p6==i for i in values]))
s.add(Or([p7==i for i in values]))
s.add(Or([p8==i for i in values]))
s.add(Or([p9==i for i in values]))
s.add(Or([p10==i for i in values]))
s.add(Or([p11==i for i in values]))
s.add(Or([p12==i for i in values]))
s.add(Or([p13==i for i in values]))
s.add(Or([p14==i for i in values]))
s.add(Or([p15==i for i in values]))
s.add(Or([p16==i for i in values]))
s.add(Or([p17==i for i in values]))
s.add(Or([p18==i for i in values]))
s.add(Or([p19==i for i in values]))
s.add(Or([p20==i for i in values]))
s.add(Or([p21==i for i in values]))
s.add(Or([p22==i for i in values]))
s.add(Or([p23==i for i in values]))
# Sum of all values >= p4 == 1352
# Or of all values >= p4 == 44
s.add(p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14+p15+p16+p17+p18+p19+p20+p21+p22+p23==1352)
res=s.check()
print(res)
res=s.model()
print(res)

(Important: We need to have the additional checks from the wasm like the sum == 1452!)

When we run the program we get:

daubsi@ubuntu:~/tinned-z3$ python solveme.py
sat
[p23 = 51,
 p22 = 49,
 p21 = 76,
 p20 = 52,
 p19 = 53,
 p18 = 49,
 p17 = 51,
 p16 = 99,
 p15 = 49,
 p14 = 48,
 p13 = 72,
 p12 = 99,
 p11 = 102,
 p10 = 48,
 p9 = 88,
 p8 = 48,
 p7 = 100,
 p6 = 52,
 p5 = 114,
 p4 = 52,
 p3 = 80,
 p2 = 51,
 p1 = 104,
 p0 = 84]

Where these ASCII char codes translate to:

https://gchq.github.io/CyberChef/#recipe=From_Charcode('Comma',10)&input=Cjg0LDEwNCw1MSw4MCw1MiwxMTQsNTIsMTAwLDQ4LDg4LDQ4LDEwMiw5OSw3Miw0OCw0OSw5OSw1MSw0OSw1Myw1Miw3Niw0OSw1MQ

Th3P4r4d0X0fcH01c3154L13




