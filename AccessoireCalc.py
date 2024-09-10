from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import math
import tkinter as tk

# Base de données des panneaux (puissance: (longueur, largeur))
BASE_PANNEAUX = {
    550: (2.3, 1.13),
    400: (2.0, 1.1),
    300: (1.7, 1.0),
    # Ajoutez d'autres panneaux si nécessaire
}

# Prix des accessoires (à ajuster selon les prix réels)
PRIX_CLAMP_FIN = 7.50
PRIX_CLAMP_MILIEU = 7.50
PRIX_RAIL_PAR_METRE = 30.83  
PRIX_CONNEXION = 15
PRIX_ECROU_BOULON_2_60 = 1.25
PRIX_ECROU_BOULON_2_80 = 1.67
PRIX_BETON = 30  
PRIX_TIREFOND_BETON = 0.50
PRIX_CHEVILLE_DIAMETRE_10 = 0.16
PRIX_RONDELLE = 0.5
LONGUEUR_RAIL = 6

# Taux de TVA
TAUX_TVA = 0.2  # 20% de TVA

# Fonction pour formater les montants en type monétaire
def format_monetaire(montant):
    return f"{montant:.2f} DH"

# Fonction pour calculer les accessoires
def calcul_accessoires(nombre_panneaux, longueur_panneau, largeur_panneau):
    clamps_fin = 4
    clamps_milieu = (nombre_panneaux - 1) * 2
    
    nombre_de_pieds = math.ceil((nombre_panneaux * largeur_panneau) / 1.5)
    longueur_totale_rails_horizontal = nombre_panneaux * largeur_panneau * 2
    longueur_rail_de_pieds = nombre_de_pieds * 0.3
    longueur_totale_rails_vertical = longueur_panneau * nombre_de_pieds
    
    connexions_jumelage = math.ceil(3 * nombre_de_pieds)
    boulon_2_60 = math.ceil(8 * nombre_de_pieds)
    boulon_2_80 = math.ceil(2 * nombre_de_pieds)
    nombre_betons = math.ceil(2 * (nombre_de_pieds))
    longueur_totale_rails = longueur_totale_rails_horizontal + longueur_totale_rails_vertical + longueur_rail_de_pieds
    
    tirefond_beton = 2 * nombre_de_pieds
    cheville_diametre_10 = 2 * nombre_de_pieds
    rondelle = 2 * boulon_2_60

    nombre_rails = math.ceil(longueur_totale_rails / LONGUEUR_RAIL)

    cout_clamps_fin_HT = clamps_fin * PRIX_CLAMP_FIN
    cout_clamps_milieu_HT = clamps_milieu * PRIX_CLAMP_MILIEU
    cout_rails_HT = nombre_rails * PRIX_RAIL_PAR_METRE
    cout_connexions_HT = connexions_jumelage * PRIX_CONNEXION
    cout_ecrous_boulons_60_HT = boulon_2_60 * PRIX_ECROU_BOULON_2_60
    cout_ecrous_boulons_80_HT = boulon_2_80 * PRIX_ECROU_BOULON_2_80
    cout_beton_HT = nombre_betons * PRIX_BETON
    cout_tirefond_beton_HT = tirefond_beton * PRIX_TIREFOND_BETON
    cout_cheville_diametre_10_HT = cheville_diametre_10 * PRIX_CHEVILLE_DIAMETRE_10
    cout_rondelle_HT = rondelle * PRIX_RONDELLE
    
    cout_total_HT = (
        cout_clamps_fin_HT + 
        cout_clamps_milieu_HT +
        cout_rails_HT +
        cout_connexions_HT +
        cout_ecrous_boulons_60_HT +
        cout_ecrous_boulons_80_HT +
        cout_beton_HT +
        cout_tirefond_beton_HT +
        cout_cheville_diametre_10_HT +
        cout_rondelle_HT
    )
    
    cout_total_TTC = cout_total_HT * (1 + TAUX_TVA)

    accessoires = {
        "clamps_fin": clamps_fin,
        "clamps_milieu": clamps_milieu,
        "nombre_rails": nombre_rails,
        "connexions_jumelage": connexions_jumelage,
        "boulon_2_60": boulon_2_60,
        "boulon_2_80": boulon_2_80,
        "nombre_betons": nombre_betons,
        "tirefond_beton": tirefond_beton,
        "cheville_diametre_10": cheville_diametre_10,
        "rondelle": rondelle,
        "cout_clamps_fin_HT": format_monetaire(round(cout_clamps_fin_HT, 2)),
        "cout_clamps_milieu_HT": format_monetaire(round(cout_clamps_milieu_HT, 2)),
        "cout_rails_HT": format_monetaire(round(cout_rails_HT, 2)),
        "cout_connexions_HT": format_monetaire(round(cout_connexions_HT, 2)),
        "cout_ecrous_boulons_60_HT": format_monetaire(round(cout_ecrous_boulons_60_HT, 2)),
        "cout_ecrous_boulons_80_HT": format_monetaire(round(cout_ecrous_boulons_80_HT, 2)),
        "cout_beton_HT": format_monetaire(round(cout_beton_HT, 2)),
        "cout_tirefond_beton_HT": format_monetaire(round(cout_tirefond_beton_HT, 2)),
        "cout_cheville_diametre_10_HT": format_monetaire(round(cout_cheville_diametre_10_HT, 2)),
        "cout_rondelle_HT": format_monetaire(round(cout_rondelle_HT, 2)),
        "cout_total_HT": format_monetaire(round(cout_total_HT, 2)),
        "cout_total_TTC": format_monetaire(round(cout_total_TTC, 2))
    }

    return accessoires

