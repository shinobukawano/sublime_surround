import sublime_plugin


class SublimeSurroundCommand(sublime_plugin.TextCommand):

    def on_done(self, word):

        for region in self.view.sel():

            if not region.empty():

                # Get the selected text
                s = self.view.substr(region)

                # Surround word by input word
                surroundStr = word + s + word

                # Replace the selection with transformed text
                self.view.replace(self.edit, region, surroundStr)

    def run(self, edit):

        self.edit = edit

        # Show input panel for surround word, then handling input
        self.view.window().show_input_panel('Surrond Word: ', '',
            self.on_done, None, None)
