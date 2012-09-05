import sublime
import sublime_plugin

class ToggleWhiteSpaceCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        white_space = "selection" if settings.get("draw_white_space", "selection") != "selection" else "all"
        settings.set("draw_white_space", white_space)
        sublime.save_settings("Preferences.sublime-settings")

class ToggleVintageModeCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        vintage = ["Vintage"] if settings.get("ignored_packages", ["Vintage"]) != ["Vintage"] else []
        settings.set("ignored_packages", vintage)
        sublime.save_settings("Preferences.sublime-settings")

