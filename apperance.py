import os, time

print(f"1: Install Themes\n2: Install Icons\n3: Install Mouse Theme\n4: Install Hyprland")
data_menu = int(input('Enter number: '))
gitTheme = 'git clone https://github.com/vinceliuice/Graphite-gtk-theme.git'
gitIcons = 'git clone https://github.com/vinceliuice/Tela-circle-icon-theme.git'
gitMouse = 'git clone https://github.com/alvatip/Nordzy-cursors.git'
done = None
readme = ['Благодарим за исползование этого скрипта\n' 'И ты умничка))\n']


try:
    if data_menu == 1:
        print("All files and folders: ", os.listdir())
        data_directory = input('Enter folder: ')
        os.chdir(data_directory)
        os.system('clear')
        print("Current directory: ", os.getcwd())
        if input('Install Theme? (y/n): ') == 'y':
            os.system(gitTheme)
            os.chdir('Graphite-gtk-theme')
            os.system('sudo ./install')

    elif data_menu == 2:
        print("All files and folders: ", os.listdir())
        data_directory = input('Enter folder: ')
        os.chdir(data_directory)
        os.system('clear')
        print("Current directory: ", os.getcwd())
        if input('Install Icons? (y/n): '):
            os.system(gitIcons)
            os.chdir('Tela-circle-icon-theme')
            os.system('sudo ./install -a')

    elif data_menu == 3:
        print("All files and folders: ", os.listdir())
        data_directory = input('Enter folder: ')
        os.chdir(data_directory)
        os.system('clear')
        print("Current directory: ", os.getcwd())
        if input('Install Mouse Theme? (y/n): '):
            os.system(gitMouse)
            os.chdir('Nordzy-cursors')
            os.system('sudo ./install')

    elif data_menu == 4:
        os.system('sudo pacman -Syu npm clang jq nerd-fonts hyprland hyprpaper waybar xorg-xwayland wofi neofetch mako wl-clipboard slurp grim nemo nemo-fileroller xdg-desktop-portal-hyprland polkit-gnome cmake ninja sddm bluez blueman gvfs gvfs-mtp telegram-desktop')

except FileNotFoundError:
    os.system('clear')
    print("Sorry(\nError: 404")

except ValueError:
    os.system('clear')
    print("Sorry(\nError: 400")

with open("Прочитай.txt", "w") as f:
    f.writelines(readme)
