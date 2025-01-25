from mcdreforged.api.all import *
from connect_core.api.mcdr import get_plugin_control_interface
from cli_core.mcdr.commands import CommandActions


__mcdr_server, _control_interface = None, None


def on_load(server: PluginServerInterface, _):
    global __mcdr_server, _control_interface
    __mcdr_server = server
    _control_interface = get_plugin_control_interface(
        "cli_core", "cli_core.connectcore.connectcore_entry", server
    )
    if not _control_interface:
        return
    _control_interface.info("Plugin Server Interface loaded")
    CommandActions(_control_interface, __mcdr_server)


