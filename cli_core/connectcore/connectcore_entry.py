from connect_core.api.interface import PluginControlInterface
import threading

global _control_interface


def on_load(control_interface: "PluginControlInterface"):
    global _control_interface
    _control_interface = control_interface

    _control_interface.info(
        _control_interface.tr("started.finish").format(
            _control_interface.sinfo["version"]
        )
    )

    if _control_interface.is_server():
        from cli_core.connectcore.server.commands import commands_main

        cli_thread = threading.Thread(target=commands_main, args=(_control_interface,))
        cli_thread.start()
    else:
        from cli_core.connectcore.client.commands import commands_main

        cli_thread = threading.Thread(target=commands_main, args=(_control_interface,))
        cli_thread.start()


def on_unload():
    pass


def new_connect(servers):
    flush_server_list(servers)


def del_connect(servers):
    flush_server_list(servers)


def flush_server_list(servers):
    from cli_core.connectcore.global_data import set_server_list

    if _control_interface.is_server():
        from cli_core.connectcore.server.commands import set_completer_words

        server_list = {"all": None}
        for i in servers:
            server_list[i] = None
        set_completer_words(
            {
                "help": None,
                "list": None,
                "send": {"msg": server_list, "file": server_list},
                "reload": None,
                "exit": None,
            }
        )

    else:
        from cli_core.connectcore.client.commands import set_completer_words

        server_list = {"all": None, "-----": None}
        for i in servers:
            if i != _control_interface.get_server_id():
                server_list[i] = None
        set_completer_words(
            {
                "help": None,
                "info": None,
                "list": None,
                "send": {
                    "msg": server_list,
                    "file": server_list,
                },
                "reload": None,
                "exit": None,
            }
        )

    set_server_list(servers)
