from connect_core.api.interface import PluginControlInterface

global _control_interface


def on_load(control_interface: "PluginControlInterface"):
    global _control_interface
    _control_interface = control_interface

    _control_interface.info(
        _control_interface.tr(
            "started.finish", "0.0.1"
        )
    )

    if not _control_interface.get_config():
        config = {"debug": False}
        _control_interface.save_config(config)

    if _control_interface.is_server():
        from cli_core.connectcore.server.commands import commands_main

        commands_main(_control_interface)
    else:
        from cli_core.connectcore.client.commands import commands_main

        commands_main(_control_interface)


def on_unload():
    pass


def new_connect(servers):
    flush_server_list(servers)


def del_connect(servers):
    flush_server_list(servers)


def flush_server_list(servers):
    from cli_core.global_data import set_server_list

    if _control_interface.is_server():
        from cli_core.connectcore.server.commands import set_completer_words

        server_list = {"all": None}
        debug_server_list = {}
        for i in servers:
            server_list[i] = None
            debug_server_list[i] = None
        if _control_interface.get_config()["debug"]:
            set_completer_words(
                {
                    "help": None,
                    "list": None,
                    "send": {"msg": server_list, "file": server_list},
                    "getkey": None,
                    "reload": None,
                    "get_history_packet": debug_server_list,
                    "exit": None,
                }
            )
        else:
            set_completer_words(
                {
                    "help": None,
                    "list": None,
                    "send": {"msg": server_list, "file": server_list},
                    "getkey": None,
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
        if _control_interface.get_config()["debug"]:
            set_completer_words(
                {
                    "help": None,
                    "info": None,
                    "list": None,
                    "send": {
                        "msg": server_list,
                        "file": server_list,
                    },
                    "get_history_packet": None,
                    "reload": None,
                    "exit": None,
                }
            )
        else:
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

def recv_data(server_id, data):
    _control_interface.info(f"[{server_id}] {data.get('msg', 'N/A')}")
