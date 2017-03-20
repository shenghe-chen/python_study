#!/usr/bin/python
from __future__ import print_function


def display_inventory(inventory):
    i=0
    for good in inventory:
        i += 1
        print(inventory[good],good,sep=' ') 
    print('\nTotal number of items: ',i)


def add_to_inventory(inv, add):
    for m in add:
        if m in inv:
            inv[m]+=1
    {inv.setdefault(i,1) for i in add}
    return inv

d={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 

display_inventory(d)
inv = add_to_inventory(d, dragon_loot)
display_inventory(inv)
