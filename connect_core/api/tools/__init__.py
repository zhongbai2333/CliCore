from typing import Optional, Union, Callable


def new_thread(arg: Optional[Union[str, Callable]] = None):
    """
    启动一个新的线程运行装饰的函数，同时支持类方法和普通函数。
    """
    pass


def auto_trigger(interval: float, thread_name: Optional[str] = None):
    pass


def restart_program() -> None:
    """
    重启程序，使用当前的Python解释器重新执行当前脚本。
    """
    pass


def check_file_exists(file_path) -> bool:
    """
    检查目录中的特定文件是否存在。

    Args:
        file_path (str): 文件路径

    Returns:
        bool: 如果文件存在则返回 True，否则返回 False
    """
    pass


def append_to_path(path, filename) -> str:
    """
    Appends a filename to the given path if it is a directory.

    :param path: The path to check and modify.
    :param filename: The filename to append if path is a directory.
    :return: The modified path.
    """
    pass


def encode_base64(data: str) -> str:
    """
    对输入的数据进行Base64编码

    Args:
        data (str): 需要编码的字节数据
    :return: 编码后的字符串
    """
    pass


def decode_base64(encoded_data: str) -> str:
    """
    对Base64编码的数据进行解码

    Args:
        encoded_data(str): Base64编码的字符串
    :return: 解码后的字节数据
    """
    pass


def get_all_internal_ips() -> list:
    """
    获取所有网卡的内网IP地址
    :return: 一个列表, 包含所有内网IP地址
    """
    pass


def get_external_ip() -> str:
    """
    获取公网地址
    :return: 一个公网IP
    """
    pass
