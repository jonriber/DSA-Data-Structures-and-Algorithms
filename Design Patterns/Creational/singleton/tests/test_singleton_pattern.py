import pytest
from ..singleton_pattern import Singleton

class TestSingletonClass1:
  def test_class1_is_singleton(self):
    class1 = Singleton()
    class2 = Singleton()
    assert class1 is class2

class TestSingletonClass2:
  def test_class2_is_singleton(self):
    class2 = Singleton()
    class3 = Singleton()
    assert class2 is class3

class TestSingletonClass3:
  def test_class3_is_singleton(self):
    class1 = Singleton()
    class3 = Singleton()
    assert class1 is class3
