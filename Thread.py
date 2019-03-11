from multiprocessing import Process

import os,time

def run_proc(name):

	print('Run child process %s (%s)...' % (name, os.getpid()))
	time.sleep(10)


if __name__=='__main__':

	print('Parent process %s.' % os.getpid())

	p = Process(target=run_proc, args=('test',))

	print('Child process will start.')

	p.start()


	print('Child process end.')