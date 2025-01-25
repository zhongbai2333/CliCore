from connect_core.api.tools import restart_program, check_file_exists, append_to_path
import os, sys
from connect_core.api.interface import PluginControlInterface
from connect_core.api.account import get_password
from connect_core.api.tools import new_thread

global _control_interface


# 启动核心命令行程序
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
        _control_interface.info(_control_interface.tr("server_commands.send"))
        return None

    server_name, content = commands[1], commands[2]
    if commands[0] == "msg" and (
        server_name == "all" or server_name in get_server_list()
    ):
        _control_interface.send_data(server_name, "cli_core", {"msg": content})
    elif (
        commands[0] == "file"
        and (server_name == "all" or server_name in get_server_list())
        and len(commands) == 4
    ):
        save_path = commands[3]
        if check_file_exists(content):
            _control_interface.send_file(
                server_name,
                "cli_core",
                content,
                append_to_path(save_path, os.path.basename(content)),
            )
        else:
            _control_interface.info(_control_interface.tr("server_commands.no_file"))
    else:
        _control_interface.info(_control_interface.tr("server_commands.send"))


def do_help(args):
    """
    显示所有可用命令的帮助信息。
    """
    _control_interface.info(_control_interface.tr("server_commands.help"))


def do_reload(args):
    """
    重载程序和插件
    """
    restart_program()


def do_exit(args):
    """
    退出命令行系统
    """
    _cli_core.running = False


def do_getkey(args):
    """
    获取服务器的公钥
    """
    _control_interface.info(
        _control_interface.tr("server_commands.getkey", get_password())
    )


def do_get_history_packet(args):
    """
    获取历史数据包
    """
    if args:
        _control_interface.info("==get_history_packet==")
        for num, packet in enumerate(_control_interface.get_history_packet(args)):
            _control_interface.info(f"{num + 1}. {packet}")
    else:
        _control_interface.info(_control_interface.tr("server_commands.none_server_id"))


@new_thread("CliCoreServer")
def commands_main(control_interface: "PluginControlInterface"):
    """
    Server 命令行系统主程序
    """
    from cli_core.connectcore.cli_core import CommandLineInterface

    global _control_interface, _cli_core

    _control_interface = control_interface
    _cli_core = CommandLineInterface(_control_interface, "ConnectCoreServer> ")

    _cli_core.add_command("help", do_help)
    _cli_core.add_command("list", do_list)
    _cli_core.add_command("send", do_send)
    _cli_core.add_command("getkey", do_getkey)
    _cli_core.add_command("reload", do_reload)
    _cli_core.add_command("exit", do_exit)

    if _control_interface.get_config()["debug"]:
        _cli_core.add_command("get_history_packet", do_get_history_packet)
        _cli_core.set_completer_words(
            {
                "help": None,
                "list": None,
                "send": {"msg": {"all": None}, "file": {"all": None}},
                "getkey": None,
                "get_history_packet": None,
                "reload": None,
                "exit": None,
            }
        )
    else:
        _cli_core.set_completer_words(
            {
                "help": None,
                "list": None,
                "send": {"msg": {"all": None}, "file": {"all": None}},
                "getkey": None,
                "reload": None,
                "exit": None,
            }
        )

    os.system(f"title ConnectCore Server")

    _cli_core.set_prompt("ConnectCoreServer> ")

    _cli_core.start()


def set_completer_words(comp: dict):
    _cli_core.set_completer_words(comp)
    _cli_core.flush_cli()
