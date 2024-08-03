import xml.etree.ElementTree as ET
from tkinter import messagebox
def apply_theme(theme, root, *args):
    root.config(bg=theme['bg'])
    if len(args) > 0 and args[0] is not None:
        label = args[0]
        label.config(bg=theme['bg'], fg=theme['fg'], font=theme['font'])
    if len(args) > 1 and args[1] is not None:
        buttons = args[1]
        for button in buttons:
            button.config(bg=theme['btn_bg'], fg=theme['btn_fg'], font=theme['font'])

def load_and_apply_theme(theme_name, root, *args):
    tree = ET.parse('themes.xml')
    xml_root = tree.getroot()

    for theme in xml_root.findall('Theme'):
        if theme.get('name') == theme_name:
            bg = theme.find('Background').text
            fg = theme.find('Foreground').text
            btn_bg = theme.find('ButtonBackground').text
            btn_fg = theme.find('ButtonForeground').text
            font_family = theme.find('FontFamily').text
            font_size = int(theme.find('FontSize').text)

            theme_settings = {
                'bg': bg,
                'fg': fg,
                'btn_bg': btn_bg,
                'btn_fg': btn_fg,
                'font': (font_family, font_size)
            }

            apply_theme(theme_settings, root, *args)
            return

def quit_programm(root):
    answer = messagebox.askokcancel(title='Выход', message='Закрыть программу')
    if answer:
        root.destroy()