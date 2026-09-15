from user_interface import ShopApplication

def main():
    app = ShopApplication()
    try:
        app.run()
    except (KeyboardInterrupt, EOFError):
        app.console.print("[bold yellow on red]         App close safely        [/bold yellow on red]")
        if app.pending_save:
            app.console.print(
                "[bold yellow on red] Unsave changes remain. Please check Csv file before reSopening [/bold yellow on red]"
            )

if __name__ == "__main__":
    main()
            
