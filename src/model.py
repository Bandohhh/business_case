from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_curve, roc_auc_score

from .load_data import load_dataset
from .config import TARGET_COL


FIG_DIR = Path("figures")


def train_decision_tree(random_state=42):
    """
    Train a Decision Tree classifier and return the fitted model and test data.
    """
    df = load_dataset()

    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    # One-hot encode categorical variables
    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=random_state, stratify=y
    )

    model = DecisionTreeClassifier(
        max_depth=5,
        random_state=random_state
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test


def plot_roc_curve(model, X_test, y_test):
    """
    Plot and save ROC curve.
    """
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    y_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    auc = roc_auc_score(y_test, y_prob)

    plt.figure()
    plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}")
    plt.plot([0, 1], [0, 1], linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve — Decision Tree")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "roc_curve_decision_tree.png")
    plt.close()

    print("Saved:", FIG_DIR / "roc_curve_decision_tree.png")


def plot_feature_importance(model, X_test, top_n=10):
    """
    Plot and save top feature importances.
    """
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    importances = model.feature_importances_
    feature_names = X_test.columns

    imp_df = (
        pd.DataFrame({"feature": feature_names, "importance": importances})
        .sort_values("importance", ascending=False)
        .head(top_n)
    )

    plt.figure()
    plt.barh(imp_df["feature"], imp_df["importance"])
    plt.xlabel("Importance")
    plt.title("Top Feature Importances — Decision Tree")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "feature_importance_decision_tree.png")
    plt.close()

    print("Saved:", FIG_DIR / "feature_importance_decision_tree.png")


if __name__ == "__main__":
    model, X_test, y_test = train_decision_tree()
    plot_roc_curve(model, X_test, y_test)
    plot_feature_importance(model, X_test)
