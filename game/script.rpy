## Python definitions don't have to be done here, but it's convenient to have them all in one place
init python:
    import codecs
    import os
    import os.path
    import subprocess
    import sys
    import platform

    ## Dummy Displayable
    class DrawImage(renpy.Displayable):

        def __init__(self, child, opaque_distance, transparent_distance, **kwargs):
            super(DrawImage, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):
            t = Transform(child=self.child)
            child_render = renpy.render(t, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.blit(child_render, (0, 0))
            return render

    ## Basic file reader for logs. Can replace later.
    def loadtext(log_file):
        logtext = [ ]
        myfile = config.gamedir + '/' + log_file + '.txt'
        myfile = myfile.replace('\\','/')

        f = codecs.open(myfile, 'r', 'utf-8')
        for i in f:
            l = i.strip()
            logtext.append(l)
        f.close()

        return logtext
    ## Ditto for appending text.
    def addtext(log_file):
        myfile = config.gamedir + '/' + log_file + '.txt'
        file = open(myfile,"a")
        file.write("\nExporting...\nCharacter: [dropdown_1]\nCostume: [dropdown_2]")
        file.close()
    ## Generic File Movement taken from DSCS texture swapper.
    def filemovement(original_filename, new_filename):
        new_filename = config.basedir + "/" + new_filename
        dirname = os.path.dirname(new_filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        orig = renpy.file(original_filename)
        new = open(new_filename, "wb")

        from shutil import copyfileobj
        copyfileobj(orig, new)

        new.close()
        orig.close()
    ## Generic Explorer Instance taken from DSCS texture swapper.
    def openfolder():
        Exportfolder = os.path.abspath(os.path.join(config.basedir, "!Export"))

        if sys.platform == "win32":
            os.startfile(Exportfolder)
        elif platform.mac_ver()[0]:
            subprocess.Popen([ "open", Exportfolder ])
        else:
            subprocess.Popen([ "xdg-open", Exportfolder ])
    ## Dumb bodge, pls don't look
    def aNull():
        anull = []

    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False
################################################################################

## Text styling. Totally unimportant, but just in case...
define narrator = nvl_narrator
default dropdown_1 = "None"
default dropdown_2 = "None"

## For the Dummy Displayable to use
image dummy = Solid("#274372")

## Remove stock intro screen
label main_menu:
    return

## Game Start ###############
label start:
    window hide
    ## Call main UI (stored in screens.rpy) preventing progress in this file until returned from
    # Defaults to opening /log.txt for now, as seen in the "def loadtext" block above.
    call screen main_UI('log')

label exit:
    return
