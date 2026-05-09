from __future__ import annotations

import sys
from pathlib import Path

<<<<<<< codex/develop-coding-agent-for-app-creation-s7kay5
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

from core.orchestrator.state_machine import RunSession, RunState, StateStore
from ui.desktop.phase_gate import can_enable_phase_button
=======
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

from core.orchestrator.state_machine import RunSession, RunState, StateStore
>>>>>>> main


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ForgeFlow Agent Studio — Phase 0")
        self.resize(900, 600)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(QLabel("ForgeFlow desktop shell is running."))
        layout.addWidget(QLabel("State machine baseline initialized."))
<<<<<<< codex/develop-coding-agent-for-app-creation-s7kay5

        phase3_enabled = can_enable_phase_button(Path("storage/tasks.json"), "phase3")
        phase3_button = QPushButton("Start Phase 3")
        phase3_button.setEnabled(phase3_enabled)
        status = "enabled" if phase3_enabled else "blocked until prior phases complete"

        layout.addWidget(QLabel(f"Phase 3 gate status: {status}"))
        layout.addWidget(phase3_button)
=======
>>>>>>> main
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
