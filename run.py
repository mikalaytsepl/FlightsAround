import sys
import os

# Add the project root to PYTHONPATH dynamically
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from view_controller.main import main  # Import main function from view_controller/main.py

if __name__ == "__main__":
    main()
