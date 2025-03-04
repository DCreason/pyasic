from pyasic.device.algorithm import MinerAlgo
from pyasic.device.models import MinerModel
from pyasic.miners.device.makes import LuckyMinerMake


class LV07(LuckyMinerMake):
    raw_model = MinerModel.LUCKYMINER.LV07

    expected_hashboards = 1
    expected_chips = 1
    expected_fans = 1
    algo = MinerAlgo.SHA256
