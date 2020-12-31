#!/usr/bin/python

#merge internet
ori_file = ["internet/seperate_notes/lesson1.md",
                "internet/seperate_notes/lesson2.md",
                "internet/seperate_notes/lesson3.md",
                "internet/seperate_notes/lesson4.md",
                "internet/seperate_notes/lesson5.md",
                "internet/seperate_notes/lesson6.md"]
target_file = "internet/internet_merged.md"
merged_note = open(target_file,'w')
for str in ori_file:
    seperate_note = open(str,'r').readlines()
    merged_note.writelines(seperate_note)

#merge operation system
ori_file = ["operation_system/notes/Chapter01.md",
            "operation_system/notes/Chapter02_1.md",
            "operation_system/notes/Chapter02_2.md",
            "operation_system/notes/Chapter02_3.md",
            "operation_system/notes/Chapter02_4.md",
            "operation_system/notes/Chapter03_1.md",
            "operation_system/notes/Chapter03_2.md",
            "operation_system/notes/Chapter04_1.md",
            "operation_system/notes/Chapter04_2.md",
            "operation_system/notes/Chapter05.md"]
target_file = "operation_system/operation_system_merged.md"
merged_note = open(target_file,'w')
for str in ori_file:
    seperate_note = open(str,'r').readlines()
    merged_note.writelines(seperate_note)

#merge C++Primer
ori_file = ["C++Primer/chapter01.md",
                    "C++Primer/chapter02.md",
                    "C++Primer/chapter03.md",
                    "C++Primer/chapter06.md",
                    "C++Primer/chapter07.md",
                    "C++Primer/chapter10.md"]
target_file = "C++Primer/notes.md"
merged_note = open(target_file,'w')
for str in ori_file:
    seperate_note = open(str,'r').readlines()
    merged_note.writelines(seperate_note)