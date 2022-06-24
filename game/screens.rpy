################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Stock UI Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



## Main UI #####################################################################
## Basically just solid colours, tables, bars, images, etc... "displayables" that can be tied to python functions.
## The language for arguments is a bit inconsistent and won't always seamlessly transfer across similar types of displayables. It's a bit dumb.

screen main_UI(log_file):

    tag menu
    zorder 99
    key "update" action Function(aNull, _update_screens=True) # r = screen update

    ## Placeholders UI Blocks #####
    ##                            #
    ## Background                 #
    add Solid("#25292c")
    ## End ########################

    ## Leftside Displayable       #
    add DrawImage("dummy", 100, 50):
        xpos 0
        ypos 51
        xsize 1153
        ysize 918
    vbox:
        pos (0.25, 0.5)
        text "Render"
    ## End ########################

    ## Rightside Menu             #
    add Solid("#274372",  xpos=1158, ypos=51, xsize=762, ysize=1029)
    ## End ########################

    ## Log Box                    #
    $ logtext = loadtext(log_file)
    add Solid("#ddd",  xpos=0, ypos=969, xsize=1153, ysize=111)
    hbox:
        pos (0, 969)
        maximum (1153, 111)
        box_wrap True
        viewport:
            draggable True
            scrollbars "vertical"
            mousewheel True

            has vbox

            for i in logtext:
                text i color "000" size 20 xysize (1153, 111) rest_indent 35

    ## End ########################

    ## Top Bar                    #
    add Solid("#2ba6ff",  xpos=0, ypos=0, xsize=1920, ysize=50)
    frame:
        pos (1240, 3)
        padding (16, 2)
        textbutton "Export" text_size 22 text_ypos 0.5:
            action Confirm('Export?', yes=Function(addtext, log_file, _update_screens=True), no=None, confirm_selected=False)

    use dropdown1
    use dropdown2
    ## End ########################

################################################################################
## Character dropdown bar ######################################################
##
screen dropdown1():    ##screen dropdown1(dropdown1_list):
    frame:
        pos (40, 3)
        padding (16, 2)
        hbox:
            text "Character: " size 20 color "000" ypos 0.2
            # This is the button that is clicked to enable the dropdown,
            textbutton "[dropdown_1] ▼" text_size 22 text_ypos 0.5:

                # This action captures the focus rectangle, and in doing so,
                # displays the dropdown.
                action CaptureFocus("diff_drop"), Function(aNull, _update_screens=True)

    # All sorts of other screen elements could be here, but the nearrect needs
    # be at the top level, and the last thing show, apart from its child.

    # Only if the focus has been captured, display the dropdown.
    # You could also use showif instead of basic if
    if GetFocusRect("diff_drop"):

        # If the player clicks outside the frame, dismiss the dropdown.
        # The ClearFocus action dismisses this dropdown.
        dismiss action ClearFocus("diff_drop"), Function(aNull, _update_screens=True)

        # This positions the displayable near (usually under) the button above.
        nearrect:
            focus "diff_drop"

            # Finally, this frame contains the choices in the dropdown, with
            # each using ClearFocus to dismiss the dropdown.
            frame:
                modal True

                has vbox

                textbutton "Option 1" action [ SetVariable("dropdown_1", "Option 1"), ClearFocus("diff_drop"), Function(aNull, _update_screens=True) ] text_size 22
                textbutton "Option 2" action [ SetVariable("dropdown_1", "Option 2"), ClearFocus("diff_drop"), Function(aNull, _update_screens=True) ] text_size 22
                textbutton "Option 3" action [ SetVariable("dropdown_1", "Option 3"), ClearFocus("diff_drop"), Function(aNull, _update_screens=True) ] text_size 22
                textbutton "Option 4" action [ SetVariable("dropdown_1", "Option 4"), ClearFocus("diff_drop"), Function(aNull, _update_screens=True) ] text_size 22

## Costume dropdown bar ######################################################
##
screen dropdown2():    ##screen dropdown2(dropdown2_list):
    frame:
        pos (640, 3)
        padding (16, 2)
        hbox:
            text "Costume: " size 20 color "000" ypos 0.2
            # This is the button that is clicked to enable the dropdown,
            textbutton "[dropdown_2] ▼" text_size 22 text_ypos 0.5:

                # This action captures the focus rectangle, and in doing so,
                # displays the dropdown.
                action CaptureFocus("diff_drop2"), Function(aNull, _update_screens=True)

    # All sorts of other screen elements could be here, but the nearrect needs
    # be at the top level, and the last thing show, apart from its child.

    # Only if the focus has been captured, display the dropdown.
    # You could also use showif instead of basic if
    if GetFocusRect("diff_drop2"):

        # If the player clicks outside the frame, dismiss the dropdown.
        # The ClearFocus action dismisses this dropdown.
        dismiss action ClearFocus("diff_drop2"), Function(aNull, _update_screens=True)

        # This positions the displayable near (usually under) the button above.
        nearrect:
            focus "diff_drop2"

            # Finally, this frame contains the choices in the dropdown, with
            # each using ClearFocus to dismiss the dropdown.
            frame:
                modal True

                has vbox

                textbutton "Outfit 1" action [ SetVariable("dropdown_2", "Outfit 1"), ClearFocus("diff_drop2"), Function(aNull, _update_screens=True) ] text_size 22
                textbutton "Outfit 2" action [ SetVariable("dropdown_2", "Outfit 2"), ClearFocus("diff_drop2"), Function(aNull, _update_screens=True) ] text_size 22
                textbutton "Outfit 3" action [ SetVariable("dropdown_2", "Outfit 3"), ClearFocus("diff_drop2"), Function(aNull, _update_screens=True) ] text_size 22
                textbutton "Outfit 4" action [ SetVariable("dropdown_2", "Outfit 4"), ClearFocus("diff_drop2"), Function(aNull, _update_screens=True) ] text_size 22

## Default (trimmed) Ren'Py Stuff Below ########################################
##
##
##
##
##
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
