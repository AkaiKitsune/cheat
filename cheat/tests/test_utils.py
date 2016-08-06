from __future__ import print_function
import cheat.utils
import os
import unittest
from mock import patch
import sys
from mock import *


class TestUtils(unittest.TestCase):

    def test_colorize(self):
        os.environ['CHEATCOLORS'] = 'Yes' #enable cheatcolors
        ret = cheat.utils.colorize("""echo 'Diplodocus'""")
        # test cheats should now be colorized
        self.assertEquals(ret, u'''\x1b[36mecho\x1b[39;49;00m \x1b[33m'Diplodocus'\x1b[39;49;00m\n''')

        del os.environ['CHEATCOLORS'] #disable cheatcolors
        ret = cheat.utils.colorize("""echo 'Diplodocus'""")
        self.assertEquals(ret, "echo 'Diplodocus'") #test colorization has stoppped


    def test_die(self):
        #it's slightly painful to test the output of stderr, and honestly it's just informational anyway. We're dead.
        with self.assertRaises(SystemExit) as cm:
            cheat.utils.die('ded')
            self.assertEqual(cm.exception, "Error")


    def test_editor(self):
        os.environ['EDITOR'] = 'ed' #This is my attempt to avoid an editor war
        x = cheat.utils.editor()
        self.assertEqual(x, "ed")

        # it's slightly painful to test the output of stderr, and honestly it's just informational anyway. We're dead.
        del os.environ['EDITOR']
        with self.assertRaises(SystemExit) as cm:
            cheat.utils.editor()
            self.assertEqual(cm.exception, "Error")



    @patch('cheat.utils.print', create=True)
    def test_warn(self,print_):
        #warning function patched here to get extact response
        cheat.utils.warn('Ouch!')
        print_.assert_called_with('Ouch!',file=sys.stderr)
