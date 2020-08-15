import nubepalabras
import stack_usertags

while True:
    userid = input("Ingrese el id del usuario de stackoverflow para generar una nube de palabras con los tags mas usados o ingrese f para salir: ")

    if userid == "f":
        break

    tags = stack_usertags.obtener_tags(userid)

    if tags == None:
        print("Error al ingresar el id")
    else:
        nubepalabras.generar_imagen(tags, "Img/cloud_mask.png")

    

