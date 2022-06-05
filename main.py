import markdown
import typer

app = typer.Typer()

@app.command()
def main(markdown_file: str, html_name_file):
    with open(markdown_file, "r") as file:
        text = file.read()
        html = markdown.markdown(text)

    with open(html_name_file, "w") as file:
        file.write(html)

if __name__ == "__main__":
    app()