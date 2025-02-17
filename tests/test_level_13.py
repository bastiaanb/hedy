import hedy
import textwrap
from test_level_01 import HedyTester

class TestsLevel13(HedyTester):
  level = 13

  def test_while_equals(self):
    code = textwrap.dedent("""\
      antwoord is 0
      while antwoord != 25
          antwoord is ask 'Wat is 5 keer 5?'
      print 'Goed gedaan!'""")
    expected = textwrap.dedent("""\
    antwoord = 0
    while str(antwoord).zfill(100)!=str(25).zfill(100):
      antwoord = input(\'Wat is 5 keer 5?\')
      try:
        antwoord = int(antwoord)
      except ValueError:
        try:
          antwoord = float(antwoord)
        except ValueError:
          pass
    print(f'Goed gedaan!')""")

    self.multi_level_tester(
      code=code,
      expected=expected,
      extra_check_function=self.is_not_turtle(),
      test_name=self.name()
    )

  def test_while_smaller(self):
    code = textwrap.dedent("""\
      getal is 0
      while getal < 100000
          getal is ask 'HOGER!!!!!'
      print 'Hoog he?'""")
    expected = textwrap.dedent("""\
    getal = 0
    while str(getal).zfill(100)<str(100000).zfill(100):
      getal = input('HOGER!!!!!')
      try:
        getal = int(getal)
      except ValueError:
        try:
          getal = float(getal)
        except ValueError:
          pass
    print(f'Hoog he?')""")

    self.multi_level_tester(
      code=code,
      expected=expected,
      extra_check_function=self.is_not_turtle(),
      test_name=self.name()
    )
