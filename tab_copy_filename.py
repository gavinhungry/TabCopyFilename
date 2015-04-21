import sublime, sublime_plugin, os

class TabCopyFilenameCommand(sublime_plugin.TextCommand):
  def run(self, edit, group=-1, index=-1):
    window = self.view.window()
    group_index, view_index = window.get_view_index(self.view)

    sheets = window.sheets_in_group(group)
    sheet = sheets[index]
    view = sheet.view()

    path = view.file_name()
    filename = os.path.basename(path)
    sublime.set_clipboard(filename)
