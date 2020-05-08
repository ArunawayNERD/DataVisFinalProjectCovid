from app import app
from callbacks import left_column
from callbacks import right_column

if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_silence_routes_logging=False)
