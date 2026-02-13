import importlib.metadata
import random

try:
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
except ImportError:
    pd = None
    plt = None


def check_dependencies() -> bool:
    packages = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }
    missing = []

    print("Checking Dependencies:")
    for package, description in packages.items():
        try:
            version = importlib.metadata.version(package)
            print(f"[OK] {package} ({version}) - {description}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[ERROR] {package:<12} | NOT INSTALLED")
            missing.append(package)

    if missing:
        print("\n[!] Alerte : Des packages manquent à l'appel.")
        print("Installe-les avec : pip install -r requirements.txt "
              "/ poetry install\n")
        return False

    print("\nTout est prêt. Connexion à la Matrice établie.\n")
    return True


def analyze_data() -> None:
    if pd is None or plt is None:
        return

    print("Analyzing Matrix data...")

    # Création de données factices (1000 points)
    data = {
        'index': range(1000),
        'value': [random.gauss(0, 1) + (i * 0.01) for i in range(1000)]
    }
    df = pd.DataFrame(data)

    print(f"Processing {len(df)} data points...")

    # Génération du graphique
    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.plot(df['index'], df['value'], color='green', alpha=0.8)
    plt.title('Matrix Data Analysis')
    plt.xlabel('Time (s)')
    plt.ylabel('Signal Strength')
    plt.grid(True, alpha=0.3)

    filename = "matrix_analysis.png"
    plt.savefig(filename)
    plt.close()  # Ferme la figure pour libérer la mémoire

    print("\nAnalysis complete!")
    print(f"Results saved to: {filename}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    if check_dependencies():
        if pd is None or plt is None:
            print("[ERROR] Une ou plusieurs bibliothèques essentielles "
                  "n'ont pas pu être importées.")
            return

        analyze_data()


if __name__ == "__main__":
    main()
