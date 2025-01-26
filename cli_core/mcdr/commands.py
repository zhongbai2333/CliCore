from mcdreforged.api.all import *
from connect_core.api.interface import PluginControlInterface
from connect_core.api.tools import check_file_exists


class CommandActions(object):
    def __init__(
        self, control_interface: PluginControlInterface, mcdr: PluginServerInterface
    ):
        self._control_interface = control_interface
        self.__mcdr_server = mcdr
        self._is_server = control_interface.is_server()

        self.create_command()

    def create_command(self):
        builder = SimpleCommandBuilder()
        if self._is_server:
            builder.command("!!clicore", self._handle_help)
            builder.command("!!clicore help", self._handle_help)
            builder.command("!!clicore list", self._handle_list)
            builder.command(
                "!!clicore send msg <server_id> <message>", self._handle_send_msg
            )
            builder.command(
                "!!clicore send file <server_id> <path> <save_path",
                self._handle_send_file,
            )
            builder.command("!!clicore getkey", self._handle_getkey)
            builder.command("!!clicore reload", self._handle_reload)
        else:
            builder.command("!!clicore", self._handle_help)
            builder.command("!!clicore help", self._handle_help)
            builder.command("!!clicore info", self._handle_info)
            builder.command("!!clicore list", self._handle_list)
            builder.command(
                "!!clicore send msg <server_id> <message>", self._handle_send_msg
            )
            builder.command(
                "!!clicore send file <server_id> <path> <save_path",
                self._handle_send_file,
            )
            builder.command("!!clicore reload", self._handle_reload)

        builder.arg("server_id", Text)
        builder.arg("message", Text)
        builder.arg("path", Text)
        builder.arg("save_path", Text)

        builder.register(self.__mcdr_server)

        self.__mcdr_server.register_help_message(
            "!!clicore", self._control_interface.tr("mcdr.get_help")
        )

    def _handle_help(self, source: CommandSource):
        if self._is_server:
            source.reply(self._control_interface.tr("server_commands.help"))
        else:
            source.reply(self._control_interface.tr("client_commands.help"))

    def _handle_info(self, source: CommandSource):
        source.reply("==info==")
        server_id = self._control_interface.get_server_id()
        if server_id:
            source.reply(f"Main Server Connected! Server ID: {server_id}")
        else:
            source.reply("Main Server Disconnected!")

    def _handle_list(self, source: CommandSource):
        if self._is_server:
            from cli_core.global_data import get_server_list

            source.reply("==list==")
            for num, key in enumerate(get_server_list()):
                source.reply(f"{num + 1}. {key}")
        else:
            from cli_core.global_data import get_server_list

            source.reply("==list==")
            for num, key in enumerate(get_server_list()):
                source.reply(f"{num + 1}. {key}")

    def _handle_send_msg(self, source: CommandSource, context: CommandContext):
        self._control_interface.send_data(context["server_id"], "cli_core", {"msg": context["message"]})

    def _handle_send_file(self, source: CommandSource, context: CommandContext):
        if check_file_exists(context["save_path"]):
            self._control_interface.send_file(
                context["server_id"],
                "cli_core",
                context["path"],
                context["save_path"],
            )
        else:
            self._control_interface.info(self._control_interface.tr("server_commands.no_file"))

    def _handle_getkey(self, source: CommandSource):
        from connect_core.api.account import get_password

        source.reply(
            self._control_interface.tr("server_commands.getkey", get_password())
        )

    def _handle_reload(self, source: CommandSource):
        self.__mcdr_server.reload_plugin("cli_core")
