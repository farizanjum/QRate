from app import create_app
import sys

def main():
    try:
        app = create_app()
        return app
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

app = main()

if __name__ == "__main__":
    app.run(port=5000) 