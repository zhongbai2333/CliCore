from connect_core.api.interface import CoreControlInterface


# Public
def init_plugin_main(control_interface: "CoreControlInterface"):
    """
    插件初始化
    """
    pass


def new_connect(server_list: list) -> None:
    """
    新的连接

    Args:
        sid (str): 插件ID
        server_list (list): 服务器列表
    """
    pass


def del_connect(server_list: list) -> None:
    """
    断开的连接

    Args:
        sid (str): 插件ID
        server_list (list): 服务器列表
    """
    pass


def connected():
    """
    连接成功
    """
    pass


def disconnected():
    """
    断开连接
    """
    pass


def recv_data(sid: str, data: dict):
    """
    收到数据包

    Args:
        sid (str): 插件ID
        data (dict): 收到的数据
    """
    pass


def recv_file(sid: str, file: str):
    """
    收到文件

    Args:
        sid (str): 插件ID
        file (str): 收到的文件地址
    """
    pass


def unload_plugin(sid: str):
    """
    卸载插件

    Args:
        sid (str): 插件ID
    """
    pass


def reload_plugin(sid: str):
    """
    重载插件

    Args:
        sid (str): 插件ID
    """
    pass
