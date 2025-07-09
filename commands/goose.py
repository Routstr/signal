from signalbot import Command, Context
import subprocess
import re

class GooseCommand(Command):
    def describe(self) -> str:
        return "Honk! Honk! You called the goose!"

    async def handle(self, c: Context):
        command = c.message.text

        if any(greeting in command.lower() for greeting in ["hey goose", "hello goose", "hi goose"]):
            result = subprocess.run(["goose", "run", "--no-session", "-t", "Fetch all the issues from Routstr/proxy, Routstr/routstr-chat and Routstr/frontend and summarize it under the heading **Summary of Current Issues**each repository should get a brief summarize of the current issues. No need to display issues. Show no more than 3 main points per respository"], capture_output=True, text=True)
            raw_output = result.stdout
            output = re.sub(r'\x1b$$[^m]*m', '', raw_output)
            heading = "Summary of Current Issues"
            if heading in output:
                summary = heading + "\n" + output.split(heading, 1)[1].strip()
                await c.send(summary, text_mode="styled")
            else:
                await c.send("Could not find the summary heading in the goose command output.")
            return