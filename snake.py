# codeing: utf-8

#module
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

#conste
HEIGHT = 22 
WIDTH = 42
GROUND = (HEIGHT-2) * (WIDTH-2)

#var
position_x = 1
position_y = 1

snake = [0] * (GROUND+1);
head = 1
tail = 3
#     2
#     |
#-1 -- -- 1
#     |
#    -2   
snake_direct = 1;

#function
def init_snake():
	i = 3;
	j = 1;
	while i > 0:
		snake[j]=i
		i = i - 1
		j = j + 1

	temp_head = head
	while temp_head != tail+1:
		position = map_into_ground(temp_head)
		win.addch(position[0],position[1],'o')
		temp_head = (temp_head + 1)%(WIDTH-1)

def map_into_ground(position):
	x = (position)%(WIDTH-2)
	if x == 0:
		x = 40
	y = (position-1)/(WIDTH-2)+1
	return [y,x]


def move_one_step():
	global head
	global tail
	if(snake_direct == 1):
		next_step = snake[head]+1;
		#check_next_step#################################################
		next_step = next_step % 41
		if(next_step == 0):
			next_step = 1
		head = (head-1+41)%41
		snake[head] = next_step
		win.addstr(0, 10, str(next_step))
		position = map_into_ground(next_step)
		win.addstr(0,0, str(position[0])+':'+str(position[1]))
		win.addch(position[0],position[1],'o')

		position = map_into_ground(snake[tail])
		win.addch(position[0],position[1],' ')
		tail = (tail-1+41)%41
		
	elif(snake_direct == -1):
		next_step = snake[head]-1;

		next_step = (next_step+41)%41 


	elif(snake_direct == 2):
		pass
	elif(snake_direct == -2):
		next_step = snake[head]+40
		#check_next_step 
		if(next_step > 800):
			next_step = next_step % 40 
		if(next_step == 0):
			next_step = 40
		head = (head-1+41)%41 
		snake[head] = next_step
		win.addstr(0,10, str(next_step)+'head:'+str(head))
		position = map_into_ground(next_step)
		win.addstr(0,0, str(position[0])+':'+str(position[1]))
		win.addch(position[0],position[1],'o')

		position = map_into_ground(snake[tail])
		win.addch(position[0],position[1],' ')
		tail = (tail-1+41)%41


def position_process(x):
	global snake_direct
	if(x == 2):
		if(snake_direct == -1 or snake_direct == 1):
			snake_direct = 2
	if(x == -2):
		if(snake_direct == -1 or snake_direct == 1):
			snake_direct = -2
	if(x == 1):
		if(snake_direct == -2 or snake_direct == 2):
			snake_direct == 1
	if(x == -1):
		if(snake_direct == -2 or snake_direct == 2):
			snake_direct == -1

#impletment switch-case process key up down left right
key_process = {
		KEY_UP: lambda : position_process(2),
		KEY_DOWN: lambda : position_process(-2),
		KEY_LEFT: lambda : position_process(-1),
		KEY_RIGHT: lambda : position_process(1)
		}


#main
curses.initscr()
curses.noecho()
curses.curs_set(0)
win = curses.newwin(HEIGHT, WIDTH, 0, 0)
win.keypad(1)
win.nodelay(1)
win.border(0)
count = 1

init_snake()

while 1:
#	win.addstr(0,0,'position_x:'+str(position_x)+'|'+'position_y:'+str(position_y))
	c = win.getch()
	win.timeout(200)
	if(c != -1):
		key_process[c]()
		move_one_step()
	else:
		move_one_step()
