#OJO, antes hay que meter los idiomas, vamos al venv, a la carpeta scripts, y ejecutamos un cmd y escribimos

#Download resource
#YOU must run this as admin
import subprocess
subprocess.run(["python", "-m", "snips_nlu", "download", "es"])

#----
import io
import json

#Load   with io.open("trainingDatasets/multiple.json") as f:
with io.open("trainingDatasets/multiple.json") as f:
    sample_dataset = json.load(f)

#Train
from snips_nlu import SnipsNLUEngine
nlu_engine = SnipsNLUEngine()
print(sample_dataset)
nlu_engine.fit(sample_dataset)

#Test
import json

parsing = nlu_engine.parse("Creame una máquina virtual con seis cores y 3 gigas de ram en Europa")
print(json.dumps(parsing, indent=2))
print("---------------------")

parsing = nlu_engine.parse("Dame de alta un data lake en Asia")
print(json.dumps(parsing, indent=2))
