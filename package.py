import sublime
import sublime_plugin


class ClerkSublimedShowCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print("Clerk evaluating \"" + self.view.file_name() + "\".")
    sublime.active_window().run_command("clojure_sublimed_eval_code", {"code": "(nextjournal.clerk/show! \"" + self.view.file_name() + "\")"})
