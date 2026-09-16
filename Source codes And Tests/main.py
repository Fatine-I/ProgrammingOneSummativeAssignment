from user_interface import ShopApplication

message ="App close safely"
message2 = "Unsave changes remain. Please check Csv file before reopening "


def main():
    app = ShopApplication()
    try:
        app.run()
    except (KeyboardInterrupt, EOFError):
        app.console.log(message, style="Bold yellow on red",)
        if app.pending_save:
            app.console.log( message2, style="Bold yellow on red" )         

if __name__ == "__main__":
    main()
            
