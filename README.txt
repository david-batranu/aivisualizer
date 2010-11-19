The purpose of this script is to output a html file that will use the
GAI-Challenge game visualizer to view your offline games.

The script attempts to use `PlayGame-1.2.jar` if available in the 
`tools` folder, otherwise it will use the standard `PlayGame.jar`



Usage
-----

1. Copy the contents of this folder into the folder containing 
   your GAI-Challenge starter package.

2. Run it by issuing the following command 
   (the map argument is optional, defaults to map7.txt, maps are taken from ./maps)

    `python visualizer.py MyBotName.py YourBotName.jar map10.txt`

3. If all works well, you should find a file named `MyBotNamevsYourBotName.html`
   in the `visualizer` folder.


Currently, the only bot types the script supports are Python,
Java and compiled executables. This can be extended by editing
the `ftypes` variable on line 5 (notice the space at the end).

Java is presumed installed and in your PATH.
Developed and tested on Python 2.6.4 on Windows.

If you find anything wrong or it doesn't work for you, feel free to message me.

Have fun!
