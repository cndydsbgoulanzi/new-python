#! /usr/bin/env python
import sys,shelve
def store_person(db):
    """

    Query user for data and store it in the shelf object
    """

    pid = raw_input('Enter unique ID number: ')
    person = {}
    person['name'] =raw_input('Enter name: ']
    person['age'] =raw_input('Enter age: ']
    person['phone'] =raw_input('Enter phone number: ']

    db[pid] = person

def lookup_person(db):
    """

    Query user for ID and desired field,and fetch the corresponding data from the shelf object
    """

    pid = raw_input('Enter unique ID number: ')
    field = raw_input('What would you like to know? (name,age,phone) ')
    field = field.strip().lower()
    print filed.capitalize() + ':' \
           db[pid][field]

def print_help():
    print 'The available commands are:'
    print 'store  : Stores imformation about a person'
    print 'lookup : Looks up a person from ID number'
    print 'quit   : Save changes and exit'
    print '?      : Prints this message'

def enter_command():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('~/database.dat')#You mat want to change this name
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_persom(database)
            elif cmd == 'lookup':
                lookup_person(databse)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
    database.close()

if _name_ == '_main_':main()
