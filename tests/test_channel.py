from src.channel import Channel
import os.path

moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
def test_channel():
    assert moscowpython.print_info() == None
    assert os.path.exists('../homework-2') == True
