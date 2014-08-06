#ifndef    _H_QUERY_SRV_MSG_H
#define    _H_QUERY_SRV_MSG_H

#include "base.ice"

module Test1
{
    enum Color {
        RED = 3,
        BLUE = 0xF,
    };
    //sequence<string> Strings;
    //dictionary<int, string> ISMap;


    //const int k1 = 3;

    //struct actor {
    //    string key;
    //};

    interface HelloI {
        ["amd"] void func(string A, out LL::int s);
    };
};

module Test2 {
};

#endif
