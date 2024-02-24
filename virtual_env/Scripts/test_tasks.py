from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
from taskcode4 import Header, Visualization, Region
def test_Header():
      output = Header('Pink Morsel Visualization')
      assert output == 'Header: Pink Morsel Visualization'
def test_Visualization():
      output = Visualization('Pink Morsel Sales')
      assert output == 'Visualization: Pink Morsel Sales'
def test_Region():
      output = Region("['north', 'east', 'south', 'west', 'all'], 'all', id = 'region_picker', inline = True")
      assert output == "Region: ['north', 'east', 'south', 'west', 'all'], 'all', id = 'region_picker', inline = True"      