
#include <stdio.h>
struct Emprunt {
    char nom[20];
    char emprunteur[20];
};

int main() {
    struct Emprunt e = {"IA", "Zoubirou"};
    printf("Nom: %s, Emprunteur: %s\n", e.nom, e.emprunteur);
    return 0;
}
