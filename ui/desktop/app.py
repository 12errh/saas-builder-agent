from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

from core.orchestrator.state_machine import RunSession, RunState, StateStore


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ForgeFlow Agent Studio — Phase 0")
        self.resize(900, 600)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(QLabel("ForgeFlow desktop shell is running."))
        layout.addWidget(QLabel("State machine baseline initialized."))
        self.setCentralWidget(container)


def bootstrap_state() -> None:
    store = StateStore(Path("storage/run_session.json"))
    session = RunSession(run_id="phase0-local", state=RunState.PROJECT_INIT)
    store.save(session)


def main() -> int:
    bootstrap_state()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
