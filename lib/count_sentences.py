#!/usr/bin/env python3

class MyString:
  def __init__(self, value =''):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)


  def has_ending(self, character):
    if self._value and self._value.endswith(character):
      return True
    return False

  def is_sentence(self):
      return self.has_ending('.')

  def is_question(self):
      return self.has_ending('?')

  def is_exclamation(self):
      return self.has_ending('!')

 
  def count_sentences(self):
    i = 0
    for word in self._value.split():
      if word.endswith('.') or word.endswith('!') or word.endswith('?'):
        i += 1
    return i

  