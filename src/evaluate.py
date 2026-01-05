from pathlib import Path
import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    roc_auc_score,
)

from .model import train_decision_tree
from .config import TARGET_COL

FIG_DIR = Path("figures")


def evaluate_decision_tree():
    """
    Train the decision tree and print evaluation metrics.
    Save confusion matrix plot as a PNG.
    """
    model, X_test, y_test = train_decision_tree()

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, y_prob)

    print("\n=== Decision Tree Evaluation ===")
    print(f"ROC-AUC: {auc:.3f}\n")
    print(classification_report(y_test, y_pred, digits=3))

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure()
    disp.plot(values_format="d")
    plt.title("Confusion Matrix — Decision Tree")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "confusion_matrix_decision_tree.png")
    plt.close()

    print("Saved:", FIG_DIR / "confusion_matrix_decision_tree.png")


if __name__ == "__main__":
    evaluate_decision_tree()
