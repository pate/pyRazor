# Alex Lusco
"""
  Unit tests which just shotgun a bunch of templates
  at the problem and make sure they render correctly.
"""

import unittest
import pyrazor

class RenderTests(unittest.TestCase):

  def testSimple(self):
    """Tests a simple rendering case."""
    template = "test"
    self.assertEquals(template, pyrazor.render(template))

  def testIgnoreMultiline(self):
    """Tests that the @: does not affect output."""
    self.assertEquals("", pyrazor.render("@:\n\ta=3"))

  def testSimpleModel(self):
    class test:
      pass

    model = test()
    model.a = 3
    model.b = 5
    self.assertEquals("3", pyrazor.render("@model.a", model))
    self.assertEquals("3 5", pyrazor.render("@model.a @model.b", model))
    self.assertEquals("8", pyrazor.render("@(model.a + model.b)", model))

  def testModelInstaceOf(self):
    m = dict()
    m['test'] = 3
    self.assertEquals("3", pyrazor.render("@model dict\n@model['test']", m))

  def testModelSubclassOf(self):
    class subdict(dict):
      pass
    m = subdict()
    m['test'] = 3
    self.assertEquals("3", pyrazor.render("@model dict\n@model['test']", m))

if __name__ == '__main__':
      unittest.main()

