import os
from PIL import Image

# Dossier contenant les images
dossier_cartes = "../CartesMinis"
dossier_sortie = "../Cartes_Minis_redimensionnees"  # Nouveau dossier pour les images redimensionnées

# Si le dossier de sortie n'existe pas, on le crée
if not os.path.exists(dossier_sortie):
    os.makedirs(dossier_sortie)

# Parcours chaque fichier du dossier
for filename in os.listdir(dossier_cartes):
    # On vérifie si c'est bien une image (par exemple .png)
    if filename.endswith(".png"):  
        # Chemin complet du fichier image
        chemin_image = os.path.join(dossier_cartes, filename)
        
        # Ouvre l'image
        img = Image.open(chemin_image)
        
        # Redimensionne l'image
        img_resized = img.resize((180, 150))  # Change ici la taille selon tes besoins
        
        # Sauvegarde l'image redimensionnée dans le dossier de sortie
        chemin_sortie = os.path.join(dossier_sortie, filename)
        img_resized.save(chemin_sortie)

        print(f"{filename} a été redimensionnée et sauvegardée dans {chemin_sortie}")
