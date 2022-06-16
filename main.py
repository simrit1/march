import markdown
import typer

app = typer.Typer()

@app.command(help = "An markdown to html converter.")
def main(markdown_file: str = typer.Argument(..., help = "The markdown file you want to convert."), html_name_file: str = typer.Argument(..., help = "The name of the html file.")):
    with open(markdown_file, "r") as file: # get the markdown file
        text = file.read() # get the content of the markdown file
        html = markdown.markdown(text) # convert the markdown in html

    with open(html_name_file, "w") as file: # create the html file
        file.write(html) # write the html in the file

if __name__ == "__main__":
    app()
