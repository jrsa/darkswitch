import sublime, sublime_plugin

PLUGIN_SETTINGS_FN = "darkswitch.sublime-settings"
USER_SETTINGS_FN = "Preferences.sublime-settings"
PLAINTASKS_SETTINGS_FN = "PlainTasks.sublime-settings"

def plugin_settings():
  return sublime.load_settings(PLUGIN_SETTINGS_FN)

def user_settings():
  return sublime.load_settings(USER_SETTINGS_FN)

def pt_settings():
  return sublime.load_settings(PLAINTASKS_SETTINGS_FN)


def flush_settings():
  sublime.save_settings(PLUGIN_SETTINGS_FN)
  sublime.save_settings(USER_SETTINGS_FN)
  sublime.save_settings(PLAINTASKS_SETTINGS_FN)

class DarkSwitchCommand(sublime_plugin.ApplicationCommand):
  def __init__(self):
    pass

  def run(self):
    if(user_settings().get("theme") == plugin_settings().get("dark_theme")):
      user_settings().set("theme", plugin_settings().get("light_theme"))
      user_settings().set("color_scheme", plugin_settings().get("light_color_scheme"))
      pt_settings().set("color_scheme", plugin_settings().get("pt_light_color_scheme"))

    elif(user_settings().get("theme") == plugin_settings().get("light_theme")):
      user_settings().set("theme", plugin_settings().get("dark_theme"))
      user_settings().set("color_scheme", plugin_settings().get("dark_color_scheme"))
      pt_settings().set("color_scheme", plugin_settings().get("pt_dark_color_scheme"))

    else:
      print("darkswitch: plugin settings do not exist")

  flush_settings()

