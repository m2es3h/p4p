
from __future__ import print_function

import unittest
import weakref, gc

from ..client import Context

class TestProviders(unittest.TestCase):
    def tearDown(self):
        gc.collect() # try to provoke any crashes here so they can be associated with this testcase
    def testProviders(self):
        providers = Context.providers()
        self.assertIn('pva', providers)
        self.assertIn('ca', providers)

class TestPVA(unittest.TestCase):
    def setUp(self):
        self.ctxt = Context("pva")
    def tearDown(self):
        self.ctxt = None
        gc.collect()

    def testChan(self):
        chan = self.ctxt.channel("completelyInvalidChannelName")

        self.assertEqual(chan.getName(), "completelyInvalidChannelName")

    def testGetAbort(self):
        chan = self.ctxt.channel("completelyInvalidChannelName")
        _X = [None]
        def fn(V):
            _X[0] = V
        op = chan.get(fn)

        op.cancel()

        self.assertIsNone(_X[0])
