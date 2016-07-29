import subprocess
import psutil, time

start = 0

exit = False

timeout = 60 * 30 # 60 * minutos

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
		subp = subprocess.Popen([path+exe, folder], cwd=path)
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
			time.sleep(60)#Esperamos un minuto para relogear
			openProcs()
	time.sleep(5)
