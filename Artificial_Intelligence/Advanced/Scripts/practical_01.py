# Experiment No.1 - Advanced Expert Rule-Based System (Script Version)

try:
    from rich.console import Console 
    from rich.table import Table
    import graphviz
except ImportError:
    print("Please Install Dependencies using 'pip install -r requirements.txt'")
    exit()

console = Console()

def career_advisor(stream: str) -> str:

    stream = stream.lower()

    if stream == "science":
        return "You can pursue careers in Engineering, Medicine, Research, Data Science, etc."
    elif stream == "commerce":
        return "You can pursue careers in Business, Finance, Accounting, Marketing, etc."
    elif stream == "arts":
        return "You can pursue careers in Literature, History, Psychology, Sociology, etc."
    else:
        return "Invalid input. Please enter Science, Commerce, or Arts."
    
def show_table():

    table = Table(title = "Career Advisor Expert System : ")

    table.add_column("Stream", justify="center", style="cyan", no_wrap=True)
    table.add_column("Suggested Careers", justify="center", style="magenta")
    table.add_column("Example Careers", justify="center", style="green")

    table.add_row("Science", "Engineering, Medicine, Research, Data Science", "Software Engineer, Doctor, Scientist, Data Analyst")
    table.add_row("Commerce", "Business, Finance, Accounting, Marketing", "Accountant, Financial Analyst, Marketing Manager")
    table.add_row("Arts", "Literature, History, Psychology, Sociology", "Writer, Historian, Psychologist, Sociologist")

    console.print(table)

def show_tree():
    dot = graphviz.Digraph(comment='Career Advisor Expert System')

    dot.node('A', 'Start')
    dot.node('B', 'Input Stream')
    dot.node('C', 'Science')
    dot.node('D', 'Commerce')
    dot.node('E', 'Arts')
    dot.node('F', 'Engineering, Medicine, Research, Data Science')
    dot.node('G', 'Business, Finance, Accounting, Marketing')
    dot.node('H', 'Literature, History, Psychology, Sociology')

    dot.edges(['AB'])
    dot.edge('B', 'C', label='Science')
    dot.edge('B', 'D', label='Commerce')
    dot.edge('B', 'E', label='Arts')
    dot.edge('C', 'F')
    dot.edge('D', 'G')
    dot.edge('E', 'H')

    console.print(dot.source)
    dot.render('career_advisor_expert_system.gv', view=True)

if __name__ == "__main__":
    console.print("[bold green]Welcome to the Career Advisor Expert System![/bold green]")
    console.print("This system will help you choose a career path based on your interests and skills.\n")

    show_table()

    stream = console.input("\nEnter your preferred stream (Science/Commerce/Arts): ")
    advice = career_advisor(stream)
    console.print(f"\n[bold blue]Advice:[/bold blue] {advice}")

    show_tree()