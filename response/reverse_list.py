#!/usr/bin/env python3

class Item(object):

  def __init__(self, data=None, next_item=None):
    self.next_item = next_item
    self.data = data

class LinkedList(object):

  def __init__(self, items=None):
    self.head = None
    if items:
      for item in reversed(items):    # Added a reversed here to make the init more intuitive
        self.push(item)

  def push(self, data):
    '''Add an item to the front of the LinkedList'''
    item = Item(data, self.head)
    self.head = item

  def check_loop(self):
    '''Check if there is a loop in the LinkedList'''
    items = set()
    current_item = self.head
    while (current_item):
      if (current_item in items): 
        return True
      items.add(current_item)
      current_item = current_item.next_item
    return False


  def reverse(self):
    '''Reverse LinkedList in place using iterative O(n) approach'''
    previous_item = None
    current_item = self.head
    while(current_item):
      next_item = current_item.next_item
      current_item.next_item = previous_item
      previous_item = current_item
      current_item = next_item
    self.head = previous_item
    
    return self

  def __str__(self):
    items = []
    item = self.head
    while(item):
      items.append(item.data)
      item = item.next_item
    return str(items)


def main():
    list = LinkedList([12, 13, "apple", "banana"])

    # If "given" a LinkedList, should check there's no loops
    if list.check_loop():
      raise ValueError('Loop in the provided LinkedList!')

    # Reverse in place
    list.reverse()

    print("Reversed LinkedList: %s" % list)


if __name__ == "__main__":
    main()