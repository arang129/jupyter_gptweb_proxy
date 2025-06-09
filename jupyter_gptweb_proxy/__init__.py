"""
Return config on servers to start web services from JupyterLab

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""

import os


def setup_gptweb_proxy():
    """
    Proxy wrapper to launch Streamlit from JupyterHub on Binder

    Note that a shell script that launches the actual Streamlit application is expected at
    /home/jovyan/run_streamlit.sh
    The script must accept additional command line flags being passed to streamlit, see below.
    """
    return {
        'command': [
            "streamlit", "run", "/home/jupyter-data/gpt/gpt.py",
            "--browser.gatherUsageStats", "false",
            "--browser.serverAddress", "0.0.0.0",
            "--server.port", "{port}",
            "--server.headless", "true",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false",
            "--server.maxUploadSize", "20",       # 限制檔案上傳大小 (MB)
            "--server.maxMessageSize", "200",     # 限制訊息大小 (MB)
        ],
        'environment': {},
        'timeout': 120.0,
        'launcher_entry': {
            'title': 'ChatAI',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'chatgpt.svg'),
        }
    }
