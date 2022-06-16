import markdown
import typer

app = typer.Typer()

@app.command(help = "An markdown to html converter.")
def main(markdown_file: str = typer.Argument(..., help = "The markdown file you want to convert."), html_name_file: str = typer.Argument(..., help = "The name of the html file.")):
    with open(markdown_file, "r") as file:
        text = file.read()
        html = markdown.markdown(text)

    with open(html_name_file, "w") as file:
        file.write(html)

if __name__ == "__main__":
    app()