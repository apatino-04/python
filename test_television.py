import unittest
from television import *


class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = Television()

    def test_init(self):
        #   test starting values
        self.assertEqual(str(self.tv), "Power = False, Channel = 0, Volume = 0")

    def test_tv_on(self):
        self.tv.power()             # Power on
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.power()             # Power off
        self.assertEqual(str(self.tv), "Power = False, Channel = 0, Volume = 0")

    def test_mute(self):
        self.tv.power()              # Power on
        self.tv.volume_up()          # Volume up
        self.tv.mute()               # mute
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.mute()               # unmute
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")
        self.tv.power()              # Power off
        self.tv.mute()               # mute, because tv is off mute shouldn't work
        self.assertEqual(str(self.tv), "Power = False, Channel = 0, Volume = 1")

    def test_channel_up(self):
        self.tv.channel_up()        # Increase channel while tv is off
        self.assertEqual(str(self.tv), "Power = False, Channel = 0, Volume = 0")
        self.tv.power()             # Turn Tv on
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 1, Volume = 0")
        self.tv.channel_up()        # Increase channel
        self.assertEqual(str(self.tv), "Power = True, Channel = 2, Volume = 0")
        self.tv.channel_up()        # Increase channel
        self.assertEqual(str(self.tv), "Power = True, Channel = 3, Volume = 0")
        self.tv.channel_up()        # Increase channel
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")

    def test_channel_down(self):
        self.tv.channel_down()      # decrease channel while tv is off
        self.assertEqual(str(self.tv), "Power = False, Channel = 0, Volume = 0")
        self.tv.power()             # Turn Tv on
        self.tv.channel_down()      # decrease channel
        self.assertEqual(str(self.tv), "Power = True, Channel = 3, Volume = 0")
        self.tv.channel_down()      # decrease channel
        self.assertEqual(str(self.tv), "Power = True, Channel = 2, Volume = 0")
        self.tv.channel_down()      # decrease channel
        self.assertEqual(str(self.tv), "Power = True, Channel = 1, Volume = 0")

    def test_volume_up(self):
        self.tv.volume_up()         # Increase volume while tv is off
        self.assertEqual(str(self.tv), "Power = False, Channel = 0, Volume = 0")
        self.tv.power()             # Turn Tv on
        self.tv.volume_up()         # Increase volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")
        self.tv.volume_up()         # Increase volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 2")
        self.tv.volume_up()         # Increase volume at limit
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 2")
        self.tv.mute()              # mute
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.volume_up()         # Increase volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 2")

    def test_volume_down(self):
        self.tv.volume_down()       # decrease volume while tv is off
        self.assertEqual(str(self.tv), "Power = False, Channel = 0, Volume = 0")
        self.tv.power()             # Turn Tv on
        self.tv.volume_down()       # decrease volume at limit
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.volume_up()         # Increase volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")
        self.tv.mute()              # mute
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.volume_down()       # decrease volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.volume_up()  # Increase volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")
        self.tv.volume_up()         # Increase volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 2")
        self.tv.volume_down()       # decrease volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")
        self.tv.volume_down()       # decrease volume
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")


if __name__ == '__main__':
    unittest.main()
