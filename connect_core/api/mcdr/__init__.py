from connect_core.api.interface import PluginControlInterface
from mcdreforged.api.types import PluginServerInterface


def get_plugin_control_interface(
    sid: str, enter_point: str, mcdr: PluginServerInterface
) -> PluginControlInterface:
    """
    获取插件控制接口

    Args:
        sid (str): 插件ID
        enter_point (str): 入口点
        mcdr (PluginServerInterface): MCDR接口
    Returns:
        PluginControlInterface: 插件控制接口
    """
    pass
