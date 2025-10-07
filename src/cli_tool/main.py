import argparse
from rich.console import Console

def cli():
    # Create a console object for rich printing
    console = Console()

    # Set up the argument parser
    parser = argparse.ArgumentParser(description="A simple CLI tool.")
    parser.add_argument(
        "--name",
        default="World",
        help="The name to greet."
    )
    args = parser.parse_args()

    # The main logic of your CLI
    console.print(f"\nHello, [bold magenta]{args.name}[/bold magenta]! :wave:")
    console.print("This is your CLI tool running directly from GitHub! :rocket:\n")

if __name__ == "__main__":
    cli()
