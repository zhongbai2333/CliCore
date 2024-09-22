from connect_core.api.tools import restart_program, check_file_exists, append_to_path
import os
from connect_core.api.interface import PluginControlInterface

global _control_interface


def do_info(args):
    """
    显示主服务器信息。
    """
    _control_interface.info("==info==")
    server_id = _control_interface.get_server_id()
    if server_id:
        _control_interface.info(f"Main Server Connected! Server ID: {server_id}")
    else:
        _control_interface.info("Main Server Disconnected!")


def do_list(args):
    """
    显示当前可用的子服务器列表。
    """
    from cli_core.connectcore.global_data import get_server_list

    _control_interface.info("==list==")
    for num, key in enumerate(get_server_list()):
        _control_interface.info(f"{num + 1}. {key}")


def do_send(args):
    """
    向指定服务器发送消息或文件。
    """
    from cli_core.connectcore.global_data import get_server_list

    commands = args.split()
    if len(commands) < 3:
        _control_interface.info(_control_interface.tr("client_commands.send"))
        return None

    server_name, content = commands[1], commands[2]
    if commands[0] == "msg" and (
        server_name == "all"
        or server_name == "-----"
        or server_name in get_server_list()
    ):
        _control_interface.send_data(server_name, "cli_core", {"msg": content})
    elif (
        commands[0] == "file"
        and (
            server_name == "all"
            or server_name == "-----"
            or server_name in get_server_list()
        )
        and len(commands) == 4
    ):
        if check_file_exists(content):
            save_path = commands[3]
            _control_interface.send_file(
                server_name,
                "cli_core",
                content,
                append_to_path(save_path, os.path.basename(content)),
            )
        else:
            _control_interface.info(_control_interface.tr("client_commands.no_file"))
    else:
        _control_interface.info(_control_interface.tr("client_commands.send"))


def do_reload(args):
    """
    重载程序和插件
    """
    restart_program()


def do_help(args):
    """
    显示所有可用命令的帮助信息。
    """
    _control_interface.info(_control_interface.tr("client_commands.help"))


def do_exit(args):
    """
    退出命令行系统
    """
    _cli_core.running = False


def commands_main(control_interface: "PluginControlInterface"):
    """
    Client 命令行系统主程序
    """
    from cli_core.connectcore.cli_core import CommandLineInterface

    global _control_interface, _cli_core

    _control_interface = control_interface
    _cli_core = CommandLineInterface(_control_interface, "ConnectCoreClient> ")

    _cli_core.add_command("help", do_help)
    _cli_core.add_command("info", do_info)
    _cli_core.add_command("list", do_list)
    _cli_core.add_command("send", do_send)
    _cli_core.add_command("reload", do_reload)
    _cli_core.add_command("exit", do_exit)

    _cli_core.set_completer_words(
        {
            "help": None,
            "info": None,
            "list": None,
            "send": {
                "msg": {"all": None, "-----": None},
                "file": {"all": None, "-----": None},
            },
            "reload": None,
            "exit": None,
        }
    )

    os.system(f"title ConnectCore Client")

    _cli_core.set_prompt("ConnectCoreClient> ")

    _cli_core.start()


def set_completer_words(comp: dict):
    _cli_core.set_completer_words(comp)
    _cli_core.flush_cli()
