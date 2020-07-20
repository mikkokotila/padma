from app import app

if __name__ == "__main__":
    # Added host, port and debug, but I think only host is actually required (if default port is 5000 ?)
    app.run(host='0.0.0.0', port=5000)
