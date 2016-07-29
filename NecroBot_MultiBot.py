import subprocess
import psutil, time

start = 0

exit = False

timeout = 60 * 30 # 60 * minutos
waiting = 60 * 1 # 60 * minutos

sameconsole = False # All bots on same console

path = "D:\PokemonGO\GrindingConfig"
exe = "\NecroBot.exe"
folders = ["Legit",
	"Grinder",
	"Grinder2",
	"Grinder3",
	"Grinder4",
	"Grinder5",
	"Grinder6"
	]
procs = []

def openProcs():
	global procs
	procs[:] = []
	global start
	start = time.time()
	for folder in folders:
		if sameconsole:
			subp = subprocess.Popen([path+exe, folder], cwd=path)
		else:
			subp = subprocess.Popen([path+exe, folder], cwd=path, creationflags = subprocess.CREATE_NEW_CONSOLE)
		p = psutil.Process(subp.pid)
		procs.append(p)
			
openProcs()
while not exit:
	if (time.time() - start) > timeout:
		for proc in procs:
			proc.kill()
		#exit = True
		#Arriba comentado = reinicia los procesos cuando el timer acabe
		if not exit:
			print "[Bot Manager] Un minuto para relogear los Bots."
			time.sleep(waiting)#Esperamos un minuto para relogear
			openProcs()
	time.sleep(5)
