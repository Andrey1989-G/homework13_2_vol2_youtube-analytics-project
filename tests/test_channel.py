from src.channel import Channel

moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
def test_channel():
    assert moscowpython.print_info() == None