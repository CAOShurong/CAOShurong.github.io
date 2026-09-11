"""Copy a validated Pages build into the registered static mirror checkout."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = "https://caoshurong.github.io"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    parser.add_argument("--origin", required=True)
    args = parser.parse_args()
    target = args.checkout.resolve()
    manifest = json.loads((target / ".openai/hosting.json").read_text())
    if manifest.get("static", {}).get("directory") != "out":
        raise SystemExit("Mirror must explicitly serve out/")
    if target == ROOT or ROOT in target.parents:
        raise SystemExit("Use a separate mirror checkout")
    origin = args.origin.rstrip("/")
    if not origin.startswith("https://"):
        raise SystemExit("Use the exact HTTPS origin returned by Sites")
    source = ROOT / "site"
    if not (source / "index.html").exists():
        raise SystemExit("Run build.py and scripts/check_site.py first")
    public = target / "out"
    # Preserve unrelated files. Review stale routes explicitly on future syncs.
    shutil.copytree(source, public, dirs_exist_ok=True)
    for path in public.rglob("*"):
        if path.is_file() and path.suffix in {".html", ".xml", ".txt"}:
            text = path.read_text(encoding="utf-8")
            if PRIMARY in text:
                path.write_text(text.replace(PRIMARY, origin), encoding="utf-8")
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    (target / "README.md").write_text(
        "# Shurong Cao academic website — public mirror\n\n"
        f"Primary: {PRIMARY}/\n\nMirror: {origin}/\n\n"
        f"Primary source commit: `{sha}`\n\n"
        "Static output copied from the validated primary website. Only absolute "
        "site-origin metadata is adapted; root-relative navigation and all public "
        "research content/assets are shared. Asset provenance and licenses are "
        "documented in the primary source repository. No private source documents "
        "or credentials belong here.\n\n"
        "To refresh: build and validate the primary checkout, run its "
        "`scripts/sync_mirror.py CHECKOUT --origin MIRROR_ORIGIN`, review the diff, "
        "commit/push this checkout, and publish with the Sites hosting workflow.\n",
        encoding="utf-8",
    )
    print(f"Synced {len(list(public.rglob('*')))} entries from primary {sha}")

if __name__ == "__main__":
    main()
