def outer():
    def inner1():
        def inner2():
            def inner3():
                v5 = "You just got dominated, Comrade."
                print("inner3()")
                print(v1 + ", " + v2 + ", " + v3 + ", " + v4 + ", " + v5)
                #end of inner3

            v4 = "You are like the cyclops of greek myth; except you are scottish, and I Hate You!"
            print("inner2()")
            print(v1 + ", " + v2 + ", " + v3 + ", " + v4)
            inner3()
            #end of inner2

        v2 = "Got anything funny to say about that, funny man!"
        v3 = "How do you like that, All Quiet on The Western Front?"

        print("inner1()")
        print(v1 + ", " + v2 + ", " + v3)
        inner2()     
        #end of inner1



    v1 = "What's the matter hippy, hair get in your eyes"
    inner1()
    #end of outer


print("Nested Functions in python\n")

outer()
