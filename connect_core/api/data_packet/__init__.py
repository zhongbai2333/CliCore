class DataPacket(object):
    """数据包处理相关代码"""

    def __init__(self):
        self.TYPE_TEST_CONNECT = (-1, 0)
        self.TYPE_PING = (0, 1)
        self.TYPE_PONG = (0, 2)
        self.TYPE_CONTROL_STOP = (1, 0)
        self.TYPE_CONTROL_RELOAD = (1, 1)
        self.TYPE_CONTROL_MAINTENANCE = (1, 2)
        self.TYPE_CONTROL_RESUME = (1, 3)
        self.TYPE_REGISTER = (2, 0)
        self.TYPE_REGISTERED = (2, 1)
        self.TYPE_REGISTER_ERROR = (2, 2)
        self.TYPE_LOGIN = (3, 0)
        self.TYPE_LOGINED = (3, 1)
        self.TYPE_NEW_LOGIN = (3, 2)
        self.TYPE_DEL_LOGIN = (3, 3)
        self.TYPE_LOGIN_ERROR = (3, 4)
        self.TYPE_DATA_SEND = (4, 0)
        self.TYPE_DATA_SENDOK = (4, 1)
        self.TYPE_DATA_ERROR = (4, 2)
        self.TYPE_FILE_SEND = (5, 0)
        self.TYPE_FILE_SENDING = (5, 1)
        self.TYPE_FILE_SENDOK = (5, 2)
        self.TYPE_FILE_ERROR = (5, 3)

        self.DEFAULT_TO_FROM = ("-----", "-----")
        self.DEFAULT_SERVER = ("-----", "system")
        self.DEFAULT_ALL = ("all", "system")

    def get_data_packet(
        self, Type: tuple, ToInfo: tuple, FromInfo: tuple, Data: any
    ) -> dict:
        """
        获取数据包格式

        Args:
            Type (tuple): 数据包类型和状态
            ToInfo (tuple): 数据包目标信息
            FromInfo (tuple): 数据包来源信息
            Data (any): 数据
        :return: 数据包字典
        """
        pass

    def get_history_packet(self, server_id: str, old_sid: int) -> list:
        """
        获取历史数据包

        Args:
            server_id (str): 服务器id
            old_sid (int): 旧sid
        :return: 历史数据包
        """
        pass

    def add_recv_packet(self, server_id: str, packet: dict) -> None:
        """
        添加接收到的数据包

        Args:
            server_id (str): 服务器id
            packet (dict): 数据包
        """
        pass

    def del_server_id(self, server_id: str) -> None:
        """
        删除指定服务器id的数据包

        Args:
            server_id (str): 服务器id
        """
        pass

    def _get_sid(self, server_id: str, add_sid: bool = True) -> dict:
        """
        获取sid

        Args:
            server_id (str): 服务器id
            add_sid (bool): 是否添加sid，默认为True
        :return: sid字典
        """
        pass

    def get_file_hash(self, file_path, algorithm="sha256") -> str | None:
        """
        获取文件的哈希值。

        Args:
            file_path (str): 文件路径
            algorithm (str): 哈希算法，默认使用 'sha256'

        Returns:
            str: 文件的哈希值，如果文件不存在则返回 None
        """
        pass

    def verify_file_hash(self, file_path, expected_hash, algorithm="sha256") -> bool:
        """
        验证文件的哈希值。

        Args:
            file_path (str): 文件路径
            expected_hash (str): 预期的哈希值
            algorithm (str): 哈希算法，默认使用 'sha256'

        Returns:
            bool: 如果哈希值匹配则返回 True，否则返回 False
        """
        pass

    def generate_md5_checksum(self, data):
        """
        Generate MD5 checksum for the given data.

        Args:
            data: The data to generate checksum for. Must be convertible to bytes.

        Returns:
            str: The generated MD5 checksum as a hex string.
        """
        pass

    def verify_md5_checksum(self, data, checksum) -> bool:
        """
        校验数据是否匹配给定的 MD5 校验和。

        :param data: 输入数据，类型为 bytes。
        :param checksum: 输入的 MD5 校验和，类型为 str。
        :return: 如果校验通过返回 True，否则返回 False。
        """
        pass
