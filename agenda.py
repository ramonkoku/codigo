agenda_artistas = ["ArtistaA", "ArtistaB", "ArtistaC", "ArtistaD"]

artista_cancelado = "ArtistaA"
novo_artista = "NovoArtista"

indice_cancelado = agenda_artistas.index(artista_cancelado)

agenda_artistas.pop(indice_cancelado)

agenda_artistas.insert(indice_cancelado, novo_artista)

print(agenda_artistas)