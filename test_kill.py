import json
from unittest.mock import patch, Mock
import unittest
from unittest import TestCase
from kill import Kill


class TestKill(TestCase):

    def test_proc_info(self):
        client = Kill()
        client.handle()
