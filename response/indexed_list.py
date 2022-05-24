#!/usr/bin/env python3

class Item(object):

  def __init__(self, data=None, next_item=None):
    self.next_item = next_item
    self.data = data

class LinkedList(object):

  def __init__(self, items=None):
    self.head = None
    self.lookup = []
    if items:
      for item in reversed(items):    # Added a reversed here to make the init more intuitive
        self.push(item)

  def push(self, data):
    '''Add an item to the front of the LinkedList'''
    item = Item(data, self.head)
    self.head = item

  def __getitem__(self, index):
    '''Get the list item at a position, starting at 0'''
    item = self.head
    if item is None: 
      raise IndexError('List is empty')
    for _ in range(index):
      if item is None: 
        raise IndexError('Index out of range')
      item = item.next_item
    return item.data

  def to_array(self):
    items = []
    item = self.head
    while(item):
      items.append(item.data)
      item = item.next_item
    return items

def main():
    list = LinkedList([12, 13, "apple", "banana"])

    # Iterate through list to find value (uses getitem())
    v = list[2]
    print("list[2]: %s" % v)

    # Convert to an array, then use index
    array = list.to_array()
    v = array[2]
    print("array[2]: %s" % v)


if __name__ == "__main__":
    main()
