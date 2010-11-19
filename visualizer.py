import sys
import os
import subprocess

ftypes = {
        'py': 'python ',
        'jar': 'java -jar ',
        'exe': '',
    }


def create_visualizer(fname):
    if not os.path.isdir('visualizer'):
        print 'Visualizer not present!'
        return
    
    template = open(os.path.join('visualizer', 'template.html'), 'rb')
    data = open(fname, 'rb')
    ttext = template.read()
    ttext = ttext.replace('$$$GAMELOG$$$', data.read().strip())
    ofname = '%s.html' % fname.split('.')[0]
    ofile = open(os.path.join('visualizer', ofname), 'wb')
    ofile.write(ttext)
    ofile.close()
    print 'Game visualization ready in %s' % ofname

def main(args):

    base_command = 'java -jar %(gameplayer)s %(gamemap)s 1000 1000 log.txt "%(player1)s" "%(player2)s"'

    def find_gameplayer():
        gameplayers = ['PlayGame-1.2.jar', 'PlayGame.jar']
        for gp in gameplayers:
            gppath = os.path.join('tools', gp)
            if os.path.isfile(gppath):
                return gppath

    def player_command(player):
        extension = player.split('.')[-1]
        return '%s%s' % (ftypes[extension], player)

    def map_path(gamemap):
        return os.path.join('maps', gamemap)

    def output_file(argp1, argp2):
        def clean_fname(f):
            return os.path.basename(f)
        return '%svs%s.log' % (clean_fname(argp1.split('.')[0]),
                               clean_fname(argp2.split('.')[0]))

    try:
        argp1 = args[0]
        argp2 = args[1]
    except IndexError:
        print 'Not enough players!'
        sys.exit(1)
    try:
        argmap = args[2]
    except IndexError:
        argmap = 'map7.txt'

    command = base_command % {'gameplayer': find_gameplayer(),
                               'gamemap': map_path(argmap),
                               'player1': player_command(argp1),
                               'player2': player_command(argp2),
                                }
    print 'Running:', command
    ofile = output_file(argp1, argp2)
    x = subprocess.call(command, stdout=open(ofile, 'wb'))
    print ofile
    if x != 0:
        print 'Some error has occured!'
        return
    create_visualizer(ofile)

if __name__ == "__main__":
    main(sys.argv[1:])
