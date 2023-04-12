import csv

def chromosome_to_rgb(chromosome, palette_file):
    with open(palette_file, 'r') as file:
        reader = csv.reader(file)
        palette = [list(map(int, row)) for row in reader]

    r, g, b = 0, 0, 0
    for i in range(len(chromosome)):
        color = palette[chromosome[i]]
        r += color[0]
        g += color[1]
        b += color[2]

    r /= len(chromosome)
    g /= len(chromosome)
    b /= len(chromosome)

    return tuple(map(int, (r, g, b)))