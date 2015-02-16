#ifndef    _H_QUERY_SRV_MSG_H
#define    _H_QUERY_SRV_MSG_H

//#include "base.ice"

module Test1
{

    const int k1 = 3;

    enum Color {
        RED = 13,
        BLUE = 0xF,
        YELLOW = k1,
    };

    //module Inner {
    //    const int k2 = Color::RED;
    //};

    sequence<string> Strings;
    //sequence<string> Uids;
    //dictionary<int, string> ISMap;
    //sequence<ISMap>  MapSeq;



    struct actor {
        string key;
        Strings seq;
        int     keydd;
    };

    interface HelloI {
        ["amd"] void func(string name, out int data);
    };
};
/*
module Test2 {};
*/
#endif
