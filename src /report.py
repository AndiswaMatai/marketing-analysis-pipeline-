"""
Generates a chart and a short markdown report from the campaign summary —
a lightweight, dependency-free stand-in for the automated Power BI
dashboards this mirrors, so the output is something you can actually look
at without opening Power BI Desktop.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

PROCESSED = Path(__file__).resolve().parent.parent / "data" / "processed"


def make_chart(summary: pd.DataFrame, out_path: Path):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    axes[0].barh(summary["campaign_name"], summary["roas"], color="#2E75B6")
    axes[0].set_xlabel("ROAS (revenue / spend)")
    axes[0].set_title("Return on Ad Spend by Campaign")
    axes[0].invert_yaxis()

    axes[1].barh(summary["campaign_name"], summary["cpa"], color="#E8A33D")
    axes[1].set_xlabel("Cost per Acquisition (ZAR)")
    axes[1].set_title("CPA by Campaign")
    axes[1].invert_yaxis()

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def make_markdown_report(summary: pd.DataFrame, out_path: Path):
    best_roas = summary.loc[summary["roas"].idxmax()]
    worst_cpa = summary.loc[summary["cpa"].idxmax()]

    lines = [
        "# Campaign Performance Report",
        "",
        f"Best ROAS: **{best_roas['campaign_name']}** at {best_roas['roas']}x return on spend.",
        f"Highest CPA (needs attention): **{worst_cpa['campaign_name']}** at R{worst_cpa['cpa']} per acquisition.",
        "",
        "## Campaign Summary",
        "",
        summary[["campaign_name", "cost", "revenue", "roas", "cpa", "churn_rate"]].to_markdown(index=False),
        "",
        "![Campaign performance chart](campaign_performance.png)",
    ]
    out_path.write_text("\n".join(lines))


def run():
    summary = pd.read_csv(PROCESSED / "campaign_summary.csv")
    make_chart(summary, PROCESSED / "campaign_performance.png")
    make_markdown_report(summary, PROCESSED / "report.md")
    print(f"Wrote {PROCESSED / 'campaign_performance.png'} and {PROCESSED / 'report.md'}")


if __name__ == "__main__":
    run()
