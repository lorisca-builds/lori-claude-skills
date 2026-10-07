#!/usr/bin/env python3
"""
Execute a Jupyter notebook top-to-bottom in a completely fresh kernel and
report whether it ran clean. This is the automated version of the
"restart the runtime, run all" check that course materials
flag as the single most-penalized technical failure: a notebook that
only works because of a variable still sitting in memory from a cell
that was later edited or deleted. That failure is invisible on your own
screen and fatal the moment a grader (or Colab, or the user) opens a fresh
copy and runs it from the top.

Usage:
    python execute_notebook.py notebook.ipynb [notebook2.ipynb ...]

On success, the notebook is overwritten in place with the fresh outputs
baked in (charts, printed numbers, everything) so what ships is exactly
what was verified. On failure, the original file is left untouched and
the failing cell's index and error are printed so it can be fixed --
after fixing, re-run this script again on the WHOLE notebook, not just
the cell that failed, since a partial re-run can hide the exact kind of
stale-state problem this script exists to catch.

Exits 0 if every notebook passed, 1 if any notebook failed.
"""
import sys
import time

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


def run_one(path, timeout=600, kernel_name="python3"):
    nb = nbformat.read(path, as_version=4)
    t0 = time.time()
    try:
        NotebookClient(nb, timeout=timeout, kernel_name=kernel_name).execute()
    except CellExecutionError as e:
        print(f"[FAIL] {path}: execution stopped partway through -- {e}")
        return False

    errors = [
        (i, out)
        for i, cell in enumerate(nb.cells)
        if cell.cell_type == "code"
        for out in cell.get("outputs", [])
        if out.get("output_type") == "error"
    ]
    if errors:
        for i, out in errors:
            print(f"[FAIL] {path} cell {i}: {out.get('ename')}: {out.get('evalue')}")
        return False

    nbformat.write(nb, path)
    n_code = sum(1 for c in nb.cells if c.cell_type == "code")
    n_md = sum(1 for c in nb.cells if c.cell_type == "markdown")
    print(
        f"[OK] {path} -- {n_code} code cells, {n_md} markdown cells, "
        f"executed clean in {round(time.time() - t0, 1)}s"
    )
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python execute_notebook.py notebook.ipynb [notebook2.ipynb ...]")
        sys.exit(1)

    results = [run_one(path) for path in sys.argv[1:]]

    if not all(results):
        print(
            "\nOne or more notebooks failed a clean fresh-kernel run. "
            "Fix the failing cell (or an earlier cell it depends on) and "
            "re-run this script on the full notebook again before delivering."
        )
        sys.exit(1)

    sys.exit(0)
