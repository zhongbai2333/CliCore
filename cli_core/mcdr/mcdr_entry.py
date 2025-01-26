from mcdreforged.api.all import *
from connect_core.api.mcdr import get_plugin_control_interface
from cli_core.mcdr.commands import CommandActions
from cli_core.global_data import set_server_list


__mcdr_server, _control_interface = None, None


def on_load(server: PluginServerInterface, _):
    global __mcdr_server, _control_interface
    __mcdr_server = server
    _control_interface = get_plugin_control_interface(
        "cli_core", "cli_core.mcdr.mcdr_entry", server
    )
    if not _control_interface:
        return

    _control_interface.info(_control_interface.tr("started.finish", "0.0.1"))
    if not _control_interface.get_config():
        config = {"debug": False}
        _control_interface.save_config(config)

    CommandActions(_control_interface, __mcdr_server)


def new_connect(servers):
    set_server_list(servers)


def del_connect(servers):
    set_server_list(servers)
