from connect_core.api.interface import CoreControlInterface


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


def get_plugins() -> dict:
    """
    获取插件列表

    :return: 插件列表
    """
    pass
