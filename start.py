import os
import sys
from voila.app import Voila
from voila.config import VoilaConfiguration

if __name__ == "__main__":
    # Get the port from Render's environment variable, default to 10000
    port = int(os.environ.get("PORT", 10000))

    # Configure Voilà to bind to all interfaces
    config = VoilaConfiguration()
    config.ip = "0.0.0.0"  # This is the critical fix
    config.port = port
    config.no_browser = True

    # Point to your notebook
    notebook = "prediction.ipynb"

    # Start the Voilà server
    Voila().start(notebook, config=config)