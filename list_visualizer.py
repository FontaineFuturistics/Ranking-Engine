import tkinter as tk

list1 = [
    "Judas",
    "Critter Crosser",
    "Little Nightmares III",
    "Ark 2",
    "Lay of the Land",
    "Plunder",
    "Life is Strange: Double Exposure",
    "Besiege: The Splintered Sea",
    "The Last of Us Part II Remastered",
    "The Elder Scrolls IV: Oblivion Remastered",
    "Horizon Zero Dawn Remastered",
    "The Outer Worlds",
    "Warhammer 40k: Space Marine 2",
    "Factorio",
    "Blade and Sorcery",
    "Timberborn",
    "Far Cry Primal",
    "Void Crew",
    "Selaco",
    "BattleBit Remastered",
    "Sid Meier's Civilization VII",
    "The Walking Dead: Saints & Sinners",
    "Coromon",
    "Warhammer 40k: Boltgun",
    "Zombie Army 4: Dead War",
    "Foundation",
    "RailGods of Hysterra",
    "What Remains of Edith Finch",
    "Airborne Empire",
    "Clair Obscur: Expedition 33"
]
list2 = [
    "Ark 2", "Judas", "Critter Crosser", "Little Nightmares III", "Lay of the Land", "Plunder", 
    "The Outer Worlds", "Blade and Sorcery", "The Last of Us Part II Remastered", "Horizon Zero Dawn Remastered", 
    "Warhammer 40k: Space Marine 2", "The Elder Scrolls IV: Oblivion Remastered", "Factorio", 
    "Clair Obscur: Expedition 33", "Timberborn", "The Walking Dead: Saints & Sinners", 
    "Life is Strange: Double Exposure", "Far Cry Primal", "Selaco", "BattleBit Remastered", 
    "Coromon", "Void Crew", "Sid Meier's Civilization VII", "Besiege: The Splintered Sea", 
    "Zombie Army 4: Dead War", "What Remains of Edith Finch", "Warhammer 40k: Boltgun", 
    "Foundation", "RailGods of Hysterra", "Airborne Empire"
]

def visualize_shift(list1, list2):
    root = tk.Tk()
    root.title("List Shift Visualizer")

    canvas = tk.Canvas(root, width=800, height=800, bg="white")
    canvas.pack(padx=10, pady=10)

    y_gap = 20
    x1, x2 = 200, 600

    # Draw list1
    for i, item in enumerate(list1):
        y = 40 + i * y_gap
        canvas.create_text(x1, y, text=item, font=("Arial", 14), tags=f"l1_{item}")

    # Draw list2
    for i, item in enumerate(list2):
        y = 40 + i * y_gap
        canvas.create_text(x2, y, text=item, font=("Arial", 14), tags=f"l2_{item}")

    # Draw arrows
    for i, item in enumerate(list1):
        y1 = 40 + i * y_gap
        j = list2.index(item)
        y2 = 40 + j * y_gap
        canvas.create_line(x1 + 20, y1, x2 - 20, y2, arrow=tk.LAST, fill="blue", width=2)

    root.mainloop()

if __name__ == "__main__":
    visualize_shift(list1, list2)