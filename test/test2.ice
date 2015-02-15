#ifndef    _H_QUERY_SRV_MSG_H
#define    _H_QUERY_SRV_MSG_H


module Test1
{
    const int k1 = 3;
    module T2 {
        const int x = k1;
    };




    enum Color {
        RED = 3,
        BLUE = 0xF,
        //YELLOW = k1,
    };

    module Inner {

    };

    sequence<string> Strings;
    sequence<string> Uids;
    dictionary<int, string> ISMap;




    //struct actor {
    //    string key;
    //};

    //interface HelloI {
    //    ["amd"] void func(string A, out LL::int s);
    //};
};

//module Test2 {
//};

#endif
