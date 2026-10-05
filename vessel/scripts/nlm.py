#!/usr/bin/env python3
"""La CLI di NotebookLM con il tetto delle risposte alzato (evita «RPCResponseTooLargeError»).

Uso (stessi comandi di `notebooklm`):
    ~/.local/share/uv/tools/notebooklm-py/bin/python ~/.claude/skills/vessel/scripts/nlm.py ask -n ae39f678 "domanda"
Non usare `ask --new`: cancella la conversazione del notebook.
"""
import notebooklm._streaming_post as sp

sp.stream_post_with_size_cap.__kwdefaults__["max_bytes"] = 600 * 1024 * 1024

from notebooklm.notebooklm_cli import main  # noqa: E402

main()
