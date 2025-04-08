# 🔎 Port Scanner TCP - Python (Version Simple & Multithreadée)

Un projet de cybersécurité pédagogique qui présente deux versions d’un **scanner de ports TCP** en Python :  
✅ Une version **de base (mono-thread)** pour comprendre les fondamentaux --> scanner.py

⚡ Une version **optimisée (multithreadée)** pour gagner en vitesse et monter en compétence --> scanner_multi.py

---

## 🎯 Objectif du projet

Ce projet a pour but de :
- Comprendre comment fonctionnent les **ports et services réseau**
- Apprendre à utiliser les **sockets TCP en Python**
- Reproduire une étape essentielle de la reconnaissance dans un **pentest**
- Comparer les performances entre **traitement séquentiel** et **parallélisation (multithreading)**

---

## 🛠️ Fonctionnalités

| Fonction                            | Version simple | Version multithreadée |
|-------------------------------------|----------------|------------------------|
| Scan de ports TCP                   | ✅              | ✅                      |
| Résolution d’adresse IP (DNS)       | ✅              | ✅                      |
| Plage personnalisable (dans le code)| ✅              | ✅                      |
| Affichage des ports ouverts         | ✅              | ✅                      |
| Scan rapide (grâce au parallélisme) | ❌              | ✅                      |
| Gestion des erreurs réseau          | ✅              | ✅                      |

---

