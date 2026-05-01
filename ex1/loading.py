import matplotlib.pyplot as plt  # type: ignore
import importlib.metadata as md
import numpy as np
import sys


def matrix_gen() -> None:
    try:
        import pandas as pd  # type: ignore
    except ModuleNotFoundError:
        pd = None
    matrix = np.random.randn(1000, 3)
    labels = np.random.randint(0, 4, 1000)
    d = pd.DataFrame(matrix, columns=["f_1", "f_2", "f_3"])
    d["label"] = labels
    plt.figure(figsize=(10, 6))
    for label in d["label"].unique():
        subset = d[d["label"] == label]
        plt.scatter(subset["f_1"], subset["f_2"], label=f"Class {label}")
    plt.title("data analysis")
    plt.xlabel("f_1")
    plt.ylabel("f_2")
    plt.savefig("matrix_analysis.png", dpi=200)


def check_dependencies(packages:
                       list[str]) -> tuple[dict[str, str], list[str]]:
    there = {}
    missing = []

    for p in packages:
        try:
            version = md.version(p)
            key = p
            there[key] = version
        except md.PackageNotFoundError:
            missing.append(p)
    return there, missing


def main() -> None:
    packages = [
        "numpy",
        "pandas",
        "matplotlib",
        "requests"
    ]
    there, missing = check_dependencies(packages)
    print("LOADING STATUS: loading programs...\n")
    print("checking dependencies:")
    if len(missing) > 0:
        print("\nERROR: Missing dependency")
        print(f"the missing suspect is: {missing}")
        print("you have 2 options")
        print()
        print("1. pip install -r requirements.txt")
        print("2. poetry install")
        print("   poetry run python loading.py")
        if sys.prefix == sys.base_prefix:
            print("\nyou are still pluged in")
            print("go into isolatet environment!")
    else:
        for key, value in there.items():
            print(f"[OK] {key}({value})", end="")
            if key == "pandas":
                print(" - Data manipulation ready")
            elif key == "numpy":
                print(" - Numerical computation ready")
            elif key == "requests":
                print(" - Network acces ready")
            elif key == "matplotlib":
                print(" - Visualization ready")
        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        print("generating visualization...")
        print()
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
        matrix_gen()


if __name__ == "__main__":
    main()
