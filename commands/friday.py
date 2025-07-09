from signalbot import Command, Context

class FridayCommand(Command):
    def describe(self) -> str:
        return "🦀 Congratulations sailor, you made it to friday!"

    async def handle(self, c: Context):
        command = c.message.text

        if command == "friday":
            await c.send(
                "https://www.youtube.com/watch?v=pU2SdH1HBuk"
            )
            return