# Fonction pour générer le PDF
def generer_pdf(nombre_panneaux, longueur_panneau, largeur_panneau, accessoires):
    nom_fichier = "rapport_accessoires.pdf"
    document = SimpleDocTemplate(nom_fichier, pagesize=A4)
    elements = []
    
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        'CustomStyle',
        parent=styles['Title'],
        textColor=colors.HexColor('#000080'),
        alignment=TA_CENTER
    )
    titre = Paragraph(f"Rapport d'accessoires pour <font color='red'>{nombre_panneaux}</font> panneaux solaires", custom_style)
    
   
    
   
   
    elements.append(Spacer(1, 20))
    
    elements.append(titre)
    elements.append(Spacer(1, 24))

    note = Paragraph("* Merci de vérifier les PRIX des accessoires", styles['Normal'])
    elements.append(note)
    elements.append(Spacer(1, 12))
    
    data = [
        ["Type d'Accessoire", "Quantité", "Prix Unitaire HT (DH)", "Prix Total HT (DH)", "Prix Total TTC (DH)"],
        ["Clamp End", accessoires['clamps_fin'], format_monetaire(PRIX_CLAMP_FIN), accessoires['cout_clamps_fin_HT'], format_monetaire(round(float(accessoires['cout_clamps_fin_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        ["Clamp Middle", accessoires['clamps_milieu'], format_monetaire(PRIX_CLAMP_MILIEU), accessoires['cout_clamps_milieu_HT'], format_monetaire(round(float(accessoires['cout_clamps_milieu_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
                ["Nombre de rails de 6 mètres", accessoires['nombre_rails'], format_monetaire(PRIX_RAIL_PAR_METRE), accessoires['cout_rails_HT'], format_monetaire(round(float(accessoires['cout_rails_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        ["Connexions Jumelage", accessoires['connexions_jumelage'], format_monetaire(PRIX_CONNEXION), accessoires['cout_connexions_HT'], format_monetaire(round(float(accessoires['cout_connexions_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        ["Écrou Boulon 2 * 60", accessoires['boulon_2_60'], format_monetaire(PRIX_ECROU_BOULON_2_60), accessoires['cout_ecrous_boulons_60_HT'], format_monetaire(round(float(accessoires['cout_ecrous_boulons_60_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        ["Écrou Boulon 2 * 80", accessoires['boulon_2_80'], format_monetaire(PRIX_ECROU_BOULON_2_80), accessoires['cout_ecrous_boulons_80_HT'], format_monetaire(round(float(accessoires['cout_ecrous_boulons_80_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        ["Beton", accessoires['nombre_betons'], format_monetaire(PRIX_BETON), accessoires['cout_beton_HT'], format_monetaire(round(float(accessoires['cout_beton_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        ["Tirefond Beton", accessoires['tirefond_beton'], format_monetaire(PRIX_TIREFOND_BETON), accessoires['cout_tirefond_beton_HT'], format_monetaire(round(float(accessoires['cout_tirefond_beton_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        ["Cheville Diamètre 10", accessoires['cheville_diametre_10'], format_monetaire(PRIX_CHEVILLE_DIAMETRE_10), accessoires['cout_cheville_diametre_10_HT'], format_monetaire(round(float(accessoires['cout_cheville_diametre_10_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        ["Rondelle", accessoires['rondelle'], format_monetaire(PRIX_RONDELLE), accessoires['cout_rondelle_HT'], format_monetaire(round(float(accessoires['cout_rondelle_HT'].replace(' DH', '')) * (1 + TAUX_TVA), 2))],
        
        ["Total", "", "", accessoires['cout_total_HT'], accessoires['cout_total_TTC']]
    ]

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E4E4E4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SPAN', (-4, -1), (-2, -1)),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ]))

    elements.append(table)
    document.build(elements)



    import tkinter as tk
from tkinter import messagebox

def interface():
    root = tk.Tk()
    root.title("Calcul des accessoires pour panneaux solaires")
    root.geometry("400x250")
    root.configure(bg='#f0f0f0')

    # Style des labels et des entrées
    label_style = {'font': ('Helvetica', 12), 'bg': '#f0f0f0', 'padx': 10, 'pady': 5}
    entry_style = {'font': ('Helvetica', 12), 'bg': '#ffffff', 'bd': 2, 'relief': 'flat'}

    # Ajout de frames pour organiser les éléments
    frame1 = tk.Frame(root, bg='#f0f0f0')
    frame1.pack(pady=20)

    frame2 = tk.Frame(root, bg='#f0f0f0')
    frame2.pack(pady=10)

    # Labels
    tk.Label(frame1, text="Nombre de panneaux:", **label_style).grid(row=0, column=0, sticky='w')
    tk.Label(frame1, text="Puissance du panneau (en W):", **label_style).grid(row=1, column=0, sticky='w')

    # Entries
    entry_nombre_panneaux = tk.Entry(frame1, **entry_style)
    entry_puissance_panneau = tk.Entry(frame1, **entry_style)

    entry_nombre_panneaux.grid(row=0, column=1, padx=10)
    entry_puissance_panneau.grid(row=1, column=1, padx=10)



    def generer():
        try:
            nombre_panneaux = int(entry_nombre_panneaux.get())
            puissance_panneau = int(entry_puissance_panneau.get())

            if puissance_panneau in BASE_PANNEAUX:
                longueur_panneau, largeur_panneau = BASE_PANNEAUX[puissance_panneau]
                accessoires = calcul_accessoires(nombre_panneaux, longueur_panneau, largeur_panneau)
                generer_pdf(nombre_panneaux, longueur_panneau, largeur_panneau, accessoires)
                messagebox.showinfo("Succès", "Le PDF a été généré avec succès.")
            else:
                messagebox.showerror("Erreur", "La puissance du panneau n'est pas dans la base de données.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    # Bouton
    bouton_generer = tk.Button(frame2, text='Générer le PDF', command=generer, font=('Helvetica', 12, 'bold'), bg='#4CAF50', fg='#ffffff', relief='flat', padx=10, pady=5)
    bouton_generer.pack()

    root.mainloop()

# Appel de la fonction pour afficher l'interface
interface()
