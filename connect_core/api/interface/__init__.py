class CoreControlInterface:
    def __init__(self):
        pass
    # =============
    #  Json Editer
    # =============
    def get_config(self, config_path: str = None) -> dict:
        """
        获取配置文件

        Args:
            config_path (str): 配置文件目录, 默认为插件或服务器默认 config 路径

        Returns:
            dict: 配置文件字典
        """
        pass

    def save_config(self, config_data: dict, config_path: str = None) -> None:
        """
        写入配置文件

        Args:
            config_data (dict): 新的配置项字典
            config_path (str): 配置文件目录, 默认为插件或服务器默认 config 路径
        """
        pass

    # =============
    #   Translate
    # =============
    def translate(self, key: str) -> str:
        """
        获取翻译项

        Args:
            key (str): 翻译文件关键字

        Returns:
            str: 翻译文本
        """
        pass

    def tr(self, key: str) -> str:
        """
        获取翻译项 | `translate函数的别称`

        Args:
            key (str): 翻译文件关键字

        Returns:
            str: 翻译文本
        """
        pass

    # =============
    #   Log Print
    # =============
    def info(self, msg: any):
        """
        输出INFO级别的日志信息。

        Args:
            msg (any): 日志消息内容。
        """
        pass

    def warn(self, msg: any):
        """
        输出WARN级别的日志信息。

        Args:
            msg (any): 日志消息内容。
        """
        pass

    def error(self, msg: any):
        """
        输出ERROR级别的日志信息。

        Args:
            msg (any): 日志消息内容。
        """
        pass

    def debug(self, msg: any):
        """
        输出DEBUG级别的日志信息。

        Args:
            msg (any): 日志消息内容。
        """
        pass


class PluginControlInterface(CoreControlInterface):

    def __init__(self, sid: str, sinfo: dict, self_path: str, config_path: str):
        """
        插件控制接口

        Args:
            sid (str): 插件ID
            sinfo (dict): 插件Info
            self_path (str): 自身路径
            config_path (str): 配置文件路径
        """
        # 导入
        super().__init__()

        self.sid = ""
        self.sinfo = {}
        self.self_path = ""
        self.config_path = ""
        self.log_system = False
        self.language = ""
        pass

    # ========
    #   Send
    # ========
    def send_data(self, server_id: str, plugin_id: str, data: dict):
        """
        向指定的服务器发送消息。

        Args:
            server_id (str): 目标服务器的唯一标识符。
            plugin_id (str): 目标服务器插件的唯一标识符
            data (str): 要发送的数据。
        """
        pass

    def send_file(
        self, server_id: str, plugin_id: str, file_path: str, save_path: str = None
    ):
        """
        向指定的服务器发送文件。

        Args:
            server_id (str): 目标服务器的唯一标识符。
            plugin_id (str): 目标服务器插件的唯一标识符
            file_path (str): 要发送的文件目录。
            save_path (str): 要保存的位置。
        """
        pass

    # =========
    #   Tools
    # =========
    def is_server(self) -> bool:
        """
        判断是否为服务器

        Returns:
            bool: 是/否
        """
        pass

    def get_server_id(self) -> str:
        """
        客户端反馈服务器ID

        Returns:
            str: 服务器ID
        """
        pass
