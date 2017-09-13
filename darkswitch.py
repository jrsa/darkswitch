import sublime, sublime_plugin

PLUGIN_SETTINGS_FN = "darkswitch.sublime-settings"
USER_SETTINGS_FN = "Preferences.sublime-settings"

def plugin_settings():
  return sublime.load_settings(PLUGIN_SETTINGS_FN)

def user_settings():
  return sublime.load_settings(USER_SETTINGS_FN)


def flush_settings():
  sublime.save_settings(PLUGIN_SETTINGS_FN)
  sublime.save_settings(USER_SETTINGS_FN)

class DarkSwitchCommand(sublime_plugin.ApplicationCommand):
  def __init__(self):
    pass

  def run(self):
    if(user_settings().get("color_scheme") == plugin_settings().get("dark_color_scheme")):
      user_settings().set("color_scheme", plugin_settings().get("light_color_scheme"))
    elif(user_settings().get("color_scheme") == plugin_settings().get("light_color_scheme")):
      user_settings().set("color_scheme", plugin_settings().get("dark_color_scheme"))
    else:
      darkscheme = plugin_settings().get("dark_color_scheme")
      user_settings().set("color_scheme", darkscheme)


class SetDarkCommand(sublime_plugin.ApplicationCommand):
  def __init__(self):
    pass

  def run(self):
    current_color_scheme = user_settings().get("color_scheme")
    plugin_settings().set("dark_color_scheme", current_color_scheme)

class SetLightCommand(sublime_plugin.ApplicationCommand):
  def __init__(self):
    pass

  def run(self):
    current_color_scheme = user_settings().get("color_scheme")
    plugin_settings().set("light_color_scheme", current_color_scheme)
